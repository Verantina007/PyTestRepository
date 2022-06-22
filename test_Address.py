import pyodbc

'connect to database as administrator'
connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=EPBYMINW0E8A\SQLEXPRESS;Database=AdventureWorks2017;Trusted_Connection=yes;')

'Test-cases for table [Person].[Address]'
'1.1. Number of rows in the table'

'Function count_number_rows() for counting the number of rows in the table'
def count_number_rows():
    cursor = connection_to_db.cursor()
    cursor.execute('SELECT COUNT ([AddressID]) AS num FROM [AdventureWorks2017].[Person].[Address]')
    row = cursor.fetchone().num
    return(row)

'Test-case 1.1:'
def test_equals():
    print("The result of test-case 1.1. is")
    assert count_number_rows() == 19614, "The number of rows in the table [Address] does not correspond the expected result"

'1.2. Foreign key [FK_Address_StateProvince_StateProvinceID] check'
'Function foreign_keys_check() for counting the number of values in column [StateProvinceID] which do not exist in the table [StateProvince]'
def foreign_keys_check():
    cursor = connection_to_db.cursor()
    cursor.execute('SELECT COUNT(pa.[StateProvinceID]) AS num FROM [Person].[Address] pa WHERE NOT EXISTS (SELECT ps.[StateProvinceID] FROM [Person].[StateProvince] ps)')
    row = cursor.fetchone().num
    return(row)

'Test-case 1.2:'
def test_foreign_keys_check():
    print("The result of test-case 1.2. is")
    assert foreign_keys_check() == 0, "There are rows with values which do not exist in the table [StateProvince]"

'--------------------------------------------------------------------------------------------------------------------'
'Test-cases for table [Production].[Document]'
'2.1. Constraint [CK_Document_Status] check'

'Function count_number_correct_statuses() for counting the number of rows with wrong satatuses in column [Status]'
def count_number_correct_statuses():
    cursor = connection_to_db.cursor()
    cursor.execute('SELECT COUNT ([Status]) AS num FROM [Production].[Document] WHERE [Status]>=1 OR [Status]<=3')
    row = cursor.fetchone().num
    return(row)

'Test-case 2.1:'
def test_correct_statuses():
    print("The result of test-case 2.1. is")
    assert count_number_correct_statuses() == 13, "The are incorrect statuses in the table"

'2.2. Data type of the column [FolderFlag] check'
'Function count_not_bool_values() for counting the number of non-boolen values in the column'
def count_not_bool_values():
    cursor = connection_to_db.cursor()
    cursor.execute('SELECT COUNT([FolderFlag]) AS num FROM [Production].[Document] WHERE [FolderFlag] != \'False\' AND  [FolderFlag] != \'True\' ')
    row = cursor.fetchone().num
    return(row)

'Test-case 2.2:'
def test_bool_values():
    print("The result of test-case 2.2. is")
    assert count_not_bool_values() == 0, "There are non-boolen values in the column [FolderFlag]"

'----------------------------------------------------------------------------------------------------------------------'
'Test-cases for table [Production].[UnitMeasure]'
'3.1. Data accuracy in column [ModifiedDate] check'

'Function count_wrong_dates() for counting the number of rows with wrong dates'
def count_wrong_dates():
    cursor = connection_to_db.cursor()
    cursor.execute('SELECT COUNT ([ModifiedDate]) AS num FROM [Production].[UnitMeasure] WHERE [ModifiedDate] > getdate()')
    row = cursor.fetchone().num
    return(row)

'Test-case 3.1:'
def test_dates_correctness():
    print("The result of test-case 3.1. is")
    assert count_wrong_dates() == 0, "The are rows with incorrect dates in the table"

'3.2. Length of char column check'
'Function count_length() for counting the number of rows with length less then 3 or equal 3'
def count_length():
    cursor = connection_to_db.cursor()
    cursor.execute('SELECT COUNT(*) AS num FROM [Production].[UnitMeasure] WHERE LEN ([UnitMeasureCode])<=3')
    row = cursor.fetchone().num
    return(row)

'Test-case 3.2:'
def test_char_length():
    print("The result of test-case 3.2. is")
    assert count_length() == 38, "There are rows with length more then 3"


