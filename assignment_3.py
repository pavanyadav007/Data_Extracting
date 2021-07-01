# 1 Correct the malformed time string , for e.g "5:70:65" to "6:11:05"

def Time_changes_check(time1):
    string_len = time1.split(":")
    hours = int(string_len[0])
    mins = int(string_len[1])
    secs = int(string_len[2])
    if secs >= 60:
        mins +=secs//60
        secs %=60
    if mins >=60:
        hours +=mins//60
        mins %=60
    result = str(hours)+":"+str(mins)+":"+str(secs)
    return('"'+ result +'"')

# 2 Correct the malformed date string , for e.g. "45/8/2018" to "14/9/2018"

def DATE_checking_excess(date1):
    temp_chech_in = date1.split("/")
    days = int(temp_chech_in[0])
    months = int(temp_chech_in[1])
    years = int(temp_chech_in[2])

    if months == 1 or months == 3 or months == 5 or months == 7 or months == 8 or months == 10 or months == 12:
        last_date_end = 31

    elif months == 2:
        if years % 4 == 0:
            if years % 100 == 0:
                if years % 400 == 0:
                    last_date_end = 29
                last_date_end = 28
            last_date_end = 29
        last_date_end = 28

    else:
        last_date_end = 30

    if days > last_date_end:
        months += days // last_date_end
        days %= last_date_end

    if months > 12:
        years += months // 12
        months %= 12

    result = str(days) + "/" + str(months) + "/" + str(years)
    return('"'+result+'"')


# 3 Convert ip address from "a.b.c.d" format into integer and vice versa
import ipaddress
def ip4_number(addr1):
    # converting IPv4 address to int
    addr2 = ipaddress.ip_address('0.0.0.123')
    return(int(ipaddress.ip_address(addr1)))
    return(int(addr2))

def ip6_number(addr3):
    # converting IPv6 address to int
    return(int(ipaddress.ip_address(addr3)))

def number_ip4(number1):
    # converting int to IPv4 address
    return(ipaddress.ip_address(number1))
    return(ipaddress.ip_address(123))

def number_ip6(number2):
    # converting int to IPv6 address
    return(ipaddress.ip_address(number2))


#4  Check whether given string is isogram or not

def solve(word):
   char_list = []
   for char in word:
      if char.isalpha():
         if char in char_list:
            return False
            char_list.append(char)
   return True
#s = "education"

#5 Given a string, find the mexican wave

def MEX_wave_generation(s):
 new=[]
 for i, val in enumerate(s[:]):
    up=s[i].upper()
    c=s.replace(s[i],up)
    new.append(c)
 return(new)

# 6 Given a number, find the largest number by deleting single digit (order of digits will remain same)
def maxnumber(n, k):
    for i in range(0, k):
        ans = 0
        i = 1
        while n // i > 0:
            temp = (n//(i * 10))*i + (n % i)
            i *= 10
            if temp > ans:
                ans = temp
                n = ans      
            return ans
#n = 6358
#k = 1
#print(maxnumber(n, k))


#7 Given a number, find the largest number by shuffling the digits

def printMaximum(inum):
    count = [0 for x in range(10)]
    string = str(inum)
    for i in range(len(string)):
        count[int(string[i])] = count[int(string[i])] +  1
        result = 0
        multiplier = 1
        
    for i in range(10):
        while count[i] > 0:
            result = result + ( i * multiplier )
            count[i] = count[i] - 1
            multiplier = multiplier * 10
    return result

#8 Compute the word frequency in given message

def freq(str):

	# break the string into list of words
	str = str.split()		
	str2 = []

	# loop till string values present in list str
	for i in str:			

		# checking for the duplicacy
		if i not in str2:

			# insert value in str2
			str2.append(i)
			
	for i in range(0, len(str2)):

		# count the frequency of each word(present
		# in str2) in str and print
		print('Frequency of', str2[i], 'is :', str.count(str2[i]))	

def main():
	str ='apple mango apple orange orange apple guava mango mango'
	freq(str)					

if __name__=="__main__":
	main()			 # call main function



#9 RGB to Hex conversion and vice versa, e.g. (255,0,255) into 0xFF00FF

def RGB_TO_HEX(r, g, b):
    return("#{:02x}{:02x}{:02x}".format(r, g, b))


#Generate accumulated strings,e.g. abcd ==> A-Bb-Ccc-Dddd

n = 4
a = 67
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("%c" % (a))
    a += 1
    print("-")