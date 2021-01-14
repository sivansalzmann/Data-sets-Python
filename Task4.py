import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def by4grid(df):
    g = sns.PairGrid(df, vars=['price', 'camera', 'DPI_W', 'battery_power'], hue='gen', palette='RdBu_r')
    g.map(plt.scatter, alpha=0.8)
    g.add_legend()
    # plt.show()

def fourD(df):
    coreNumb = [0, 'single', 'dual', 'triple', 'quad', 'penta', 'hexa', 'hepta', 'octa']
    coreNumbc = pd.Categorical(df['cores'], ordered=True, categories=coreNumb).codes
    plt.scatter(df['px_width'], df['px_height'], s=(coreNumbc+1)*10, c=df['price'], alpha=0.5,cmap='BrBG_r')
    plt.colorbar(label='price')
    plt.xlabel('px_width')
    plt.ylabel('px_height')
    core_names = {10: 'single', 20: 'dual', 30: 'triple', 40: 'quad', 50: 'penta', 60: 'hexa', 70: 'hepta', 80: 'octa'}
    for ar in [10, 20, 30, 40, 50, 60, 70, 80]:
        plt.scatter([], [], c='k', alpha=0.3, s=ar, label=core_names[ar])
    plt.legend(scatterpoints=1, frameon=False, labelspacing=1)
    # plt.show()

def show_correlation_heatmap(df):
    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    f, ax = plt.subplots(figsize=(20, 10))
    ax.set_title("Correlation Heatmap")
    cmap = sns.diverging_palette(200, 10, as_cmap=True)
    sns.heatmap(corr, annot=True,mask=mask, cmap=cmap)
    # plt.show()

def pricesComp(df1,df2):
    df3 = pd.concat([df1,df2],axis=1)
    df3["price_diff"]=df3.price_2/df3.price
    plt.scatter(df3.camera,df3.price_diff,vmin=0)
    plt.xlabel("Entreies")
    plt.ylabel("price relation")
    plt.colorbar(label='camera')
    # plt.show()

    x = df2['price_2']
    y = df1['price']
    c = df1['camera']
    plt.scatter(x, y, c=c, alpha=0.3, cmap='YlGnBu')
    plt.colorbar(label='camera')
    plt.xlabel('price_2')
    plt.ylabel('price')
    # plt.show()

    df1 = pd.merge(df1, df2, on='id', how='left')
    df1['price_rate'] = np.round(df1['price_2'] / df1['price'], 2)
    show_correlation_heatmap(df1)
    sns.jointplot(x='camera', y='price_rate', data=df1)

if __name__ == '__main__':
    df = pd.read_csv('Output\mobile_prices_1_converted.csv',index_col="id")
    df2 = pd.read_csv('Data\mobile_price_2.csv',index_col="id")
    #4.1
    by4grid(df)
    #4.2
    fourD(df)
    #4.3
    pricesComp(df,df2)