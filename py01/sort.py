def me():
    arrs = [111, 3243, 432, 4, 5, 32, 4, 2314, 12, 3123]
    for i in arrs:
        print(i, end=" ")
me()
print()
def factorial(n):
	result = n
	for i in range(1,n):
		result *= i
	return result
def method(n):
	if n == 1:
		return 1
	else:
		return n * method(n-1)
print(factorial(3))
print(method(3))