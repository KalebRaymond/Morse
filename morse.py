class node:
	def __init__(self, c):
		self.left = None
		self.right = None
		self.c = c
		


# class tree: 
	# def __init__(self, c):
		# self.root = node(c)
	
	# def __init__(self, rootc, leftc, rightc):
		# self.root = node(rootc)
		
	# def setLeft(self, c):
		# self.left = node(c)
	# def getLeft(self)
		# return 

n = node(None)

nE = node('E')
n.left = nE
nT = node('T')
n.right = nT

nI = node('I')
nE.left = nI
nA = node('A')
nE.right = nA
nN = node('N')
nT.left = nN
nM = node('M')
nT.right = nM

nS = node('S')
nI.left = nS
nU = node('U')
nI.right = nU
nR = node('R')
nA.left = nR
nW = node('W')
nA.right = nW
nD = node('D')
nN.left = nD
nK = node('K')
nN.right = nK
nG = node('G')
nM.left = nG
nO = node('O')
nM.right = nO

nH = node('H')
nS.left = nH
nV = node('V')
nS.right = nV
nF = node('F')
nU.left = nF
n2parent = node(None)
nU.right = n2parent
nL = node('L')
nR.left = nL
nP = node('P')
nW.left = nP

morse = "... ..- .-. ."
translated = ""
cur_node = n
for c in morse:
	if(c == "."):
		cur_node = cur_node.left
	elif(c == "-"):
		cur_node = cur_node.right
	else:
	#TRY AND CATCH INCORRECT CHARACTERS IE '........................................'
		translated += cur_node.c
		cur_node = n
translated += cur_node.c

print(translated)

