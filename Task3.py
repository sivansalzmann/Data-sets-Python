from Main import *

def conv_speed(x):
    if x == 'low':
        return 0
    if x == 'medium':
        return 1
    if x == 'high':
        return 2

def conv_cores(x):
    converter = {'single':1,'dual':2,'triple':3,'quad':4,'penta':5,'hexa':6,'hepta':7,'octa':8}
    return converter[x]


def conv_price(x):
    if x > 15:
        return 1 if np.random.random() > 0.4 else 0
    return 0

def conv_cam_price(x):
    if x > 15:
        return 1.1 if np.random.random() > 0.4 else 0.95
    return 0.95

def conv_range(x):
    if x < 697:
        return 0
    elif x < 839:
        return 1
    elif x < 1010:
        return 2
    else:
        return 3

def Task3():
    df_out = df.copy()

    #3.1
    df_out['speed_ord'] = df['speed'].apply(conv_speed)
    df_out['cores_ord'] = df['cores'].apply(conv_cores)
    df_out['fourth_gen_ord'] = np.where(df['gen'] == 4 ,1,0)
    df_out['third_gen_ord'] = np.where(df['gen'] == 3 ,1,0)
    df_out['sec_gen_ord'] = np.where(df['gen'] == 2 ,1,0)

    #3.2
    df_out['bluetooth_bin']=np.where(df['bluetooth'] =='Yes',1,0)
    df_out['wifi_bin'] = np.where(df['wifi'] == 'none' ,0,1)
    df_out['sim_dual_bin'] = np.where(df['sim'] =='Dual',1,0)
    df_out['screen_touch_bin'] = np.where(df['screen'] == 'Touch',1,0)

    #3.3
    corr_new = df_out.corr()
    plt.figure(figsize = (8,6))
    sns.heatmap(corr_new)
    #plt.show()

    #3.4
    df_out.to_csv('mobile_prices_converted.csv')

if __name__ == '__main__':
    Task3()
