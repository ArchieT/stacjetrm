# -*- coding: utf-8 -*-
class getjednoczesnie:
	"To jest klasa pobierania jednoczesnego"
	# import time

	def __init__(self, stacje, pracy, debugu, lan, jezadr, lanchar, iwri, idis, tor):
		import Queue
		import threading

		self.tor = tor
		if tor == 0:
			self.torin = "nico"
		elif tor == 1:
			from tordown import tordown

			self.torin = tordown(debugu)
		else:
			print "Tor parameter variable doesn't contain 0 nor 1; Exiting."
			quit()
		self.lan = lan
		self.jezadr = jezadr
		self.lanchar = lanchar
		sa = 0
		ssa = 0
		sw = 0
		ssw = 0
		stacdict = {}
		slownikczasow = ()
		q = Queue.Queue()
		self.pracy = pracy

		def kolejka(q, s, iwri, idis):
			q.put(self.si(s, iwri, idis))

		for s in stacje:
			sa = 0
			sw = 0
			a = self.si(s, iwri, idis)
			if a[0] == 'a':
				sa = 1
				ssa = 1
			elif a[0] == 'w':
				sw = 1
				ssw = 1
			else:
				t = threading.Thread(target=kolejka, args=(q, s, iwri, idis))
				t.daemon = True
				t.start()
		if tor == 1:
			self.torin.zabij()

	def si(self, s, iwri, idis):
		lan = self.lan
		sa = 0
		sw = 0
		if int(s) == 0:
			sa = 1
			a = 'a'
			return a
		elif int(s) == 100:
			sw = 1
			a = 'w'
			return a
		elif int(s) < 0:
			o = int(s) * (-1)
			a = self.si(o, iwri, idis)
			return a
		elif int(s) < 13:
			from download import download

			thisisthedownloadinstance = download(int(s), lan.dictu, self.tor, self.torin)
			a = thisisthedownloadinstance.raz()
			if iwri == 1:
				print "instawrite"
			if idis == 1:
				self.praca(int(s), int(a[0]), int(a[1]), self.pracy)
				return a
		else:
			jezodict = lan.dictu
			print "%s: %s" % (jezodict['badstacparam'], str(s))
			quit()

	def praca(self, st, row, utim, pr):
		lan = self.lan
		jezadr = self.jezadr
		lanchar = self.lanchar
		from pokaz import pokaz

		if pr == 'n':
			pracowanie = 'nie'
		#		elif pr == 'f' or pr == 'l' or pr == 'u' or pr == 'a' or pr == 't' or pr == 'k' or pr == 'c' or pr == 'm':
		else:
			pokaz(row, st, utim, pr, lan, jezadr, lanchar)

	def razpraca(self, stli, rowslo, pr, debugu):
		lan = self.lan
		#jezadr = self.jezadr
		lanchar = self.lanchar
		from multipokaz import multipokaz

		if pr == 'n':
			pracowanie = 'nie'
		else:
			multipokaz(stli, pr, debugu, rowslo, lan, lanchar)

	def razwrajt(self, stli, rowslo, utim, pr):
		pass

	def kolwrajt(self, st, row, utim, pr):
		pass

	def wrajt(self, st, row, utim, pr):
		pass

	def slowstac(self):
		return self.stacdict

	def slowczas(self):
		return self.slwcza

# http://stackoverflow.com/questions/2846653/python-multithreading-for-dummies
