from Main import *

def Task5():
    df_1 = pd.read_csv('Data/mobile_price_1.csv',index_col='id')
    df_2 = pd.read_csv('Data/mobile_price_2.csv',index_col='id')
    df_3 = pd.concat([df_1,df_2],axis=1)

    df_3["price_diff"]=df_3.price_2/df_3.price
    plt.scatter(df_3.camera,df_3.price_diff)
    core_ord = pd.Categorical(df_3.cores,ordered=True,categories=['single','dual','triple','quad','penta','hexa','hepta','octa'])
    plt.scatter(df_3.px_width,df_3.px_height,s=df_3.price,c=core_ord.codes)
    plt.show()

if __name__ == '__main__':
    Task5()