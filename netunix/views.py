
from datetime import *

class dotnet_unix(object):
	def __init__(self, unix=None, dotnet=None, real_date=None):
		self.unix = unix
		self.dotnet = dotnet
		self.real_date=real_date
	def now(self):
		if (self.unix is None and self.dotnet is None):
			dotnet = datetime(1,1,1)
			g = datetime.now()
			unix = g - dotnet
			dotnettimestamp = (((unix.days*60*60*24 + unix.seconds)*1000 + unix.microseconds)*100)*100
			return dotnettimestamp
	def fromreal(self):
		if (self.real_date is not None):
			dotnet = datetime(1,1,1)
			f = "%d/%m/%Y %H:%M:%S"
			times = datetime.strptime(real_date, f)
			unix = times - dotnet
			dotnettimestamp = (((unix.days*60*60*24 + unix.seconds)*1000 + unix.microseconds)*100)*100
			return dotnettimestamp
# Create your views here.
