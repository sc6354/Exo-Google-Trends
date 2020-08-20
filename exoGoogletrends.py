from pytrends.request import TrendReq
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from operator import truediv
import os 
os.chdir("/Users/susanchen/Desktop/ExoGoogleTrends")



def searchList(termlist):
    pytrends = TrendReq()
    pytrends.build_payload(termlist,timeframe='2012-04-08 2020-08-17')
    df=pytrends.interest_over_time()
    df = df.drop('isPartial', axis = 1)
    return df

def commonTermInterest(dataframe, commonTerm):
    commonTermList = dataframe[commonTerm].tolist()
    return commonTermList

def findNormalizationFactor(comTermList1, comTermList2):
    return list(map(truediv, comTermList1, comTermList2))

def normalisedList(dataframe, normFactorList, keytermlist):
    othersList = dataframe.values.tolist()

    for i in range(len(othersList)):
        #othersList[i].pop()
        othersList[i].pop(0)

    #normalizationFactorList = findNormalizationFactor(list1, list2)

    for i in range(len(othersList)):
        for j in range(len(othersList[i])):
            othersList[i][j]= round(othersList[i][j]*normFactorList[i], 2)

    listdf = pd.DataFrame (othersList,columns= keytermlist[1:] )
    return listdf 

def combineNormalizedList(normList1, normList2):
    l2_3 = pd.concat([normList1, normList2], axis=1)
    l2_3.index = pd.date_range(start='05/01/2012', periods=100, freq='MS')
    return l2_3

def combineDF(datafile1,datafile2):
    ot12 = pd.concat([datafile1, datafile2], axis=1)
    os.chdir("/Users/susanchen/Desktop/ExoGoogleTrends")
    ot12.to_csv('normalizedExo.csv', header= True, index= True)


if __name__ == "__main__":
    commonTerm= "Sehun"
    list1 = ["Sehun", "Exo Kris", "Exo Chen", "Exo Suho", "Exo Tao"] 
    list2 =["Sehun", "Exo DO", "Luhan", "Chanyeol", "Exo Kai"]
    list3 = ["Sehun", "Xiumin", "Exo Lay", "Exo Baekhyun"]

    df1 = searchList(list1)
    df1.to_csv("exoSKList1.csv", header = True, index=True)
    df2 = searchList(list2)
    df2.to_csv("exoSKList2.csv", header = True, index=True)
    df3 = searchList(list3)
    df3.to_csv("exoSKList3.csv", header = True, index=True)

    commonTermL1 = commonTermInterest(df1, commonTerm)
    commonTermL2 = commonTermInterest(df2, commonTerm)
    commonTermL3 = commonTermInterest(df3, commonTerm)

    normFactor12 = findNormalizationFactor(commonTermL1, commonTermL2)
    normFactor13 = findNormalizationFactor(commonTermL1, commonTermL3)

    normdf2 = normalisedList(df2, normFactor12, list2)
    normdf3 = normalisedList(df3, normFactor13, list3)

    normdf = combineNormalizedList(normdf2 ,normdf3)

    completeList = combineDF(df1, normdf)

    
