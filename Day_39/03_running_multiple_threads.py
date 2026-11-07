import threading
import time

def download_file():
    print("Downloading file...")
    time.sleep(2)
    print("Download completed!")

def send_email():
    print("Sending email...")
    time.sleep(1)
    print("Email sent!")

t1 = threading.Thread(target=download_file)
t2 = threading.Thread(target=send_email)

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks completed!")