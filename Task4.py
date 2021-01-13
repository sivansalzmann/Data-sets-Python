import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def by4grid(df):
    g = sns.PairGrid(df, vars=['price', 'ram', 'DPI_W', 'battery_power'], hue='gen', palette='RdBu_r')
    g.map(plt.scatter, alpha=0.8)
    g.add_legend()
    #plt.show()

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
    #plt.show()

def pricesComp(df,df2):
    df2['price'] = df['price']
    df2['ram'] = df['ram']
    df2['gen'] = df['gen']
    df2['battery_power'] = df['battery_power']
    sns.heatmap(df2[df2.corr().index].corr(), annot=True, cmap='YlGnBu')
    #plt.show()
    x = df2['price_2']
    y = df2['price']
    c = df2['ram']
    plt.scatter(x, y, c=c, alpha=0.3, cmap='YlGnBu')
    plt.colorbar(label='ram')
    plt.xlabel('price_2')
    plt.ylabel('price')
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('Output\mobile_prices_1_converted.csv',index_col="id")
    df2 = pd.read_csv('Data\mobile_price_2.csv',index_col="id")
    #4.1
    by4grid(df)
    #4.2
    fourD(df)
    #4.3
    pricesComp(df,df2)
