class node:
	def __init__(self, c):
		self.left = None
		self.right = None
		self.c = c

#Generates tree based on string in level order. Each node holds a single character from the string.
def create_morse_tree(root, vals):
	queue = []
	queue.append(root)
	curIndex = 0
	while(curIndex < len(vals)):
		if(vals[curIndex] == '-'):
			queue[0].c = ""
		else:
			queue[0].c = vals[curIndex]
		
		queue[0].left = node(None)
		queue[0].right = node(None)
		queue.append(queue[0].left)
		queue.append(queue[0].right)
		queue.pop(0)
		curIndex += 1
		
		
n = node(None)
create_morse_tree(n, "-ETIANMSURWDKGOHVF-L-PJBXCYZQ--54-3---2-------16-------7---8-90")

morse = ".. - / .-- .- ... / - .... . / -... . ... - / --- ..-. / - .. -- . ... / .. - / .-- .- ... / - .... . / .-- --- .-. ... - / --- ..-. / - .. -- . ..."
translated = ""
cur_node = n
for c in morse:
	if(c == "."):
		cur_node = cur_node.left
	elif(c == "-"):
		cur_node = cur_node.right
	elif(c == "/"):
		translated += " "
	else:
	#TRY AND CATCH ILLEGAL CHARACTERS
		translated += cur_node.c
		cur_node = n
translated += cur_node.c

print(translated)

