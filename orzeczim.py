class orzeczim:
	"To jest klasa orzeczenia imiennego, w trybach u i l"
	
	def __init__(self,row,stac,unx,dz,cz):
		self.row = row
		self.stac = stac
		self.unx = unx
		self.dz = dz
		self.cz = cz

	def orz(self):
		row = self.row
		if row == 0:
			self.wyd = "estas neniu bicikloj"
		elif row == -1:
			self.wyd = "okazis iun eraron, cxar gxi transdonas ke tie estas -1 biciklo - kaj tio estas negativa kvanto \n         "
		elif row <= 0:
			self.wyd = "okazis iun eraron, cxar gxi transdonas ke tie estas " + str(row) + " bicikloj - kaj tio estas negativa kvanto \n          "
		elif row == 1:
			self.wyd = "estas 1  biciklo    "
		elif row >= 2:
			if row <= 9:
				self.wyd = ("estas " + str(row) + "  bicikloj   ")
			if row >= 10:
				self.wyd = ("estas " + str(row) + " bicikloj   ")
		else:
			self.wyd = ", ni ne scias kiom bicikloj estas tie, cxar dum la akiroprovon de la biciklokvanto okazis la eraro"
		wyd = self.wyd

	def pisul(self):
		wyd = self.wyd
		cz = self.cz
		dz = self.dz
		st = self.stac
		row = self.row
		print dz, cz, "Al la biciklastacion", st, wyd

	def pisp(self):
		cz = self.cz
		dz = self.dz
		st = self.stac
		row = self.row
		print dz, cz, st, row

	def pisc(self):
		import re
		unx = self.unx
		st = self.stac
		stn = int(re.sub(r'\D',"",st))
		row = self.row
		print unx, stn, row
	def pism(self):
		unx = self.unx
		st = self.stac
		row = self.row
		print unx, st, row
	def pisa(self):
		wyd = self.wyd
		cz = self.cz
		dz = self.dz
		st = self.stac
		row = self.row
		ad = {'001TOR': 'Rynek Staromiejski', '002TOR': 'Plac sw. Katarzyny', '003TOR': 'Plac Rapackiego', '004TOR': 'ul. Bulwar Filadelfijski - Brama Klasztorna', '005TOR': 'ul. Szosa Chelminska - Targowisko Miejskie', '006TOR': 'ul. Gagarina - Biblioteka Uniwersytecka', '007TOR': 'ul. Broniewskiego - Tesco', '008TOR': 'ul. Gen. Jozefa Hallera - Polo Market', '009TOR': 'ul. Szosa Chelminska - Polo Market', '010TOR': 'PKP Torun Glowny', '011TOR': 'ul. Dziewulskiego - Komisariat Policji', '012TOR': 'ul. Konstytucji 3 Maja - Pawilon Maciej'}
		print dz, cz, "Al la biciklastacion", st, wyd, " - ", ad[st]
