import account_details


def test_index_of_ps_no():
    assert account_details.index_of_ps_no(99004407) == 8
    assert account_details.index_of_ps_no(99004408) == 9


def test_school_mark_sheet():
    assert account_details.school_mark_sheet(3) == [93, 90, 98, 97, 93, 96, 92, 97, 97, 97, 90, 90]
    assert account_details.school_mark_sheet(16) == [67, 66, 59, 68, 55, 53, 60, 66, 63, 51, 55, 64]


def test_domain_expertise():
    assert account_details.domain_expertise(7) != ['IoT', 'C Programming', 'Embedded Systems', 'OS']
    assert account_details.domain_expertise(16) == ['C Programming','Digital Circuits and Systems','Computer System Architecture','OS']
    assert account_details.domain_expertise(2) == ['IoT','Digital Circuits and Systems','Microcontrollerd and Microprocessors','Cloud Computing']


def test_hobbies():
    assert account_details.hobbies(13) == ['Singing','Film Making','Watching movies','Reading books','Writing ','Badminton','Gaming']
    assert account_details.hobbies(16) == ['Dancing', 'Blogging', 'Stand-up Comedy', 'Photography', 'Gaming']


def test_cities():
    assert account_details.cities(15) == ['Chennai', 'Delhi', 'Shimla', 'UAE', 'Lucknow']
    assert account_details.cities(5) == ['Manali','Chennai','Bangalore','Delhi','Kolkata', 'Shimla','London','USA']


def test_personal():
    assert account_details.personal(16) ==[['Name','Email address',"Father's Name","Mother's Name",'Mother Tongue','Number of siblings','Date of Birth', 'Native place','Place of Residence'],['Mohamed Saqeeb', 'mohamedsaqeeb14@gmail.com','Adil','NOOR','urdu',3,'16.4.1999',
  'delhi',
  'india']]
    assert account_details.personal(5) != [['Name',
  'Email address',
  "Father's Name",
  "Mother's Name",
  'Mother Tongue',
  'Number of siblings',
  'Date of Birth',
  'Native place',
  'Place of Residence'],
 ['Mohamed Saqeeb',
  'mohamedsaqeeb14@gmail.com',
  'Adil',
  'NOOR',
  'urdu',
  3,
  '16.4.1999',
  'delhi',
  'india']]