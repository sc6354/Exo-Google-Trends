from pytrends.request import TrendReq
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from operator import truediv
import os 
os.chdir("/Users/susanchen/Desktop/ExoGoogleTrends")

from exoGoogletrends import *


def searchListbyRegion(termlist):
    pytrends = TrendReq()
    pytrends.build_payload(termlist,timeframe='2012-04-08 2020-08-17')
    df = pd.DataFrame(pytrends.interest_by_region(inc_low_vol=False))
    return df

def findRegNormFactor(comTermList1, comTermList2):
    normFactor = [ ] 
    for i in range(len(comTermList2)):
        if comTermList2[i] == 0:
            normFactor.append(0)
        else:
            normFactor.append(comTermList1[i]/comTermList2[i])
            
    return normFactor
    #return list(map(truediv, comTermList1, comTermList2))

def combineNormRegList(normList1, normList2):
    l2_3 = pd.concat([normList1, normList2], axis=1)
    l2_3.index = df4.index
    return l2_3

if __name__ =="__main__":
    commonTerm = "Sehun"
    list1 = ["Sehun", "Exo Kris", "Exo Chen", "Exo Suho", "Exo Tao"] 
    list2 =["Sehun", "Exo DO", "Luhan", "Chanyeol", "Exo Kai"]
    list3 = ["Sehun", "Xiumin", "Exo Lay", "Exo Baekhyun"]
    
    df4 = searchListbyRegion(list1)
    df4.to_csv("RegionList1.csv", header = True, index=True)
    df5 = searchListbyRegion(list2)
    df5.to_csv("RegionList2.csv", header = True, index=True)
    df6 = searchListbyRegion(list3)
    df6.to_csv("RegionList3.csv", header = True, index=True)

    commonTermL4 = commonTermInterest(df4, commonTerm)
    commonTermL5 = commonTermInterest(df5, commonTerm)
    commonTermL6 = commonTermInterest(df6, commonTerm)

    normFactor45 = findRegNormFactor(commonTermL4, commonTermL5)
    normFactor46 = findRegNormFactor(commonTermL4, commonTermL6)

    normdf5 = normalisedList(df5, normFactor45, list2)
    normdf6 = normalisedList(df6, normFactor46, list3)

    normdf = combineNormRegList(normdf5 ,normdf6)

    completeRegList = pd.concat([df4, normdf], axis=1)
    completeRegList.to_csv('normalizedByRegion.csv', header= True, index= True)

