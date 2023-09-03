import pandas as pd
import csv



# import data and convert to dataframe
path = 'C:/Users/sirmi/Documents/Pycharm/Chithub Pycharm/eTraffika Pycharm/regNmber code sorting/1. RegularPlate.csv'
df = pd.read_csv(path)
regnumber = df['Plate']
# print(regnumber.values)


# define standard regular plate number pattern
standardPattern = ['LLLNNNLL', 'LLLNNLL']
knownPatterns = pd.DataFrame(standardPattern, columns=['patterns'])
confirmedPattern = knownPatterns['patterns']

confirmedList = []










# function to check if plate ia aplhanumeric
def alphanumCheck(items):
    # check if plate number is alphanumeric
    if items.isalnum() is True:
        print('Alphanumeric found')
    #     find exact pattern and arrangement of characters
        patternCheck(items)

    else:
        print('Plate is not alphanumeric')



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

# function to compare established pattern to standard pattern
def comparePattern(patternJoined):
    result = confirmedPattern[confirmedPattern == patternJoined]
    print(result)
    if result.empty == True:
        print(items, 'is not a regular plate number')


    else:
        print('Regular plate number', items, 'identified')
        confirmedList.append(items)


# calculate the percentage of accuracy



for items in regnumber.values:
    print(items)
#     check patter of Plate
    patternCheck(items)



totalCount = len(regnumber)
verifiedCount = len(confirmedList)
p = (verifiedCount/totalCount) * 100
percentage = str(p) + '%'


# print(confirmedList)
print('--------------------------------')
print('--------------------------------')
print('--------------------------------')
print('Analysis Result')
print('The total Plate Number analyzed is', totalCount)
print('and the count of verified platenumber is,', verifiedCount)
print('The accuracy is', verifiedCount, 'out of', totalCount)
print('The percentage accuracy is', percentage)



