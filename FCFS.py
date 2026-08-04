def main():
    n = int(input("Enter the number of processes: "))
    print("Enter the processes (format --> PID AT BT):")

    processes = []
    for _ in range(n):
        
        PID, AT, BT = input().split()
        processes.append((PID, int(AT), int(BT)))
    processes.sort(key=lambda x: x[1])

    crnt_tm = 0
    full_cal = []
    for pid, at, bt in processes:
        if crnt_tm < at:
            crnt_tm = at        
        ct = crnt_tm + bt
        tat = ct - at
        wt = tat - bt
        crnt_tm = ct
        full_cal.append((pid, at, bt, ct, tat, wt))


    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    total_tat = total_wt = 0
    for pid, at, bt, ct, tat, wt in full_cal:
        print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")
        total_tat += tat
        total_wt += wt

    print(f"\nAverage TAT: {total_tat / n:.2f}")
    print(f"Average WT: {total_wt / n:.2f}")


if __name__ == "__main__":
    main()