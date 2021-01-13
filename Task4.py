from MobilePriceGeneral import *

def by4grid(df):
    g = sns.PairGrid(df, vars=['px_height', 'px_width', 'ram', 'price'], hue='gen', palette='RdBu_r')
    g.map(plt.scatter, alpha=0.8)
    g.add_legend()
    # plt.show()

def fourD(df):
    coreNumb = [0, 'single', 'dual', 'triple', 'quad', 'penta', 'hexa', 'hepta', 'octa']
    coreNumbc = pd.Categorical(df['cores'], ordered=True, categories=coreNumb).codes
    plt.scatter(df['px_width'], df['px_height'], s=coreNumbc, c=df['price'], alpha=0.5)
    plt.colorbar()
    for ar in [1, 4, 8]:
        plt.scatter([], [], c='k', alpha=0.3, s=ar, label=coreNumb[ar])
    plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='core sizes:')
    # plt.show()

def pricesComp(df,df2):
    tempData = pd.DataFrame(df[['ram', 'gen', 'battery_power', 'price']])
    tempData['price_2'] = df2['price_2']
    # print(tempData.head())
    sns.heatmap(tempData.corr(), annot=True, cmap="YlGnBu")
    # plt.show()


if __name__ == '__main__':
    df = pd.read_csv('Output\mobile_prices_1_converted.csv',index_col="id")
    df2 = pd.read_csv('Data\mobile_price_2.csv',index_col="id")
    #4.1
    by4grid(df)
    #4.2
    fourD(df)
    #4.3
    pricesComp(df,df2)
