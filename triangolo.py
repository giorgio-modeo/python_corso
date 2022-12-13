import _thread
def print_time(threadName):
    n=0
    while True:
        print("pdio",n)
        n+=1
# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1",) )
   _thread.start_new_thread( print_time, ("Thread-2",) )
except:
   print("Error: unable to start thread")

while 1:
   pass