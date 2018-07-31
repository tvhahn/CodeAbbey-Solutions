# open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().replace('\n',' ').split(' ')

# put the data into integers and in a list
n = list(map(int, f))
n.pop(0) # remove the number of values (first digit)
l = len(n) # number of digits

# function using repetetive division by 10, and remainders, to determine the digits in number - do this rather than int() function
def digits(num):
    whole_num = num // 10
    remainder = num % 10
    digit_list = [remainder]

    if whole_num == 0:
        return(digit_list)
    else:
        while whole_num > 0:
            remainder = whole_num % 10
            whole_num = whole_num // 10
            digit_list.append(remainder)
        return(digit_list)

# function to calculate weighted sum of digits
def wsd(num):
    l = len(str(num))
    digs = digits(num)
    i = 0
    sum_list = []
    while (i < l):
        sum_list.append(digs[l-1-i]*(i+1))
        i += 1
    return(sum(sum_list))

i = 0
string = ""
while (i < l):
    weighted_sum = wsd(n[i])
    string = string + " " + str(weighted_sum)
    i += 1

print(string)