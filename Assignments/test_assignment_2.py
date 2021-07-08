from assignment_2 import * 

def strayNumber_odd_out():
    assert strayNumber_odd_out([100,100,100,5]) == 5
    assert strayNumber_odd_out([100,0,0]) == 100
    assert strayNumber_odd_out([1,1,1,1]) == 1
    assert strayNumber_odd_out([23,23,23,23]) == 0
    assert strayNumber_odd_out([1000,1000,1000,1]) == 1


def test_Mean_of_elements():
    assert Mean_of_elements([1,2,3,4]) == 2
    assert Mean_of_elements([12,3,45,7,8]) != 'none'
    assert Mean_of_elements([10,12,13,14]) == 12
    assert Mean_of_elements([66,67,69]) == 67


#Find the average speed of vehicle, given the distance travelled for fixed time intervals, e.g. [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]
def calculation_avg():
    assert calculation_avg(10,[0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0,12]) == 23.0
    assert calculation_avg(100,[19, 13, 123, 5, 0.3, 77, 99, 11]) == 47.0 
    assert calculation_avg(1,[19, 122, 99, 11]) == 0

#* Find the no.of people in a bus, given the data of people onboarding & alighting at each station
def pepole_onBoard_total():
    pepole_onBoard_total(5, [8,6,4,3,1], [2,1,1,1,1]) == 16
    pepole_onBoard_total(4, [0,5,4,3,1], [1,1,1,1,3]) == 8
    pepole_onBoard_total(4, [0,5,8,6,9,1], [1,5,6,6] )== 1


#* Find the missing number, given the original list and modified one
def Finding_missed_one():
    Finding_missed_one([3,5,6,10,12,11], [6,10,2]) == 2
    Finding_missed_one([5,6,8,10,11], [6,7,8,10,11]) == 7
    Finding_missed_one([3,1,10,11], [6,10,12,2])   == 6


#* Find the difference between two lowest numbers in the list

def difference_bt_Low():
    difference_bt_Low([10,50,8,40,2]) == 6
    difference_bt_Low([100,500,877,324,568]) == 224
    difference_bt_Low([999,687,800,394,566]) == 174

#In a given list, count no.of elements smaller than their mean

def find_mean_lower():
    find_mean_lower([1,2,5,4,5,6]) == 2
    find_mean_lower([6,4,5,7,5,8]) == 3
    find_mean_lower([6,4,12,23,8]) == 3