# share a numpy array between processes using a manager
from multiprocessing import Process
from multiprocessing.managers import BaseManager

import numpy as np
from numpy import ones


# custom manager to support custom classes
class CustomManager (BaseManager):
	# nothing
	pass


# task executed in a child process
def task(data_proxy):
	# report details of the array
	print(f'Array sum (in child): {data_proxy.sum ()}')
	dataAll = np.frombuffer (data_proxy, dtype = int, count = len(data_proxy))
	data_proxy = data_proxy.reshape (26, 40)
	dataSumm = np.hsplit (data_proxy, 4)
	dataP1 = dataSumm[0]
	dataP2 = dataSumm[1]
	dataP3 = dataSumm[2]
	dataP4 = dataSumm[3]
	dataP1[0][0] = 212
	print('RESHAPE = ', dataP1)
# protect the entry point
if 1 == 1:
	# register a function for creating numpy arrays on the manager
	CustomManager.register ('shared_array', ones)
	# create and start the custom manager
	with CustomManager() as manager:
		# define the size of the numpy array
		n = 26*40
		# create a shared numpy array
		data_proxy = manager.shared_array ((n,))
		data_proxy = data_proxy.reshape (26, 40)
		dataSumm = np.hsplit (data_proxy, 4)
		dataP1 = dataSumm[0]
		dataP2 = dataSumm[1]
		dataP3 = dataSumm[2]
		dataP4 = dataSumm[3]

		print (f'Array created on host: {data_proxy}')
		# confirm content
		print (f'Array sum: {data_proxy.sum ()}')
		# start a child process
		process = Process (target = task, args = (data_proxy,))
		process.start ()
		process.join ()