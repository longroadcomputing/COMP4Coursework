
counties = []

with open("counties.txt",mode="r",encoding="utf-8") as myFile:
	for line in myFile:
		counties.append(line.rstrip("\n"))
		

print(counties)
