process_list = []
n = int(input("Enter the number of processes: "))

print("Enter the processes PID AT BT")

for i in range(n):
    process_id,arrival_time,burst_time = input().split(" ")
    process_list.append((process_id, int(arrival_time), int(burst_time)))


time_quant = int(input("Enter the time quant: "))


arrival_order = sorted(range(n), key = lambda i : process_list[i][1])


remaining_time = [

     burst_time for process_id, arrival_time, burst_time in process_list

]


completion_time = [0]*n
turnaround_time = [0] * n
waiting_time = [0] *n

current_time = 0
completed_count = 0 
ready_queue = []



while completed_count < n:

    while arrival_order and process_list[arrival_order[0]][1] <= current_time:
        ready_queue.append(arrival_order.pop(0))

    if not ready_queue:
        current_time += 1
        continue

    selected_index = ready_queue.pop(0)

    run_time = min(time_quant, remaining_time[selected_index])

    remaining_time[selected_index] -= run_time
    current_time += run_time

    while arrival_order and process_list[arrival_order[0]][1] <= current_time:
        ready_queue.append(arrival_order.pop(0))

    if remaining_time[selected_index] > 0:
        ready_queue.append(selected_index)
    else:
        pid, arrival, burst = process_list[selected_index]


 
        completion_time[selected_index] = current_time
        turnaround_time[selected_index] = current_time - arrival
        waiting_time[selected_index] = turnaround_time[selected_index] - burst

        completed_count+=1

total_wt = 0
total_tat = 0

print("\nROUND ROBIN\nPID\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    pid, arrival, burst = process_list[i]

    print(f"{pid}\t{arrival}\t{burst}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

    total_wt += waiting_time[i]
    total_tat += turnaround_time[i]

avg_wt = total_wt/n
avg_tat = total_tat/n

print(f"Average waiting time = {avg_wt: .2f}")
print(f"Average turnaround time = {avg_tat: .2f}")