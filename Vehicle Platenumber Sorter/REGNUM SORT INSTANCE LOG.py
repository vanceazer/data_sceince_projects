import requests
import pandas as pd
import csv
import openpyxl

# Define Urls
Instance_log = 'https://etraffica.herokuapp.com/api/instancelogger/paged?pageNumber=1&pageSize=50'
# org = 'https://etraffica.herokuapp.com/api/organisation'
#


# Convert instance log to dataframe
response = requests.get(Instance_log)
# print(response)
json_response = response.json()['data']
df = pd.DataFrame(json_response)
regNumber = df['plateNumber']
print(regNumber)




# define standard regular plate number pattern
standardPattern = ['LLLNNNLL', 'LLLNNLL']
knownPatterns = pd.DataFrame(standardPattern, columns=['patterns'])
confirmedPattern = knownPatterns['patterns']


# function to write identified regular plate number to csv
def writeRegularPlate(items):
    with open('1. RegularPlate.csv', 'a', newline='') as wrt:
        writer = csv.writer(wrt)
        writer.writerow([str(items)])


# function to write identified irregular plate number to csv
def NonRegularPlate(items):
    with open('2. IrregularPlate.csv', 'a', newline='') as wrt:
        writer = csv.writer(wrt)
        writer.writerow([str(items)])

# function to compare established pattern to standard pattern
def comparePattern(patternJoined):
    result = confirmedPattern[confirmedPattern == patternJoined]
    print(result)
    if result.empty == True:
        print(items, 'is not a regular plate number')
        print('Logging plate number', items)
        NonRegularPlate(items)
        print('Logging completed for', items)

    else:
        print('Regular plate number', items, 'identified')
        print('Running regulatory check on', items)
        writeRegularPlate(items)


# function to get the pattern of analyzed platenumber
def patternCheck(items):
    # create an empty list
    patternList = []
    # identify each of the characters in the platenumber string
    for i in items:
        # print(i)
        # if character is alphabet
        if i.isalpha() is True:
            print(i, 'alphabet found, Pattern is L')
            # print('L')
            # add recognized pattern to pattern list
            patternList.append('L')
        else:
            print(i, 'number found, Pattern is N')
            # print('N')
            # add recognized pattern to pattern list
            patternList.append('N')

    # print('This is the pattern')
    print(patternList)
    # join pattern into a single string for easy comparison
    patternJoined = ''.join(patternList)
    print(items, 'pattern is', patternJoined)
    comparePattern(patternJoined)


# function to check if plate ia aplhanumeric
def alphanumCheck(items):
    # check if plate number is alphanumeric
    if items.isalnum() is True:
        print('Alphanumeric found')
    #     find exact pattern and arrangement of characters
        patternCheck(items)

    else:
        print('Plate is not alphanumeric')
        print('Logging plate number', items)
        NonRegularPlate(items)
        print('Logging completed for', items)

# function to analyze length of plate number character
def charLength(items):
    if len(items)>6 and len(items)<9:
        print('Plate Number satisfies length criteria')
        alphanumCheck(items)
    else:
        print('Plate Number doesnt satisfy length criteria')
        print('Logging plate number', items)
        NonRegularPlate(items)
        print('Logging completed for', items)


# loop through the dataframe and analyze the regnumbers
for items in regNumber.values:
    print('--------------------------------------')
    print(items)
    # check for the class of regnumber
    if type(items) is str:
        print('Plate Number is class string, Analysis continues')
    #     check for the length of the platenumber chatacters
        charLength(items)
    #     check for patter conformity


    else:
        print('Plate number is class integer')
        print('Logging plate number', items)
        NonRegularPlate(items)
        print('Logging completed for', items)
    # print(type(items))
