# -*- coding: utf-8 -*-
class paramdemonwszystkich:
	u"To jest klasa parametrów demonwszystkich"
	import sys
	import re

	def __init__(self,argu)
		self.argu = argu
		for a in range(1,argu):
			at = argu[a]
			if at[0] == "l":
				try:
					if at[1] == "e":
						lang = "e"
						from esperanto import *
						lan = esperanto()
					elif at[1] == "a":
						lang = "a"
						from english import *
						lan = english()
					elif at[1] == "p":
						lang = "p"
						from polski import *
						lan = polski()
					elif at[1] == "d":
						lang = "d"
						from deutsch import *
						lan = deutsch()
				except:
					from esperanto import *
					espera = esperanto()
					from english import *
					engli = english()
					from polish import *
					polsk = polski()
					from deutsch import *
					deuts = deutsch()
					for badlang in ((espera.badlang()), (engli.badlang()), (polsk.badlang()), (deuts.badlang())):
						print "%s: %s"(badlang,at[1:])
					quit()
			elif at[0] == "t":
				if at[1] == "d":
					t = deft
				else:
					tc = re.sub("\D","",at)
					try:
						t = int(tc)
					except:
						print "%s: %s"(lan.badwaittime,tc)
						quit()
