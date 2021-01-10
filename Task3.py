from Main import *

def conv_gen(x):
    converter = {4:0,0:2,3:3,7:4}
    return converter[x]

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

def conv_wifi(x):
    if x == 'none':
        return 0
    else:
        return 1

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
    df['bluetooth_bin']=np.where(df['bluetooth'] =='Yes',1,0)
    df['speed_ord'] = df['speed'].apply(conv_speed)
    df['cores_ord'] = df['cores'].apply(conv_cores)
    df['wifi_bin'] = df['wifi'].apply(conv_wifi)
    df['fourth_gen_bin'] = np.where(df['gen'] == 4 ,1,0)
    df['third_gen_bin'] = np.where(df['gen'] == 3 ,1,0)
    df['sec_gen_bin'] = np.where(df['gen'] == 2 ,1,0)

    # corr2 = df.corr()
    # plt.figure(figsize = (8,6))
    # sns.heatmap(corr2)
    # plt.show()

if __name__ == '__main__':
    Task3()
