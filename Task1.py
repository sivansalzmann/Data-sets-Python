import pandas as pd
import matplotlib.pyplot as plt

def transform(df):
    df.price = df.price.astype(int)  # lots of decimals

def clean_data(df):
    df['f_camera'] = df['f_camera'].fillna(0)
    df['camera'] = df['camera'].fillna(0)
    # probably noise, there's no phone with < 100 px
    f = df.loc[(df.px_height > 100)]
    # probably noise, there's no phone with < 2cm screen width
    df = df.loc[(df.sc_w > 2)]

def pre_process(df):
    clean_data(df)
    transform(df)

def addCoulnms(df):
    #1.3
    df['resolution'] = df.px_height * df.px_width
    #1.4
    df['DPI_W'] = (df['px_width']/df['sc_w']) / 2.54
    #1.5
    df['call_ratio'] = df['battery_power'] / df['talk_time']
    #1.6
    df['memory'] /= 1024

def describe(df):
    pd.set_option('max_columns',None)
    print(f"describe():\n{df.describe()}")

def histMap(df):
    df.hist(column='price')
    plt.xlabel("Count")
    plt.ylabel("Price")
    #plt.show()

if __name__ == '__main__':
    df = pd.read_csv("Data\mobile_price_1.csv", index_col="id")
    pre_process(df)
    #1.3 - 1.6
    addCoulnms(df)
    #1.7
    describe(df)
    #1.8
    histMap(df)

    df.to_csv("mobile_price_1_1.csv")

