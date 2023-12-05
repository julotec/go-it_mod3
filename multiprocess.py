import multiprocessing



def is_divisible(number, divisor):
    return number % divisor == 0
def factorize_sync(number):
    factors = []
    for i in range(1, number + 1):
        if is_divisible(number, i):
            factors.append(i)
    return factors


def factorize_parallel(number, pool):
    factors = []
    results = []
    for i in range(1, number + 1):
        results.append(pool.apply_async(is_divisible, args=(number, i)))
    pool.close()
    pool.join()
    for i, result in enumerate(results, 1):
        if result.get():
            factors.append(i)
    return factors


def factorize(*numbers):
    results = []
    for number in numbers:
        results.append(factorize_sync(number))

    # Uncomment the following lines to use parallel version
    # pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # results = pool.starmap(factorize_parallel, [(number, pool) for number in numbers])
    # pool.close()
    # pool.join()

    return results


# Test
numbers_to_factorize = [12, 24, 36, 48]
result_sync = factorize(*numbers_to_factorize)
print("Synchronous Result:", result_sync)

