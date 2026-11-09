# What is Multiprocessing?
#   --Multiprocessing means using multiple processes to execute tasks.


import multiprocessing

def calculate_square(number):
    print("Square:", number * number)

if __name__ == "__main__":
    process1 = multiprocessing.Process(
        target=calculate_square,
        args=(5,)
    )

    process1.start()
    process1.join()

    print("Main process finished")