n = int(input("Enter the number of requests: "))

print("Enter the disk requests (space separated):")
requests = list(map(int, input().split()))

head = int(input("Enter the initial head position: "))
direction = input("Enter the direction Left/Right: ").lower()


## FCFS

current_head = head
total_movement = 0

print("\nFCFS DISK SCHEDULING")
print("Order:", end=" ")

print(current_head, end="")

for request in requests:

    movement = abs(current_head - request)

    total_movement += movement

    current_head = request

    print(" ->", request, end="")



print(f"Total Head Movement = {total_movement}")
print("\n")

fcfs_total = total_movement


## SSTF

current_head = head
total_movement = 0

print("SSTF DISK SCHEDULING")
print("Order:", end=" ")
print(current_head, end="")

remaining = requests.copy()

while remaining:
    closest = remaining[0]
    min_distance = abs(current_head - closest)

    for request in remaining:
        distance = abs(current_head - request)
        if distance < min_distance:
            min_distance = distance
            closest = request

    total_movement += min_distance
    current_head = closest
    print(" ->", closest, end="")

    remaining.remove(closest)


print(f"Total Head Movement = {total_movement}")

sstf_total = total_movement


## SCAN

requests.append(head)
requests.sort()

index = requests.index(head)

left = requests[:index]
right = requests[index+1:]

seek_sequence = []
total_movement = 0

if direction == "right":
    seek_sequence = right + left[::-1]
else:
    seek_sequence = left[::-1] + right

current = head
print("\nSCAN DISK SCHEDULING")
print("Order:", end=" ")
print(current, end="")

for r in seek_sequence:
    total_movement += abs(current - r)
    current = r
    print(" ->", r, end="")

print(f"\nTotal_movement: {total_movement}\n")

look_total = total_movement


## Comparison

print("COMPARISON")
print("ALGORITHM\tTOTAL HEAD MOVEMENT")
print(f"FCFS\t\t{fcfs_total}")
print(f"SSTF\t\t{sstf_total}")
print(f"SCAN\t\t{look_total}")

smallest = min(fcfs_total, sstf_total, look_total)

winners = []
if fcfs_total == smallest:
    winners.append("FCFS")
if sstf_total == smallest:
    winners.append("SSTF")
if look_total == smallest:
    winners.append("SCAN")

if len(winners) == 1:
    print(f"\nBest algorithm for this dataset = {winners[0]}")
else:
    print(f"\nBoth {' and '.join(winners)} give the same (best) total head movement")