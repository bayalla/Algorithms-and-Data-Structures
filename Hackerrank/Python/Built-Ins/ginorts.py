s = sorted(input())
num= list(filter(str.isnumeric, s ))
odd =list(filter(lambda x: int(x) % 2 != 0, num))
even = list(filter(lambda x: int(x) % 2 == 0, num))
lower = list(filter(str.islower, s))
upper = list(filter(str.isupper, s))
print(*(lower + upper + odd + even), sep='')