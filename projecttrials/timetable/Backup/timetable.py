
infile = "inputFile.txt"
outfile="outFile.txt"
cars=list()
a= "a"
b="b"
with open(infile) as f1:
	for  line in f1:
		row=line.split(",")
		cars.append(row)
	print (cars[0][1])
with open(outfile,'w') as f2:
	for car in cars:
		f2.write(car[0]+","+car[6]+"\n")

