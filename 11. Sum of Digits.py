# open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().replace('\n',' ').split(' ')

# put the data into integers and in a list
n = list(map(int, f))
n.pop(0) # remove the number of values (first digit)
l = len(n) # number of digits

# function using repetetive division by 10, and remainders, to determine the digits in number
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

i = 0
string = ""
while (i < l-2):
    ans = n[i] * n[i+1] + n[i+2] # a*b+c
    string = string + " " + str(sum(digits(ans)))
    i += 3

print(string)