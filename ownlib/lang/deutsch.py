# -*- coding: utf-8 -*-
class de_natio:
	u"""Das ist ein sprechtpackage, lecz niestety kompletnie nie jest zrobiony."""

	def __init__(self):
		lang = "de_natio"

	@property
	def dictu(self):
		slo = {
			"badwaittime": u"Incorrect waiting time",
			"badstacparam": u"Incorrect station parameter",
			"badlang": u"Incorrect language",
			"badpracy": u"Incorrect work mode",
			"baddebugu": u"Incorrect debug mode",
			"badsm": u"Incorrect write mode",
			"nastacji": u"On the station",
			"sumallnotsupported": u"The feature of sum of all of the stations isn't yet supported. Exiting.",
			"sumchonotsupported": u"The feature of sum of the chosen stations isn't yet supported. Exiting.",
			"elektulabormodon": u"Choose a work mode",
			"sevivolasketiunprogramonfunkcias": u"if you want this program work",
			"najprawdopodobniejtrybpracy": u"Most probably the work mode",
			"jestnieprawidlowy": u"is incorrect",
			"niepoprwartosc": u"Incorrect value",
			"downfail": u"Download failed",
			"trojliterr": u"ERR",
		}
		return slo

	@staticmethod
	def wyd(row):
		if type(row) == int and row == 0:
			wyd = u"is no bicycles "
		elif type(row) == int and row == -1:
			wyd = u"probably encountered an error, as it shows that there is -1 bicycle, and this is a negative count \n		 "
		elif type(row) == int and row <= 0:
			wyd = u"probably encountered an error, as it shows that there is " + str(
				" {:2d} ".format(row)) + " bicycles, and this is a negative count \n		  "
		elif type(row) == int and row == 1:
			wyd = u"is  1 bicycle  "
		elif type(row) == int and row >= 2:
			if row <= 9:
				wyd = (u"is" + str(" {:2d} ".format(row)) + u"bicycles ")
			if row >= 10:
				wyd = (u"is" + str(" {:2d} ".format(row)) + u"bicycles ")
		elif row == "Download failed":
			wyd = u", there is no data how many bicycles there are, because an attempt to download the information has failed"
		else:
			wyd = u", there is no data how many bicycles there are, because an attempt to get known encountered an error, it returned [type: '%s', value: '%s']" % (
				type(row), str(" {:2d} ".format(row)))
		return wyd

	@property
	def lanstac(self):
		lanstadict = {
			'001TOR': u'Rynek Staromiejski',
			'002TOR': u'Plac sw. Katarzyny',
			'003TOR': u'Plac Rapackiego',
			'004TOR': u'ul. Bulwar Filadelfijski - Brama Klasztorna',
			'005TOR': u'ul. Szosa Chelminska - Targowisko Miejskie',
			'006TOR': u'ul. Gagarina - Biblioteka Uniwersytecka',
			'007TOR': u'ul. Broniewskiego - Tesco',
			'008TOR': u'ul. Gen. Jozefa Hallera - Polo Market',
			'009TOR': u'ul. Szosa Chelminska - Polo Market',
			'010TOR': u'PKP Torun Glowny',
			'011TOR': u'ul. Dziewulskiego - Komisariat Policji',
			'012TOR': u'ul. Konstytucji 3 Maja - Pawilon Maciej',
			'013TOR': u'ul. Dabrowskiego — Dworzec autobusowy',
                        '014TOR': u'ul. Waly gen. Sikorskiego - Urzad Miasta',
                        '015TOR': u'ul. Gen. Jozefa Bema - Tor-Tor',
                        '016TOR': u'ul. Przysiecka - Barbarka',
                        '017TOR': u'ul. Bazynskich - basen',
                        '018TOR': u'PKP Torun Wschodni',
                        '019TOR': u'ul. Kosciuszki / ul. Swietopelka',
                        '020TOR': u'ul. Mickiewicza / ul. Tujakowskiego',
                        '021TOR': u'ul. Gagarina - Od Nowa',
                        '022TOR': u'ul. Rydygiera / ul. Donimirskiego',
                        '023TOR': u'ul. Kolankowskiego / ul. Kosynierow',
                        '024TOR': u'ul. Sw. Klemensa / ul. Sw. Jozefa',
                        '025TOR': u'ul. Legionow - Rondo Czadcy',
                        '026TOR': u'ul. Zolkiewskiego - Atrium Copernicus'

		}
		return lanstadict

	# powyzsze trzeba bedzie przetlumaczyc na niemiecki ze znaczkami


class de_safe:
	u"""Das ist ein sprechtpackage, lecz niestety kompletnie nie jest zrobiony."""

	def __init__(self):
		lang = "de_safe"

	@property
	def dictu(self):
		slo = {
			"badwaittime": "Incorrect waiting time",
			"badstacparam": "Incorrect station parameter",
			"badlang": "Incorrect language",
			"badpracy": "Incorrect work mode",
			"baddebugu": "Incorrect debug mode",
			"badsm": "Incorrect write mode",
			"nastacji": "On the station",
			"sumallnotsupported": "The feature of sum of all of the stations isn't yet supported. Exiting.",
			"sumchonotsupported": "The feature of sum of the chosen stations isn't yet supported. Exiting.",
			"elektulabormodon": "Choose a work mode",
			"sevivolasketiunprogramonfunkcias": "if you want this program work",
			"najprawdopodobniejtrybpracy": "Most probably the work mode",
			"jestnieprawidlowy": "is incorrect",
			"niepoprwartosc": "Incorrect value",
			"downfail": "Download failed",
			"trojliterr": "ERR",
		}
		return slo

	@staticmethod
	def wyd(row):
		if type(row) == int and row == 0:
			wyd = "is no bicycles "
		elif type(row) == int and row == -1:
			wyd = "probably encountered an error, as it shows that there is -1 bicycle, and this is a negative count \n		 "
		elif type(row) == int and row <= 0:
			wyd = "probably encountered an error, as it shows that there is " + str(
				" {:2d} ".format(row)) + " bicycles, and this is a negative count \n		  "
		elif type(row) == int and row == 1:
			wyd = "is  1 bicycle  "
		elif type(row) == int and row >= 2:
			if row <= 9:
				wyd = ("is" + str(" {:2d} ".format(row)) + "bicycles ")
			if row >= 10:
				wyd = ("is" + str(" {:2d} ".format(row)) + "bicycles ")
		elif row == "Download failed":
			wyd = ", there is no data how many bicycles there are, because an attempt to download the information has failed"
		else:
			wyd = ", there is no data how many bicycles there are, because an attempt to get known encountered an error, it returned [type: '%s', value: '%s']" % (
				type(row), str(" {:2d} ".format(row)))
		return wyd

	@property
	def lanstac(self):
		lanstadict = {
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
			'013TOR': 'ul. Dabrowskiego — Dworzec autobusowy',
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
		return lanstadict
		# powyzsze trzeba bedzie przetlumaczyc na niemiecki w angielskim alfabecie
