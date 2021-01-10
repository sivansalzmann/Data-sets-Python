from Main import *

def Task1():
    #1.2
    print(f"Numinal categorical features => {df.columns[10]} | {df.columns[14]} | {df.columns[18]} | {df.columns[19]}")
    print(f"Ordinal categorical features => {df.columns[11]} | {df.columns[12]} | {df.columns[13]}")
    #1.3
    df['resolution'] = df.px_height * df.px_width
    #1.4
    df['DPI_W'] = df['px_width']/df['sc_w']*2.5
    #1.5
    df['call_ratio'] = df['battery_power'] / df['talk_time']
    #1.6
    df['memory'] /= 1024
    #1.7
    df.describe()
    print(f"describe():\n{df.describe()}")
    #1.8
    df.hist(column='price')
    plt.xlabel("Count")
    plt.ylabel("Price")
    plt.show()

if __name__ == '__main__':
    Task1()
