from Main import *

def price_func(df):
    bat = np.random.normal(1.5,0.5,2000)
    #resolution = np.random.normal(0.0006,0.0002,2000)
    ram = np.random.normal(1.2,0.5,2000)
    gen = np.random.normal(1100,80,2000)

    # p = df.battery_power*bat + df.resolution*resolution + df.ram*ram + df.gen*gen +np.random.triangular(-200,200,300,2000)
    p = df.battery_power*bat  + df.ram*ram + df.gen*gen +np.random.triangular(-200,200,300,2000)

    return np.round(p/10,2)


def Task2():
    corr = df.corr()
    plt.figure(figsize = (8,6))
    sns.heatmap(corr)
    #plt.show()

    df['price'] = price_func(df)
    corr_new = df.corr()
    plt.figure(figsize = (8,6))
    sns.heatmap(corr_new)
    plt.show()

if __name__ == '__main__':
    Task2()