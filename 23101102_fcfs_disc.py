def main():

    n = int(input("Enter the number of requests: "))

    print("Enter the disk requests:")
    requests = []

    for i in range(n):
        request = int(input())
        requests.append(request)

    head = int(input("Enter the initial head position: "))

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

    print("\n")

    print(f"Total Head Movement = {total_movement}")


if __name__ == "__main__":
    main()