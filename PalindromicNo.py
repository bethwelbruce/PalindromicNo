def is_palindrome(n):
    return str(n) == str(n)[::-1]

t = int(input())

for _ in range(t):
    n = int(input())
    for i in range(n-1, 101100, -1):
        if is_palindrome(i):
            for j in range(999, 99, -1):
                if i % j == 0 and i // j < 1000:
                    print(i)
                    break
            break
print (i)
