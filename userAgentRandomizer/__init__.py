from glob import glob
from random import randint
import os
class userAgents(object):
	def __init__(self):
		files_ = glob('userAgents/assets/*.txt')
		self.uas = []
		for file_ in files_:
			with open(file_,'r') as f:
				records_ = f.read().split('\n')
				f.close()
			for rec in records_:
				self.uas.append(rec)
	def random(self): 
		return self.uas[randint(0,len(self.uas)-1)]

	def count(self):
		return len(self.uas)

if __name__ == "__main__":
	ua = userAgents()
	print(ua.random())
	print(ua.count())