import threading

import time

def worker(number):

    print(worker)

    time.sleep(number)

    return

for i in range(5):

    t = threading.Thread(target=worker,args=(5,))

    t.start()