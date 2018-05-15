
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
	def from_unix(self, unix):
		dotnet = datetime(1,1,1)
		g = datetime.fromtimestamp(float(unix))
		d = g - dotnet
		dotnettimestamp = (((d.days*60*60*24 + d.seconds)*1000 + d.microseconds)*100)*100
		return dotnettimestamp
		
	def from_dotnet(self, dotnet):
		delta_epoch = datetime(1970,1,1)-datetime(1,1,1)
		desec=timedelta.total_seconds(delta_epoch)
		dotnettimestamp = (dotnet/10000000) - desec
		return dotnettimestamp
# Create your views here.
