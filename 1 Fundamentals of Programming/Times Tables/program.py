def multiplies (table, startnum, endnum, pupilName):
	print("Hi, " + (pupilName if pupilName != "Joe" else "Joe mama") + " ... here is your times table")
	for i in range (startnum, endnum + 1):
		print (str(table) + " x " + str(i) + " = " + str(table * i))

name = input ("What is your name?\n")
print ("Enter times table, start number and end number")

table = int(input())
startnum = int(input())
endnum = int(input())

multiplies(table, startnum, endnum, name)

