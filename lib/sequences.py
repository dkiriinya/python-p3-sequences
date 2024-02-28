def print_fibonacci(length):
    fibonacci_array = []

    for i in range(length):
        if i < 2:
            fibonacci_array.append(i)
        else:
            fibonacci_array.append(fibonacci_array[i-1] + fibonacci_array[i-2])
    print(fibonacci_array)

print_fibonacci(14)
