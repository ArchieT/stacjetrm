# -*- coding: utf-8 -*-
class download:
	"Ta klasa będzie po prostu pobierać jeden plik jednej stacji i mówić czy succesful i z jakiego czasu pochodzi plik, ciekawe czy da się wsio w inicie"
	import urllib2
	import time
	
	def __init__(self,stacja):
		if stacja == 0:
			from suma import *
			print "Suma jeszcze nie obsługiwana wszystkiego. Exiting."
			quit()
		elif stacja == 100:
			from suma import *
			print "Suma jeszcze nie obsługiwana wybranych. Exiting."
			quit()
		elif stacja < 10:
			if stacja > 0:
				na = (r'00', str(stacja), r'TOR')
			elif stacja < 0:
				print "Eraro: malkorekta biciklstacio: %s" % str(stacja)
				quit()
		elif stacja > 9:
			if stacja > 12:
				na = (r'0', str(stacja), r'TOR')
			else:
				print "Eraro: malkorekta biciklstacio: %s" % str(stacja)
				quit()
		else:
			print "Eraro: malkorekta biciklstacio: %s" % str(stacja)
			quit()
		stacn = str.join()
		urlt = (r'trm24.pl/panel-trm/', str(stacn), r'.jsp')
		url = str.join(urlt)
		#wejs = urllib2.urlopen(url)
		#we = wejs.read()
		self.url = url
		self.stacn = stacn
	def down(self):
		import urllib2
		import time
		wejs = urllib2.urlopen(self.url)
		czas = time.time()
		self.czas = czas
		we = wejs.read()
		self.we = we
	def row(self):
		from pars import *
		par = pars(self.we,self.stacn)
		rowery = par.rowerry()
		return rowery
	def cza(self):
		return self.czas			
