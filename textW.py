numbers = [1,2,3]

f = open("textExample.txt","w+")

for i in numbers:
	f.write(str(i) + "\n")

f.close()