import time

def factorize(*numbers):
    result = []
    for number in numbers:
        divisors = [i for i in range(1, number + 1) if number % i == 0]
        result.append(divisors)
    return result

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    start_time = time.time()
    result = factorize(*numbers)
    end_time = time.time()

    for i, num in enumerate(numbers):
        print(f"Factors of {num}: {result[i]}")

    print(f"Synchronous version took {end_time - start_time} seconds")
