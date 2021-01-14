import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def show_relation_by_price(df, x, y='price'):
    sns.jointplot(x=x, y=y, data=df)
    # plt.show()

def show_correlation_heatmap(df):
    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    f, ax = plt.subplots(figsize=(20, 10))
    ax.set_title("Correlation Heatmap")
    cmap = sns.diverging_palette(200, 10, as_cmap=True)
    sns.heatmap(corr, annot=True,mask=mask, cmap=cmap, center=0, square=True, linewidths=.5)
    plt.show()

def show_correlated_with_price_catagories(df):
    features = {'bluetooth': [0,1], 'cores': [6,0,7,5,4,2,1,3], 'speed': [1,2,0], 'sim':[0,1], 'wifi':[4,1,0,2,3]}
    price = df['price']

    for feat, pos in features.items():
        temp = df[feat].astype('category')
        temp.cat.categories = pos
        temp = temp.astype('float')
        print("correlation of {} feature: {}".format(feat,price.corr(temp)))

def show_pivot_table(df):
    ram = pd.cut(df['ram'], [0,1000,2000,3000,4000])
    battery = pd.cut(df['battery_power'],[500,1000,1500,2000])
    pivot_table = df.pivot_table('price', [ram,battery], 'gen')
    print(df.pivot_table('price', [ram,battery], 'gen'))

if __name__ == '__main__':
    df = pd.read_csv('Output\mobile_price_1_1.csv',index_col="id")
    #2.1
    show_correlation_heatmap(df)
    #2.3
    show_correlated_with_price_catagories(df)
    #2.4
    show_relation_by_price(df,x='ram')
    show_relation_by_price(df,x='gen')
    show_relation_by_price(df,x='battery_power')
    #2.5
    show_pivot_table(df)