
from datetime import *
import time

class dotnet_unix(object):		
	def __init__(self, unix=None, real_date=None, dotnet=None):
		self.unix = unix
		self.real_date = real_date
		self.dotnet = dotnet


	def now(self):
		if self.unix is None and self.real_date is None and self.dotnet is None:
			dotnet = datetime(1,1,1)
			g = datetime.now
			unix = g() - dotnet
			dotnettimestamp = (((unix.days*60*60*24 + unix.seconds)*1000 + unix.microseconds)*100)*100
			return dotnettimestamp

	def from_realdate(self, real_date):
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
		if dotnet:
			delta_epoch = (datetime(1970,1,1)) - (datetime(1,1,1))
			desec=timedelta.total_seconds(delta_epoch)
			unixtimestamp = (dotnet/10000000) - desec
			return unixtimestamp


	def to_realdate(self, torealdate):
		unixconvert = self.from_dotnet(torealdate)
		realdate  = datetime.fromtimestamp(unixconvert)
		return realdate


	


# Create your views here.
