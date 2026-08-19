process_list = []
n = int(input("Enter the number of processes: "))

print("Enter the Processes: PID AT CT")


for i in range(n):
    process_id, arrival_time, burst_time = input().split(" ")
    process_list.append((process_id, int(arrival_time), int(burst_time)))

time_quantum = int(input("Enter the time quantum: "))

current_time = 0
completed = 0
done = [False] * n
results = []

while completed < n:
    selected = -1
    shortest_bt = float('inf')


    for i in range(n):
        process_id, arrival_time, burst_time = process_list[i]

        if not done[i] and arrival_time <= current_time:
            if burst_time < shortest_bt:
                shortest_bt = burst_time
                selected = i
    if selected == -1:
        current_time += 1
        continue
    process_id, arrival_time, burst_time = process_list[selected]
    ct = current_time + burst_time
    tat = ct - arrival_time
    wt = tat - burst_time

    current_time = ct
    done[selected] = True
    completed += 1

    results.append((process_id,arrival_time,burst_time,ct,tat,wt))

total_wt = 0
total_tat = 0

print("\nNON PREEMPTIVE\nPID\tAT\tBT\tCT\tTAT\tWT")

for process_id, arrival_time, burst_time, ct, tat, wt in results:
    print(f"{process_id}\t{arrival_time}\t{burst_time}\t{ct}\t{tat}\t{wt}")
    total_wt += wt
    total_tat += tat

avg_wt = total_wt/n
avg_tat = total_tat/n

print(f"Average waiting time = {avg_wt: .2f}")
print(f"Average turnaround time = {avg_tat: .2f}")

np_avg_wt = avg_wt
np_avg_tat = avg_tat


## Preemptive

current_time = 0
completed_count = 0

remaining_time = [
    burst_time for process_id, arrival_time, burst_time in process_list
]

completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

while completed_count < n:
    selected_index = -1

    for i in range(n):
        process_id, arrival_time, burst_time = process_list[i]

        if arrival_time <= current_time and remaining_time[i] > 0:

            if selected_index == -1:
                selected_index = i
            else:
                selected_pid, selected_arrival, selected_burst = process_list[selected_index]

                if remaining_time[i] < remaining_time[selected_index]:
                    selected_index = i
                elif remaining_time[i] == remaining_time[selected_index]:
                    if arrival_time < selected_arrival:
                        selected_index = i

    if selected_index == -1:
        current_time += 1
        continue

    run_time = min(time_quantum, remaining_time[selected_index])

    remaining_time[selected_index] -= run_time
    current_time += run_time


    if remaining_time[selected_index] == 0:
        pid, arrival, burst = process_list[selected_index]

        completion_time[selected_index] = current_time
        turnaround_time[selected_index] = current_time - arrival
        waiting_time[selected_index] = turnaround_time[selected_index] - burst

        completed_count += 1

total_wt = 0
total_tat = 0

print("\nPREEMPTIVE\nPID\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    pid, arrival, burst = process_list[i]

    print(f"{pid}\t{arrival}\t{burst}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

    total_wt += waiting_time[i]
    total_tat += turnaround_time[i]

avg_wt = total_wt/n
avg_tat = total_tat/n

print(f"Average waiting time = {avg_wt: .2f}")
print(f"Average turnaround time = {avg_tat: .2f}")

p_avg_wt = avg_wt
p_avg_tat = avg_tat

## Comparison

print("\nCOMPARISON\nMETRIC\t\t\tNON PREEMPTIVE\tPREEMPTIVE")
print(f"Average waiting time\t{np_avg_wt: .2f}\t\t{p_avg_wt: .2f}")
print(f"Average turnaround time\t{np_avg_tat: .2f}\t\t{p_avg_tat: .2f}")

if p_avg_wt < np_avg_wt:
    print(f"\nPreemptive has lower average waiting time by {np_avg_wt - p_avg_wt: .2f}")
elif np_avg_wt < p_avg_wt:
    print(f"\nNon preemptive has lower average waiting time by {p_avg_wt - np_avg_wt: .2f}")
else:
    print("\nBoth have the same average waiting time")

if p_avg_tat < np_avg_tat:
    print(f"Preemptive has lower average turnaround time by {np_avg_tat - p_avg_tat: .2f}")
elif np_avg_tat < p_avg_tat:
    print(f"Non preemptive has lower average turnaround time by {p_avg_tat - np_avg_tat: .2f}")
else:
    print("Both have the same average turnaround time")

if p_avg_wt < np_avg_wt and p_avg_tat < np_avg_tat:
    print("Better algorithm = PREEMPTIVE")
elif np_avg_wt < p_avg_wt and np_avg_tat < p_avg_tat:
    print("Better algorithm = NON PREEMPTIVE")
else:
    print("Better algorithm = depends on which metric is prioritized")