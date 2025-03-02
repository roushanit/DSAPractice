import threading
import time

def sleep_sort(numbers):
    def sleep_and_print(n):
        time.sleep(n)  # Sleep for 'n' seconds
        print(n, end=" ")

    threads = []
    for num in numbers:
        thread = threading.Thread(target=sleep_and_print, args=(num,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Ensure all threads finish

# Example usage
numbers = [3, 1, 4, 2, 10, 30, 50]
sleep_sort(numbers)
