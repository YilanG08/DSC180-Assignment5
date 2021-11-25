import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# drop the last-two-day data
one_day = 60*24
def clean_data(df,rows):
    clean = df.iloc[:rows-2*one_day,]
    return clean


# combine the 3 4-day repeated cycles
def find_cycle(cleaned):
    df = pd.DataFrame()
    for i in range(0,17280, 5760):
        df = pd.concat([df,cleaned.iloc[i:i+5760,].reset_index().
                        drop(['index'],axis =1)],axis = 1,ignore_index=True)
    return df

def graph_CBT_LA(total,rows):
    title = ["Female CBT", "Female LA", "Male CBT", "Male LA"]
    plt.figure(figsize=(12,8))
    for i,data in enumerate(total):
        ax = plt.subplot(2,2,i+1)
        plt.title(title[i])
        cleaned = clean_data(data,rows)
        total[i] = find_cycle(cleaned)
        plt.plot(total[i].mean(axis=1))
    plt.show(block=True)
    return 



