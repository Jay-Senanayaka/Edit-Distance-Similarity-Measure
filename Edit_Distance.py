#Author: Sanjeewa Senanayaka
#Edit-Distance
#Similarity measure

import pandas as pd

#read in two tables and the corresponding columns to compare
df1 = pd.read_csv("all_gamestop.csv", error_bad_lines=False)
saved_column1 = df1.title

df2 = pd.read_csv("ebay_data.csv" , error_bad_lines=False)
saved_column2 = df2.name

#edit distance algorithm
def editDistance( string1, string2):

    #length of the words to compare
    length1 = len(string1)
    length2 = len(string2)


    if length1 == 0:
        return length2;

    if length2 == 0:
        return length1;

    #Create an empty 2D array
    table = [[0 for i in range(length1+1)] for j in range(length2+1)]

    #Set the first row incrementing from 0 to length of string
    for i in range(0,length1+1):
        table[0][i] = i

    #Set the first column incrementing from 0 to length of string
    for i in range(0, length2+1):
        table[i][0] = i

    for i in range (1, length1+1):
        for j in range( 1, length2+1):
            if(string1[i-1] == string2[j-1]):
                table[j][i] = table[j-1][i-1]

            else:
                table[j][i] = min(table[j - 1][i], table[j][i - 1], table[j - 1][i - 1])+1

    #print("OUTPUT")
    return table[length2][length1]


#if the similarity between the two strings are greater than 0.75 return true
def similarityMeasure(string1, string2):
    similarity = 1-(editDistance(string1, string2)/ max(len(string1), len(string2)))
    if similarity > 0.75:
        return True
    else :
        return False


#compare each item in a column with every other to check for similarity
#if they have a good similarity measure, use them to block them together
for i in range (0, len(saved_column1)):
    for j in range (0, len(saved_column2)):
        if(similarityMeasure(saved_column1[i].lower(), saved_column2[j].lower())) == True:
            print("Block together")
            print( saved_column1)
            print(saved_column2)
        else:
            print("Do not block together")