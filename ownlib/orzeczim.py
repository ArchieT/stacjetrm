# -*- coding: utf-8 -*-
class orzeczim:
	u"""To jest klasa orzeczenia imiennego i w ogole outputu standardowego dotycząca wyświetlania kolejnego"""

	def __init__(self, row, stac, unx, pracy, lan, jezadr, lanchar):
		self.row = row
		self.stac = stac
		self.unx = unx
		self.lan = lan
		import datetime

		hejoczasuu = []
		for itt in datetime.datetime.fromtimestamp(unx).timetuple():
			hejoczasuu.append(itt)
		dzcz = datetime.datetime(hejoczasuu[0], hejoczasuu[1], hejoczasuu[2], hejoczasuu[3], hejoczasuu[4],
								 hejoczasuu[5]).isoformat(' ')
		self.dzcz = dzcz
		jezykinfoa = lan.dictu
		jezyu = lan
		self.jezyu = jezyu
		adrlocsafe = {
			'001TOR': 'Rynek Staromiejski',
			'002TOR': 'Plac sw. Katarzyny',
			'003TOR': 'Plac Rapackiego',
			'004TOR': 'ul. Bulwar Filadelfijski - Brama Klasztorna',
			'005TOR': 'ul. Szosa Chelminska - Targowisko Miejskie',
			'006TOR': 'ul. Gagarina - Biblioteka Uniwersytecka',
			'007TOR': 'ul. Broniewskiego - Tesco',
			'008TOR': 'ul. Gen. Jozefa Hallera - Polo Market',
			'009TOR': 'ul. Szosa Chelminska - Polo Market',
			'010TOR': 'PKP Torun Glowny',
			'011TOR': 'ul. Dziewulskiego - Komisariat Policji',
			'012TOR': 'ul. Konstytucji 3 Maja - Pawilon Maciej',
			'013TOR': 'ul. Dabrowskiego - Dworzec autobusowy',
                        '014TOR': 'ul. Waly gen. Sikorskiego - Urzad Miasta',
                        '015TOR': 'ul. Gen. Jozefa Bema - Tor-Tor',
                        '016TOR': 'ul. Przysiecka - Barbarka',
                        '017TOR': 'ul. Bazynskich - basen',
                        '018TOR': 'PKP Torun Wschodni',
                        '019TOR': 'ul. Kosciuszki / ul. Swietopelka',
                        '020TOR': 'ul. Mickiewicza / ul. Tujakowskiego',
                        '021TOR': 'ul. Gagarina - Od Nowa',
                        '022TOR': 'ul. Rydygiera / ul. Donimirskiego',
                        '023TOR': 'ul. Kolankowskiego / ul. Kosynierow',
                        '024TOR': 'ul. Sw. Klemensa / ul. Sw. Jozefa',
                        '025TOR': 'ul. Legionow - Rondo Czadcy',
                        '026TOR': 'ul. Zolkiewskiego - Atrium Copernicus'
		}
		adrlocnatio = {
			'001TOR': u'Rynek Staromiejski',
			'002TOR': u'Plac św. Katarzyny',
			'003TOR': u'Plac Rapackiego',
			'004TOR': u'ul. Bulwar Filadelfijski - Brama Klasztorna',
			'005TOR': u'ul. Szosa Chełmińska - Targowisko Miejskie',
			'006TOR': u'ul. Gagarina - Biblioteka Uniwersytecka',
			'007TOR': u'ul. Broniewskiego - Tesco',
			'008TOR': u'ul. Gen. Józefa Hallera - Polo Market',
			'009TOR': u'ul. Szosa Chełmińska - Polo Market',
			'010TOR': u'PKP Toruń Główny',
			'011TOR': u'ul. Dziewulskiego - Komisariat Policji',
			'012TOR': u'ul. Konstytucji 3 Maja - Pawilon Maciej',
			'013TOR': u'ul. Dąbrowskiego - Dworzec autobusowy',
                        '014TOR': u'ul. Wały gen. Sikorskiego - Urząd Miasta',
                        '015TOR': u'ul. Gen. Józefa Bema - Tor-Tor',
                        '016TOR': u'ul. Przysiecka - Barbarka',
                        '017TOR': u'ul. Bażyńskich - basen',
                        '018TOR': u'PKP Toruń Wschodni',
                        '019TOR': u'ul. Kościuszki / ul. Świętopełka',
                        '020TOR': u'ul. Mickiewicza / ul. Tujakowskiego',
                        '021TOR': u'ul. Gagarina - Od Nowa',
                        '022TOR': u'ul. Rydygiera / ul. Donimirskiego',
                        '023TOR': u'ul. Kolankowskiego / ul. Kosynierów',
                        '024TOR': u'ul. Św. Klemensa / ul. Św. Józefa',
                        '025TOR': u'ul. Legionów - Rondo Czadcy',
                        '026TOR': u'ul. Zółkiewskiego - Atrium Copernicus'
		}
		if jezadr == "c":
			ad = jezyu.lanstac
		elif jezadr == 'l':
			if lanchar == 'n':
				ad = adrlocsafe
			elif lanchar == 'y':
				ad = adrlocnatio
			else:
				print u"Gupi błondd"
				print lanchar
				quit()
		else:
			print "Gupppiii bwond"
			quit()
		self.ad = ad

	def orz(self):
		row = self.row
		self.wyd = self.jezyu.wyd(row)
		wyd = self.wyd

	def pisul(self):
		wyd = self.wyd
		dzcz = self.dzcz
		# dz = self.dz
		st = self.stac
		row = self.row
		print dzcz, ":", self.jezyu.dictu['nastacji'], st, wyd

	def pisp(self):
		dzcz = self.dzcz
		# dz = self.dz
		st = self.stac
		row = self.row
		print dzcz, st, row

	def pisc(self):
		import re

		unx = self.unx
		st = self.stac
		stn = int(re.sub(r'\D', "", st))
		row = self.row
		print unx, stn, row

	def pism(self):
		unx = self.unx
		st = self.stac
		row = self.row
		print unx, st, row

	def pisfa(self):
		wyd = self.wyd
		dzcz = self.dzcz
		# dz = self.dz
		st = self.stac
		ad = self.ad
		print dzcz, ":", self.jezyu.dictu['nastacji'], st, wyd, " - ", ad[st]

	def pist(self):
		dzcz = self.dzcz
		# dz = self.dz
		st = self.stac
		row = self.row
		ad = self.ad
		dl = len(ad[st])
		ds = 43 - dl
		# print ds
		# sp = spacje(ds)
		spac = " "
		for i in range(ds):
			spac += ' '
		# s = " "
		# sp = s * ds
		sp = spac
		# for sp in range (0, ds):
		# s = s + " "
		if type(row) == int and row <= 9:
			print "|", dzcz, "|", st, "| ", row, "| ", ad[st], sp, "|"
		elif type(row) == int and row >= 10:
			print "|", dzcz, "|", st, "|", row, "| ", ad[st], sp, "|"
		elif row == "Download failed":
			print "|", dzcz, "|", st, "|%s| " % self.jezyu.dictu['trojliterr'], ad[st], sp, "| %s " % self.jezyu.dictu[
				'downfail']
		else:
			print "|", dzcz, "|", st, "|%s| " % self.jezyu.dictu['trojliterr'], ad[st], sp, "| %s " % self.jezyu.dictu[
				'niepoprwartosc']
