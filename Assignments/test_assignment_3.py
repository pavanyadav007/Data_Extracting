from assignment_3 import * 
#1 Correct the malformed time string , for e.g "5:70:65" to "6:11:05"\
def Time_changes_check():
    assert Time_changes_check("5:70:65") == "6:11:5"
    assert Time_changes_check("3:11:90") == "3:12:30"



# 2 Correct the malformed date string , for e.g. "45/8/2018" to "14/9/2018"

def DATE_checking_excess():
    assert DATE_checking_excess("45/8/2018") == "14/9/2018"
    assert DATE_checking_excess("123/11/2019") == "3/3/2020"
    assert  DATE_checking_excess("1199/11/2000") == "29/2/2004"


# 4 Check whether given string is isogram or not

def test_solve1():
    assert solve("education") == True
def test_solve2():
    assert solve("process") == True


#5 Given a string, find the mexican wave

def test_MEX_wave_generation():
    assert MEX_wave_generation('love') == ['Love', 'lOve', 'loVe', 'lovE']
    assert MEX_wave_generation('pavanyadav') == ['Pavanyadav', 'pAvAnyAdAv', 'paVanyadaV', 'pAvAnyAdAv', 'pavaNyadav', 'pavanYadav', 'pAvAnyAdAv', 'pavanyaDav', 'pAvAnyAdAv', 'paVanyadaV']


#6. Given a number, find the largest number by deleting single digit (order of digits will remain same)

def test_maxnumber1():
    assert maxnumber(6358,1) == 635
def test_maxnumber2():
    assert maxnumber(4321,1) == 432


#8. Given a number, find the largest number by shuffling the digits

def test_printMaximum():
    assert printMaximum(38293367) == 98763332

 # 9 RGB to Hex conversion and vice versa, e.g. (255,0,255) into 0xFF00FF
def RGB_TO_HEX():
    assert RGB_TO_HEX(24, 245, 95) == '#18f55f'
    assert RGB_TO_HEX(254, 245, 95) == '#fef55f'