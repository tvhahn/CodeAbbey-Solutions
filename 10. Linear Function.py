#open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().replace('\n',' ').split(' ')

#put the data into integers and in a list
n = list(map(int, f))

n.pop(0)
l = len(n)

i = 0
string = ""
while (i < l-3):
    x1 = n[i]
    y1 = n[i+1]
    x2 = n[i+2]
    y2 = n[i+3]

    a = int((y2-y1) / (x2-x1))
    b = -a*(x1)+y1

    string = string + "(" + str(a) + " " + str(b) + ") "
    i += 4

print(string)