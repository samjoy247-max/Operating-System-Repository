process_list = []

n = int(input("Enter the number of processes: "))

print("Enter the Processes: PID AT BT PR")

for i in range(n):
    process_id, arrival_time, burst_time, priority = input().split(" ")
    process_list.append((process_id, int(arrival_time), int(burst_time), int(priority)))


## Non Preemptive

current_time = 0
completed = 0
done = [False] * n
results = []

while completed < n:
    selected = -1
    highest_priority = float('inf')

    for i in range(n):
        process_id, arrival_time, burst_time, priority = process_list[i]

        if not done[i] and arrival_time <= current_time:
            if priority < highest_priority:
                highest_priority = priority
                selected = i

            elif priority == highest_priority:
                if arrival_time < process_list[selected][1]:
                    selected = i

    if selected == -1:
        current_time += 1
        continue

    process_id, arrival_time, burst_time, priority = process_list[selected]

    ct = current_time + burst_time
    tat = ct - arrival_time
    wt = tat - burst_time

    current_time = ct
    done[selected] = True
    completed += 1

    results.append((process_id, arrival_time, burst_time, priority, ct, tat, wt))


total_wt = 0
total_tat = 0

print("\nNON PREEMPTIVE")
print("PID\tAT\tBT\tPR\tCT\tTAT\tWT")

for process_id, arrival_time, burst_time, priority, ct, tat, wt in results:
    print(f"{process_id}\t{arrival_time}\t{burst_time}\t{priority}\t{ct}\t{tat}\t{wt}")

    total_wt += wt
    total_tat += tat

avg_wt = total_wt / n
avg_tat = total_tat / n

print(f"Average waiting time = {avg_wt:.2f}")
print(f"Average turnaround time = {avg_tat:.2f}")

np_avg_wt = avg_wt
np_avg_tat = avg_tat


## Preemptive

current_time = 0
completed_count = 0

remaining_time = [
    burst_time for process_id, arrival_time, burst_time, priority in process_list
]

completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

while completed_count < n:
    selected_index = -1

    for i in range(n):
        process_id, arrival_time, burst_time, priority = process_list[i]

        if arrival_time <= current_time and remaining_time[i] > 0:

            if selected_index == -1:
                selected_index = i

            else:
                selected_pid, selected_arrival, selected_burst, selected_priority = process_list[selected_index]

                if priority < selected_priority:
                    selected_index = i

                elif priority == selected_priority:
                    if arrival_time < selected_arrival:
                        selected_index = i

    if selected_index == -1:
        current_time += 1
        continue

    remaining_time[selected_index] -= 1
    current_time += 1

    if remaining_time[selected_index] == 0:
        pid, arrival, burst, pr = process_list[selected_index]

        completion_time[selected_index] = current_time
        turnaround_time[selected_index] = current_time - arrival
        waiting_time[selected_index] = turnaround_time[selected_index] - burst

        completed_count += 1


total_wt = 0
total_tat = 0

print("\nPREEMPTIVE")
print("PID\tAT\tBT\tPR\tCT\tTAT\tWT")

for i in range(n):
    pid, arrival, burst, pr = process_list[i]

    print(
        f"{pid}\t{arrival}\t{burst}\t{pr}\t"
        f"{completion_time[i]}\t"
        f"{turnaround_time[i]}\t"
        f"{waiting_time[i]}"
    )

    total_wt += waiting_time[i]
    total_tat += turnaround_time[i]

avg_wt = total_wt / n
avg_tat = total_tat / n

print(f"Average waiting time = {avg_wt:.2f}")
print(f"Average turnaround time = {avg_tat:.2f}")

p_avg_wt = avg_wt
p_avg_tat = avg_tat


print("\nCOMPARISON")
print("METRIC\t\t\tNON PREEMPTIVE\tPREEMPTIVE")

print(f"Average waiting time\t{np_avg_wt:.2f}\t\t{p_avg_wt:.2f}")
print(f"Average turnaround time\t{np_avg_tat:.2f}\t\t{p_avg_tat:.2f}")


print("\n--- Waiting Time Comparison ---")

if p_avg_wt < np_avg_wt:
    difference = np_avg_wt - p_avg_wt
    print(f"Preemptive scheduling performs better in waiting time by {difference:.2f}.")

elif np_avg_wt < p_avg_wt:
    difference = p_avg_wt - np_avg_wt
    print(f"Non-preemptive scheduling performs better in waiting time by {difference:.2f}.")

else:
    print("Both scheduling methods have the same average waiting time.")


print("\n--- Turnaround Time Comparison ---")

if p_avg_tat < np_avg_tat:
    difference = np_avg_tat - p_avg_tat
    print(f"Preemptive scheduling performs better in turnaround time by {difference:.2f}.")

elif np_avg_tat < p_avg_tat:
    difference = p_avg_tat - np_avg_tat
    print(f"Non-preemptive scheduling performs better in turnaround time by {difference:.2f}.")

else:
    print("Both scheduling methods have the same average turnaround time.")


print("\n--- Final Comparison ---")

if p_avg_wt < np_avg_wt and p_avg_tat < np_avg_tat:
    print("Overall, PREEMPTIVE scheduling gives better performance.")

elif np_avg_wt < p_avg_wt and np_avg_tat < p_avg_tat:
    print("Overall, NON-PREEMPTIVE scheduling gives better performance.")

else:
    print("The better scheduling method depends on the performance metric being considered.")