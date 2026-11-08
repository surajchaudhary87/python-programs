import threading

def greet(name):
    print("Hello", name)

t1 = threading.Thread(
    target=greet,
    args=("Suraj",)
)

t1.start()
t1.join()