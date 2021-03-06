# -*- coding: utf-8 -*-
class multipokaz:
	"""Ta klasa bedzie pokazywala wszystkie stacje w jednej linijce, w formie ludzkiej tabelki
	oraz w formie bardziej kompowej (API)"""
	# czasu = datetime.datetime()
	# self.czasu = czasu
	# czasu = datetime.datetime()
	# def __init__(self,rowerdict,pracy,debugu,unix,dz,cz):
	def __init__(self, stacje, pracy, debugu, rowslo, lan, lanchar):
		self.stacje = stacje
		self.debugu = debugu
		self.pracy = pracy

	def header(self):
		headdown = "_______________________"
		qeaddown = headdown
		keaddown = u"———————————————————————"
		stacjetab = ""
		stacje = self.stacje
		for sh in stacje:
			if int(sh) == 0:
				# print "Error: station %s"(str(sh))
				# quit()
				st = "All | "
				ht = '|Sum|'
				qt = "_____"
				kt = u"—————"
			elif int(sh) == 100:
				st = "Spc | "
				ht = '|Sum|'
				qt = "_____"
				kt = u"—————"
			elif int(sh) < 10:
				st = str(sh) + "  | "
				ht = "____"
				qt = ht
				kt = u"————"
			elif int(sh) <= 26:
				st = str(sh) + " | "
				ht = "____"
				qt = ht
				kt = u"————"
			else:
				print "Error: station %s" % (str(sh))
				quit()
			stacjetab += st
			headdown = headdown + ht + "_"
			qeaddown = qeaddown + qt + "_"
			keaddown = keaddown + kt + u"—"
		# print stacjetab
		print qeaddown
		print headdown
		print '| Czas:	  Stacje—> |', (
			str(stacjetab))  # <— to jeszcze wróci, ale dla debugu testujemy na linię wyżej
		print keaddown

	def stacprint(self, stacdict, unixtime):
		# if stacdict.keys() == stacje
		# self.pstacprint(stacdict,unixtime)
		# else:
		import datetime
		import operator

		stacje = self.stacje
		ifcheck1 = []
		iffcheck2 = []
		for ifs in stacdict.keys():
			ifcheck1.append(int(ifs))
		for ifs2 in stacje:
			iffcheck2.append(int(ifs2))
		iffcheck2.sort(operator.lt)
		ifocheck2 = set(iffcheck2)
		ifcheck2 = list(ifocheck2)
		if ifcheck1 == ifcheck2:
			self.pstacprint(stacdict, stacje, unixtime)
		else:
			if True:
				print ifcheck1
				print ifcheck2
				print "Error: ifcheck1 doesn't equal ifcheck2. Exiting. ——multipokaz"
				quit()

		# datetime.format
		# czasu = datetime.datetime()
		datum = datetime.datetime.fromtimestamp(unixtime)
		# print datum #debug
		# data = strftime("%Y—%m—%d %H:%M:%S", datum)
		datem = datum.strftime("%Y—%m—%d %H:%M:%S")
		rowerostring = str(self.pstacprint(stacdict, stacje, unixtime))
		# dato = str(datem)
		printstac = '| ' + str(datem) + ' |' + rowerostring
		# printstac =
		# print ("| %s |%s" % (str(datem),rowerostring))
		# print "| ", datem, " |", rowerostring #(str(datem),rowerostring)
		print printstac

	def pstacprint(self, stacdict, stacje, unixtime):
		tsh = " "
		for s in stacje:
			try:
				ts = stacdict[s]
			except:
				try:
					ts = stacdict[str(s)]
				except:
					ts = stacdict[int(s)]
			its = int(ts)
			tts = self.ppstacprint(its, s)
			tsh += tts
		return tsh

	def morethansto(self, its, s):
		# while its > 100:
		# its = its - 100
		# its =
		if its > 999:
			while its > 1000:
				its -= 1000
			tss = self.ppstacprint(its, s)
		elif its < 1000:
			if int(s) == 0 or int(s) == 100:
				tss = str(its) + " | "
			else:
				tss = str(its) + "? "
		return tss

	def ppstacprint(self, its, s):
		if its < 0:
			its *= -1
		if its < 0:
			if int(s) == 0:
				print "Error: bikes count %s on station SumAll" % (str(its))
			elif int(s) == 100:
				print "Error: bikes count %s on station SumSpc" % (str(its))
			else:
				print "Error: bikes count %s on station %s" % (str(its), str(s))
			quit()
		elif its < 10:
			if int(s) == 0 or int(s) == 100:
				if its == 0:
					tss = str(its) + "———| "
				else:
					tss = str(its) + "   | "
			else:
				if its == 0:
					tss = str(its) + "——| "
				else:
					tss = str(its) + "  | "
		elif its < 20:
			if int(s) == 0 or int(s) == 100:
				tss = str(its) + "  | "
			else:
				tss = str(its) + " | "
		elif its > 19:
			if its < 100:
				if int(s) == 0 or int(s) == 100:
					tss = str(its) + "  | "
				else:
					tss = str(its) + "?| "
			elif its > 100:
				tss = self.morethansto(its, s)
		return str(tss)
