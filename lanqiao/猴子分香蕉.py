end = start = 5
step = 1
remain = 4
count = 10
while remain > 0:
    start += step
    end = start
    # print(f'New Round {end=}')
    if end % 5 != 0:
        remain=4
        continue
    # count -= 1
    # if count < 0:
    #     break
    while remain > 0:
        # print(f'S1 {end=} {remain=}')
        if end % 4 != 0:
            remain=4
            break
        end = end//4*5
        end += remain
        remain -= 1
        # print(f'S2 {end=} {remain=}')
print(end)
