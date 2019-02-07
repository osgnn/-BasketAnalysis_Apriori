#BasketAnalysis_Apriori
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sepet=pd.read_csv("C:\\Users\\ozgun\\Desktop\\Programlar\\Python\\market.csv",header=None) 

t=[]
for i in range (0,9835): 
    t.append([str(sepet.values[i,j]) for j in range (0,32)])


from apyori import apriori
kurallar = list(apriori(t,min_support=0.01, min_confidence=0.3, min_lift = 3, min_length=2))

for item in kurallar:

    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
