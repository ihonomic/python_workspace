#! Multithreading is a way of continuing other block of code while another is process
# Is the reverse of single-threaded (MOST COMMON)
import threading
import time
print('Start of program.')


def takeANap(text):
    time.sleep(5)
    print('Wake up!', text)


threadObj = threading.Thread(target=takeANap, args=["Red"])
threadObj.start()
print('End of program.')

#   Note - Multiple threads running at the same time can cause issues called "Concurrency issues"
#    when threads read and write variables at the same time, causing the threads to trip over each other
#   Try to avoid threads reading and writing the same variables
