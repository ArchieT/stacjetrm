# -*- coding: utf-8 -*-
class english:
	u"""This is an English language file"""

	def __init__(self):
		lang = "en"

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
		# powyzsze trzeba bedzie przetlumaczyc na angielski
