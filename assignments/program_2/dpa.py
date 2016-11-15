import threading
import os
from os import system
import locale
import time
import threading
import random
import json
import struct

screenLock = threading.Lock()

# Layout of the table (P = philosopher, f = fork):
#          P0
#       f3    f0
#     P3        P1
#       f2    f1
#          P2

# Number of philosophers at the table. 
# There'll be the same number of forks.
numPhilosophers = 16

# Lists to hold the philosophers and the forks.
# Philosophers are threads while forks are locks.
philosophers = []
forks = []

screenLock = threading.Lock()

class Philosopher(threading.Thread):
		totalRuntime = 0.0

		# def __init__(self, index,window,cell):
		def __init__(self, index):
				threading.Thread.__init__(self)
				self.index = index
				self.lastStart = 0.0
				self.runtime = 0.0
				
		def run(self):
				# Assign left and right fork
				leftForkIndex = self.index
				rightForkIndex = (self.index - 1) % numPhilosophers
				forkPair = ForkPair(leftForkIndex, rightForkIndex)

				# Eat forever
				while True:
						if self.runtime <= Philosopher.totalRuntime / (numPhilosophers - 1):
								forkPair.pickUp()
								self.lastStart = time.time()
								with screenLock:
										print 'Philosopher {0} eating'.format(self.index)
										time.sleep(.05)
								time.sleep(.01)
								forkPair.putDown()
								now = time.time()
								self.runtime += (now - self.lastStart)
								Philosopher.totalRuntime += (now - self.lastStart)

class ForkPair:
		def __init__(self, leftForkIndex, rightForkIndex):
				# Order forks by index to prevent deadlock
				if leftForkIndex > rightForkIndex:
						leftForkIndex, rightForkIndex = rightForkIndex, leftForkIndex
				self.firstFork = forks[leftForkIndex]
				self.secondFork = forks[rightForkIndex]
		

		def pickUp(self):
				# Acquire by starting with the lower index
				self.firstFork.acquire()
				self.secondFork.acquire()

		def putDown(self):
				# The order does not matter here
				self.firstFork.release()
				self.secondFork.release()

if __name__ == "__main__":

		screenLock = threading.Lock()

		
		# Create philosophers and forks
		print forks
		for i in range(0, numPhilosophers):
				philosophers.append(Philosopher(i))
				forks.append(threading.Lock())

		# All philosophers start eating
		for philosopher in philosophers:
				philosopher.start()

		# Allow CTRL + C to exit the program
		try:
				while True: time.sleep(021)
		except (KeyboardInterrupt, SystemExit):
				print ''
				for philosopher in philosophers:
						print 'Philosopher {0} runtime: {1} sec'.format(philosopher.index, philosopher.runtime)
				os._exit(0)