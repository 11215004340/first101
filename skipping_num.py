for i in range(1,9):
    if i == 3:
        print("skipping 3 in the inner loop.")
        continue

    if i == 7:
        print("reached 7, breaking outer loop.")
        break
    print(i)
