
import os

class app():

	def load(self):
		print("app im running now")

	def run(self):
		print("im running now")

class request():

	def __init__(self):
		self.uri = os.environ["REQUEST_URI"]
		self.segments = self.uri.split("/");

	def get_segment(self, index): 
		
		try:
			return self.segment[index]
		except IndexError:
			pass