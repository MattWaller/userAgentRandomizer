from glob import glob
import os, random


class userAgents(object):
	def __init__(self):
		files_ = glob(f'{os.path.dirname(os.path.realpath(__file__))}/assets/*.txt')
		self.uas,self.Chrome,self.Edge,self.Firefox,self.Opera,self.Safari = [],[],[],[],[],[]
		for file_ in files_:
			with open(file_,'r') as f:
				records_ = f.read().split('\n')
				f.close()
			for rec in records_:
				self.uas.append(rec)
				if 'Chrome' in file_:
					self.Chrome.append(rec)
				elif 'Edge' in file_:
					self.Edge.append(rec)
				elif 'Firefox' in file_:
					self.Firefox.append(rec)
				elif 'Opera' in file_:
					self.Opera.append(rec)
				elif 'Safari' in file_:
					self.Safari.append(rec)
	def random(self,engine=None):
		if engine == 'Chrome':
			return random.choice(self.Chrome)
		elif engine == 'Edge':
			return random.choice(self.Edge)
		elif engine == 'Firefox':
			return random.choice(self.Firefox)
		elif engine == 'Opera':
			return random.choice(self.Opera)
		elif engine == 'Safari':
			return random.choice(self.Safari)
		else: 
			return random.choice(self.uas)

	def count(self):
		return len(self.uas)

if __name__ == "__main__":
	ua = userAgents()
	print(ua.random('Firefox'))
	print(ua.count())