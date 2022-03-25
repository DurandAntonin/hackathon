class Soldats:
	def __init__(self,joueurId,groupeId,tuplePos,size):
		self.joueurId = joueurId
		self.groupeId = groupeId
		self.tuplePos = tuplePos
		self.size = size

	def getPos(self):
		return self.tuplePos
	
	def setPosSoldat(self,nouvellePos):
		self.tuplePos = nouvellePos

	def setSize(self,nouvelleSize):
		self.size -= nouvelleSize
	
	def getJoueurId(self):
		return self.joueurId

class Evenements:
	def __init__(self,posEvents,typeEvent,niveauEvent,tempsEvent):
		self.posEvents = posEvents
		self.typeEvent = typeEvent
		self.niveauEvent = niveauEvent
		self.tempsEvent = tempsEvent

	def getPosEvent(self):
		return self.posEvents

class Grille:
	def __init__(self,nbCases,soldatDepart):
		self.dicoRisk = self.constructionDico(nbCases)
		self.setCasesEnnemies = set()
		self.setCasesAllies = set()
		self.setCasesMalus = set()
		self.setCasesBonus = set()
		self.setCasesLibres = set(dicoRisk.keys())
		
		self.setCasesAllies.add(soldatDepart)

	def constructionDico(self,nbCases):		
		for i in range(nbCases):
			for j in range(nbCases):
				dicoRisk[(i,j)] = [None]
	def getEvents(self):
		return self.setCasesEnnemies
	
	def getSoldats(self):
		return self.setCasesAllies

	def voisinagePossibles(self,pos):
		##pos est un tuple de int
		listePosPossibles = []
		listeVoisinsPossibles = [(pos[0]+1,pos[0]),(pos[0]-1,pos[0]),(pos[0],pos[0]+1),(pos[0],pos[0]-1)]
			
		for posPossible in listeVoisinsPossibles:
			if posPossible in self.setCasesLibres:
				listePosPossibles.append(posPossible)
		return listePosPossibles

	def deplacementSoldat(self,soldat,newPos,newSoldat=False,sizeSoldat=None):
		if soldat.getJoueurId() != ID_GROUPE:	
			self.setCasesEnnemies.remove(soldat.getPos())
			self.setCasesLibres.remove(soldat.getPos())
			soldat.setPosSoldat(newPos)
			self.setCasesLibres.remove(newPos)
			self.setCasesEnnemies.add(newPos)
		else:	
			#on regarde si un nouveau groupe de soldat est crée
			if newSoldat == True:
				soldatNouveau = soldat(ID_GROUPE,NB_GROUPES,newPos,sizeSoldat)
				#on diminue la taille du soldat 
				soldat.setSize(sizeSoldat)
				NB_GROUPES += 1

			else:
				self.setCasesAllies.remove(soldat.getPos())
				self.setCasesLibres.remove(soldat.getPos())
				soldat.setPosSoldat(newPos)
				self.setCasesLibres.remove(newPos)
				self.setCasesAllies.add(newPos)

	def suppressionEvent(self,event):
		if event in self.setCasesMalus:
			self.setCasesMalus.remove(event)
		else:
			self.setCasesBonus.remove(event)
		self.setCasesLibres.add(event.getPosEvent())
	
	def mortSoldat(self,soldat):
		##on regarde si c'est un ennemi ou un allié
		if soldat.getJoueurId() == ID_GROUPE:
			self.setCasesAllies.remove(soldat)
		else:
			self.setCasesEnnemies.remove(soldat)
		self.setCasesLibres.add(soldat.getPos())
	
