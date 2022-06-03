#Program to create Deamon thread
#This program will keep sending "Hello User" message to the user until he is online. 
# His online status is tracked by the Daemon process (timer)
#Once the user exits the main thread and goes offline; the daemon is killed as well

import threading
import time,sys
import logging

#logs the behaviour of the threads
logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

#a non-daemon thread used to indicate that user is logged in
def start_thread():
    logging.debug('Starting')
    for i in range(0, 3):
        print("Hello User")
        time.sleep(5)
    logging.debug('Exiting')

#a daemon thread used to indicate how long the user is online and counts the time
def daemon_timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")


if __name__ == '__main__':

	thread = threading.Thread(name='non-daemon', target=start_thread)

	daemon = threading.Thread(name='daemon', target=daemon_timer)
    # we convert a thread into a daemon by setting the paramter daemon=True
	daemon.setDaemon(True)
    #start both the thread parallel to each other
	daemon.start()
	thread.start()


# input for main thread 
answer = input("DO YOU WISH TO LOG OFF? Enter Yes/No  \n")    

# Once user enters Yes/No the background daemon thread is killed as well