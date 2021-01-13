from MobilePriceGeneral import *


def calculate_ordinal_features(df):
    core_list = ['single', 'dual', 'triple', 'quad', 'penta', 'hexa', 'hepta', 'octa']
    df['cores_ord'] = pd.Categorical(df.cores, ordered=True, categories=core_list).codes + 1
    speed_list = ['low', 'medium', 'high']
    df['speed_ord'] = pd.Categorical(df.speed, ordered=True, categories=speed_list).codes + 1
    wifi_list = ['none', 'n', 'g', 'b', 'a']
    df['wifi_ord'] = pd.Categorical(df.wifi, ordered=True, categories=wifi_list).codes + 1
    gen_list = ['2', '3', '4']
    df['gen_ord'] = pd.Categorical(df.gen, ordered=True, categories=gen_list).codes + 1

def calculate_nominal_features(df):
    sim_list = ['Dual','Single']
    df['sim_bin'] = pd.Categorical(df.sim, ordered=True, categories=sim_list).codes
    bluetooth_list = ['No', 'Yes']
    df['bluetooth_bin'] = pd.Categorical(df.bluetooth, ordered=True, categories=bluetooth_list).codes
    screen_list = ['LCD', 'Touch']
    df['screen_bin'] = pd.Categorical(df.screen, ordered=True, categories=screen_list).codes

def show_heatmap(df):
    corr_new = df.corr()
    plt.figure(figsize = (8,6))
    sns.heatmap(corr_new)
    # plt.show()


if __name__ == '__main__':
    df = pd.read_csv('Output\mobile_price_1_1.csv',index_col="id")
    #3.1
    calculate_ordinal_features(df)
    #3.2
    calculate_nominal_features(df)
    #3.3
    show_heatmap(df)
    #3.4
    # df.to_csv('mobile_prices_1_converted.csv')