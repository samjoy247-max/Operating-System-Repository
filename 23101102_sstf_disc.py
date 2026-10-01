n = int(input("Enter the number of requests: "))

print("Enter the disk requests (space separated):")
requests = list(map(int, input().split()))

head = int(input("Enter the initial head position: "))

current_head = head
total_movement = 0

print("\nSSTF DISK SCHEDULING")
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

print("\n")
print(f"Total Head Movement = {total_movement}")