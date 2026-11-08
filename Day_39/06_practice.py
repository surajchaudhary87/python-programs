
import threading
import multiprocessing
import time


# Task 1: First thread
def download_file():
    print("Downloading file...")
    time.sleep(2)
    print("File downloaded successfully!")


# Task 2: Second thread
def send_email():
    print("Sending email...")
    time.sleep(1)
    print("Email sent successfully!")


# Task 3: Thread with arguments
def greet_user(name):
    print(f"Hello, {name}!")


# Task 4: Multiprocessing
def calculate_square(number):
    print(f"Square of {number}: {number * number}")


def run_multithreading():
    print("\n--- MULTITHREADING ---")

    thread1 = threading.Thread(target=download_file)
    thread2 = threading.Thread(target=send_email)
    thread3 = threading.Thread(
        target=greet_user,
        args=("Suraj",)
    )

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("All threads completed!")


def run_multiprocessing():
    print("\n--- MULTIPROCESSING ---")

    numbers = [5, 10, 15, 20]

    processes = []

    for number in numbers:
        process = multiprocessing.Process(
            target=calculate_square,
            args=(number,)
        )

        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All processes completed!")


def main():
    print("===== PYTHON CONCURRENCY PROJECT =====")

    run_multithreading()
    run_multiprocessing()

    print("\nProgram finished successfully!")


if __name__ == "__main__":
    main()
