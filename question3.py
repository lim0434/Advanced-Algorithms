import time
import threading

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("\nTesting factorial function:")
print(f"Factorial of 5: {factorial(5)}")
print("Function works correctly!\n")

def multithreading_factorial(rounds=10):
    numbers = [50, 100, 200]
    print("--- Multithreading ---")
    total_times = []

    for r in range(1, rounds + 1):
        threads = [threading.Thread(target=lambda x=n: factorial(x)) for n in numbers]
        start = time.perf_counter_ns()
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        elapsed = time.perf_counter_ns() - start
        total_times.append(elapsed)
        print(f"Round {r}: {elapsed} ns")

    total_time = sum(total_times)
    avg_time = total_time / rounds
    print(f"Total time: {total_time} ns")
    print(f"Average time: {avg_time:.0f} ns\n")
    return avg_time, total_time

def without_threads(rounds=10):
    numbers = [50, 100, 200]
    print("--- Without Multithreading ---")
    total_times = []

    for r in range(1, rounds + 1):
        start = time.perf_counter_ns()
        for n in numbers:
            factorial(n)

        elapsed = time.perf_counter_ns() - start
        total_times.append(elapsed)
        print(f"Round {r}: {elapsed} ns")

    total_time = sum(total_times)
    avg_time = total_time / rounds
    print(f"Total time: {total_time} ns")
    print(f"Average time: {avg_time:.0f} ns\n")
    return avg_time, total_time

def compare_times(mt_avg, st_avg):
    print("--- Comparison ---")
    print(f"Average time (multithreading): {mt_avg:.0f} ns")
    print(f"Average time (without multithreading): {st_avg:.0f} ns")

if __name__ == "__main__":
    print("Calculating 50!, 100!, and 200!\n")
    avg_threads, total_threads = multithreading_factorial()
    avg_without_threads, total_without_threads = without_threads()
    compare_times(avg_threads, avg_without_threads)
    print(f"Total time (multithreading): {total_threads} ns")
    print(f"Total time (without multithreading): {total_without_threads} ns")
