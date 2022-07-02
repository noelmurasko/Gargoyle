import os

# Used to collect the colours in GargoyleColours.txt. Could in principle 
# be used to collect colours from any pallete organized in this way.
# In the future, you could also use this compute other color formats such as CYMK.

# The pallete function returns a list of Colours. Each colour has 3 strings:
# a description, name, and hex. 
# For example: Black, Lead, #222222

class Colour:

	def __init__(self, description, name, hexCode):
		self.desc = description
		self.name = name
		self.hex = hexCode

def pallete():
	pallete = []
	file=open('GargoyleColours.txt','r')
	text=file.read()
	start=text.find('----',0)+5
	while start < len(text):
		b1 = text.find('|',start)
		b2 = text.find('|',b1+1)
		description=text[start:b1-1]
		if description[0]=="\n":
			description = description[1:]
		name=text[b1+2:b2-1]
		hexCode=text[b2+2:b2+9]
		pallete.append(Colour(description, name, hexCode))
		start=b2+10
	file.close()
	return pallete
