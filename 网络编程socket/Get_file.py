
from re import L
from matplotlib.pyplot import flag
from numpy import arange
import requests
from threading import Thread, Lock
import sys


# flag=False

# lock=Lock()

def send_request(url):
    # lock.acquire()
    # global flag
    # lock.release()
    # i=0
    while True:
        r = requests.get(url)
        # print(r.status_code)
        if r.status_code == 200:
            print("ok")
            break
            # print(i)
            # lock.acquire()
            # flag=True
            # lock.release()

send_request("http://192.168.157.166/uploadlabs/upload/upload.php")



def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <url>")
        sys.exit(1)
    for _ in range(4):
        t = Thread(target=send_request, args=(sys.argv[1],))
        t.start()
        t.join()

if __name__ == "__main__":
    main()