from multiprocessing import Pool, cpu_count
import time

def find_divisors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def factorize(*numbers):
    with Pool(cpu_count()) as pool:
        result = pool.map(find_divisors, numbers)
    return result

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    start_time = time.time()
    result = factorize(*numbers)
    end_time = time.time()

    for i, num in enumerate(numbers):
        print(f"Factors of {num}: {result[i]}")

    print(f"Parallel version took {end_time - start_time} seconds")

