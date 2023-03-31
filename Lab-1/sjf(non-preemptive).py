def arrangeArrival(n, queue):
	for i in range(0, n):
		for j in range(i, n-i-1):
			if queue[1][j] > queue[1][j+1]:
				for k in range(0, n):
					queue[k][j], queue[k][j+1] = queue[k][j+1], queue[k][j]


def CompletionTime(n, queue):
	value = 0
	queue[3][0] = queue[1][0] + queue[2][0]
	queue[5][0] = queue[3][0] - queue[1][0]
	queue[4][0] = queue[5][0] - queue[2][0]
	for i in range(1, n):
		temp = queue[3][i-1]
		mini = queue[2][i]
		for j in range(i, n):
			if temp >= queue[1][j] and mini >= queue[2][j]:
				mini = queue[2][j]
				value = j
		queue[3][value] = temp + queue[2][value]
		queue[5][value] = queue[3][value] - queue[1][value]
		queue[4][value] = queue[5][value] - queue[2][value]
		for k in range(0, 6):
			queue[k][value], queue[k][i] = queue[k][i], queue[k][value]


if __name__ == '__main__':
	btm = []
	atm = []
	n = int(input("Enter the number of processes: "))
	for i in range(n):
		bt = int(input("Enter burst time for process p{} : ".format(i+1)))
		btm.append(bt)
		at = int(input("Enter arrival time for process p{} : ".format(i+1)))
		atm.append(at)
	
	arr = [[int(i) for i in range(1, n+1)], atm,
		btm, [0]*n, [0]*n, [0]*n]	
	
	arrangeArrival(n, arr)
	CompletionTime(n, arr)
	print("Process\t\tArrival\t\tBurst\t\tCompletion\t\tWaiting\t\tTurnaround ")
	waitingtime = 0
	turaroundtime = 0
	for i in range(0, n):
		print(arr[0][i], "\t\t", arr[1][i], "\t\t", arr[2][i],
			"\t\t", arr[3][i], "\t\t", arr[4][i], "\t\t\t", arr[5][i])
		waitingtime += arr[4][i]
		turaroundtime += arr[5][i]
	print("Average waiting time is ", (waitingtime/n))
	print("Average Turnaround Time is ", (turaroundtime/n))
	







