# open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().replace('\n',' ').split(' ')

# put the data into integers and in a list
n = list(map(int, f))
n.pop(0) # remove the number of values (first digit)
l = len(n) # number of digits

# function to convert seconds into days, hours, minutes, seconds
def time_conv(sec):
    days = sec // 86400
    hours = (sec % 86400) // 3600
    minutes = (sec - days*86400 - hours*3600) // 60
    seconds = (sec - days*86400 - hours*3600 - minutes*60)

    l = "("+str(days)+" "+str(hours)+" "+str(minutes)+" "+str(seconds)+")"
    return(l)

i = 0
string = ""
while (i < l):
    d1 = n[i] * 86400
    h1 = n[i+1] * 3600
    m1 = n[i+2] * 60
    s1 = n[i+3]
    d2 = n[i+4] * 86400
    h2 = n[i+5] * 3600
    m2 = n[i+6] * 60
    s2 = n[i+7]

    travel_time_sec = (s2+m2+h2+d2) - (s1+m1+h1+d1)

    string = string + " " + str(time_conv(travel_time_sec))
    i += 8

print(string)