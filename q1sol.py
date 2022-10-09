prev_even = 0
cnt = 0
on = 1
for i in range(10):
    current = int(input())
    if prev_even and (current % 2 == 0) and on:
        cnt += 1
        on = 0
    on = 1 if current % 2 == 1 else on
    prev_even = 1 if (current % 2 == 0) else 0
print(cnt)
