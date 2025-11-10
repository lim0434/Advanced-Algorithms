import threading
import time

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("=" * 80)
print("\nTesting factorial function:")
print(f"5! = {factorial(5)}")
print(f"10! = {factorial(10)}")
print("Function works correctly!\n")

class FactorialThread(threading.Thread):
    def __init__(self, n, thread):
        threading.Thread.__init__(self)
        self.n = n
        self.thread = thread
        self.result = None
        self.start_time = None
        self.end_time = None

    def run(self):
        self.start_time = time.perf_counter_ns()
        self.result = factorial(self.n)
        self.end_time = time.perf_counter_ns()

def run_multithreaded_factorial():
    thread1 = FactorialThread(50, "Thread-50")
    thread2 = FactorialThread(100, "Thread-100")
    thread3 = FactorialThread(200, "Thread-200")
    threads = [thread1, thread2, thread3]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    earliest_start = min(t.start_time for t in threads)
    latest_end = max(t.end_time for t in threads)
    total_time = latest_end - earliest_start
    return total_time, threads

#part 4
def run_single_threaded_factorial():
    start_time = time.perf_counter_ns()

    result_50 = factorial(50)
    result_100 = factorial(100)
    result_200 = factorial(200)

    end_time = time.perf_counter_ns()
    total_time = end_time - start_time
    return total_time

#part 5
def run_experiments():
    rounds = 10
    multithreaded_times = []
    single_threaded_times = []

    print("Running experiments...")

    for round_num in range(1, rounds + 1):

        # Multithreaded
        mt_time, _ = run_multithreaded_factorial()
        multithreaded_times.append(mt_time)

        # Single-threaded
        st_time = run_single_threaded_factorial()
        single_threaded_times.append(st_time)

    print("All rounds completed!\n")
    return multithreaded_times, single_threaded_times
mt_times, st_times = run_experiments()

#part 6
print("=" * 80)
print("EXPERIMENT RESULTS - MULTITHREADED vs SINGLE-THREADED")
print("=" * 80)
print(f"\n{'Round':<10} {'Multithreaded (ns)':<25} {'Single-Threaded (ns)':<25} {'Difference (ns)'}")
print("-" * 80)

for i in range(len(mt_times)):
    diff = mt_times[i] - st_times[i]
    diff_sign = "+" if diff > 0 else ""
    print(f"{i + 1:<10} {mt_times[i]:<25,} {st_times[i]:<25,} {diff_sign}{diff:,}")

# Calculate averages
avg_mt = sum(mt_times) / len(mt_times)
avg_st = sum(st_times) / len(st_times)
avg_diff = avg_mt - avg_st

print("-" * 80)
print(f"{'AVERAGE':<10} {avg_mt:<25,.2f} {avg_st:<25,.2f} {avg_diff:+,.2f}")
print("=" * 80)

#part 7
print("\n" + "=" * 80)
print("ANALYSIS AND CONCLUSION")
print("=" * 80)

# Determine which is faster
if avg_mt < avg_st:
    faster = "Multithreaded"
    slower = "Single-threaded"
    improvement = (avg_st / avg_mt - 1) * 100
    time_diff = avg_st - avg_mt
else:
    faster = "Single-threaded"
    slower = "Multithreaded"
    improvement = (avg_mt / avg_st - 1) * 100
    time_diff = avg_mt - avg_st

print(f"""
PERFORMANCE SUMMARY:
--------------------
Multithreaded Average:    {avg_mt:,.2f} nanoseconds
Single-Threaded Average:  {avg_st:,.2f} nanoseconds
Time Difference:          {time_diff:,.2f} nanoseconds

{faster} was FASTER by {improvement:.2f}%""")