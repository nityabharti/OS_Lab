def findWaitingTime(n, ar_bt, wt, quantum):
	rem_bt = []
	for i in range(n):
		rem_bt.append(ar_bt[i].copy())
	t = 0
	t = ar_bt[0][0]
	while True:
		done = True
		for i in range(n):
			if (rem_bt[i][2] > 0) :
				done = False			
				if (rem_bt[i][2] > quantum) :
					t += quantum
					rem_bt[i][2] -= quantum
				else:
					t = t + rem_bt[i][2]
					wt[i] = t - ar_bt[i][2]-ar_bt[i][0]
					rem_bt[i][2] = 0
				
		if (done == True):
			break

def findTurnAroundTime(n, ar_bt, wt, tat):
	for i in range(n):
		tat[i] = ar_bt[i][2] + wt[i]


def findavgTime(n, ar_bt, quantum):
	wt = [0] * n
	tat = [0] * n
	findWaitingTime(n, ar_bt, wt, quantum)
	findTurnAroundTime(n, ar_bt, wt, tat)
	print("Processes Arrival Time  Burst Time	 \tWaiting Time \tTurn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(ar_bt[i][1],"\t ", ar_bt[i][0], "\t\t\t", ar_bt[i][2],
			"\t\t", wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = %.5f "% (total_tat / n))
	

if __name__ =="__main__":

	n = int(input("Enter Number of processes => "))
	print("Enter arrival, process ID, burst time for each process")
	arrival_burst_times = []
	for i in range(n):
		arrival_burst = list(map(int,input().split()))
		arrival_burst_times.append(arrival_burst)

	arrival_burst_times.sort()
	print(arrival_burst_times)
	quantum = int(input("Enter the value of quantum time => "))
	findavgTime(n, arrival_burst_times, quantum)