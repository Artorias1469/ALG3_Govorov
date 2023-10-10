import random
import time
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
print("Size\tAverage Time (key found)\tWorst Time (key not found)")
print("---------------------------------------------------------")
for size in sizes:
    arr = [random.randint(0, 999) for _ in range(size)]
    m = random.randint(1, size - 2)
    key = arr[m]

    start_time = time.time()
    for _ in range(100000):
        linear_search(arr, key)
    avg_time = (time.time() - start_time) / 100000

    start_time = time.time()
    for _ in range(100000):
        linear_search(arr, -1)
    worst_time = (time.time() - start_time) / 100000

    print(f"{size}\t{avg_time:.6f}\t\t\t{worst_time:.6f}")
