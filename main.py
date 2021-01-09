import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def Task1():
    df1 = pd.read_csv('mobile_price_1.csv')
    # df2 = pd.read_csv("mobile_price_2.csv")

    df1['screen_resolution'] = np.multiply(df1['px_width'], df1['px_height'])
    df1['DPI_w'] = "" # add the calculate
    df1['call_ratio'] = "" # add the calculate
    df1['memory'] = np.multiply(df1['memory'],0.0009765625)

    #add describe

    # sol = df1.loc([])

    prices = df1['price']
    #describe = df1.describe()
    id = df1['id']
    plt.scatter(id,prices, label="Prices",linewidth=1, alpha=0.5)
    plt.colorbar()
    plt.show()

def Tesk2():
    df1 = pd.read_csv('mobile_price_1.csv')
    phones = sns.load_dataset(df1)
    print(phones.head())





if __name__ == "__main__":
    #Task1()
    Tesk2()