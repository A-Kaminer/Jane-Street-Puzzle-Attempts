trisum = 0
count = 1

while count < 100:
    trisum += count
    if trisum % 17 == 0:
        print(f"{count} | {trisum} | {trisum / 17}")
    count += 1
