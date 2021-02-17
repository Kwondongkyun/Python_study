a = int(input())
for _ in range(1, a+1):
    print(_)

-> 116 ms


a = int(input())
for _ in range(1, a):
    print(_+1)

-> 120 ms

