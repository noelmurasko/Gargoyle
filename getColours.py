import os

# Used to collect the colours in GargoyleColours.txt. Could in principle 
# be used to collect colours from any pallete organized in this way.

# The pallete function returns a list of Colours. Each colour has 3 strings:
# a description, name, and hex. 
# For example: Black, Lead, #222222

class Colour:

	def __init__(self, description, name, hexCode):
		self.desc=description
		self.name=name
		self.hex=hexCode

		# Integers between 0 and 255.
		R=int(hexCode[1:3],16)
		G=int(hexCode[3:5],16)
		B=int(hexCode[5:7],16)

		self.rgb="("+str(R)+", "+str(G)+", "+str(B)+")"

		# Floats between 0 and 1.
		Rf=R/255
		Bf=B/255
		Gf=G/255

		K=1-max(Rf,Bf,Gf)
		C=int((1-Rf-K)/(1-K)*100)
		M=int((1-Gf-K)/(1-K)*100)
		Y=int((1-Bf-K)/(1-K)*100)
		K=int(K*100)
		self.cymk="("+str(C)+"%, "+str(M)+"%, "+str(Y)+"%, "+str(K)+"%)"

def pallete():
	pallete = []
	file=open('GargoyleColours.txt','r')
	text=file.read()
	start=text.find('----',0)+5
	while start < len(text):
		b1=text.find('|',start)
		b2=text.find('|',b1+1)
		description=text[start:b1-1]
		if description[0]=="\n":
			description = description[1:]
		name=text[b1+2:b2-1]
		hexCode=text[b2+2:b2+9]
		pallete.append(Colour(description, name, hexCode))
		start=b2+10
	file.close()
	return pallete