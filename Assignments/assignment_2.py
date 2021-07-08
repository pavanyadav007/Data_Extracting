import math


# In a given list of elements, all elements are equal except the one. Write a code to find the odd man out (Stray number

def strayNumber_odd_out(elements):
    tempr_v = [i for i in elements if elements.count(i) == 1]
    return(tempr_v[0])

# In a given list of elements, find the elements which is close to its mean
def Mean_of_elements(elements):
    tempr_v = sum(elements) / len(elements)
    for i in elements:
        if i == int(tempr_v):
            return(i)
        else:
            pass
    print('none')


#Find the average speed of vehicle, given the distance travelled for fixed time intervals, e.g. [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]
def calculation_avg(distance, time):
    speed = 0
    for i in time:
        if i != 0:
            speed = speed + (distance // i)
    return(speed // len(time))

#* Find the no.of people in a bus, given the data of people onboarding & alighting at each station

def pepole_onBoard_total(station_, onboard, alighting):

    tempr_v = 0
    for i in range(station_):
        tempr_v = tempr_v + onboard[i] - alighting[i]
    return(tempr_v)



#* Find the missing number, given the original list and modified one
def Finding_missed_one(list1, list2):
    for i in list2:
        if i not in list1:
            return(i)
            break

#* Find the difference between two lowest numbers in the list
def difference_bt_Low(items):
    items.sort()
    return(items[1] - items[0])


#In a given list, count no.of elements smaller than their mean

def find_mean_lower(elem):
    mean = sum(elem) / len(elem)
    c = 0
    for i in elem:
        if i < mean:
            c = c + 1
    return(c)