n = int(input("Enter the number of requests: "))
print("Enter the disk requests (space separated):")
requests = list(map(int, input().split()))
head = int(input("Enter the initial head position: "))
direction = input("Enter the direction Left/Right: ").lower()

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
print("\nLOOK DISK SCHEDULING")
print("Order:", end=" ")
print(current, end="")

for r in seek_sequence:
    total_movement += abs(current - r)
    current = r
    print(" ->", r, end="")

print(f"\nTotal_movement: {total_movement}\n")