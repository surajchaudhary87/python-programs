# What is a Thread?
#   --A thread is a smaller unit of execution inside a process.

# What is Multithreading?
#   --Multithreading means running multiple threads within one process.

import threading
import time

def task():
    for i in range(1, 4):
        print("Task:", i)
        time.sleep(1)

thread1 = threading.Thread(target=task)

thread1.start()
thread1.join()

print("Main program finished")