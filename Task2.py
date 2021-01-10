from Main import *

def Task2():
    #2.1
    corr = df.corr()
    plt.figure(figsize = (8,6))
    sns.heatmap(corr,cmap='YlGnBu')
    plt.show() #add categorial features? remove id

    #2.2
    print(f"Features correlated with the device price shown in the matrix : {df.columns[1]} , {df.columns[4]} , {df.columns[5]} , {df.columns[6]} , {df.columns[11]} ")

    #2.3
    print(f"Features correlated with the device price not shown in the matrix : ") #fix here

    #2.4
    sns.jointplot(x='ram', y='price', data=df)
    #plt.show()
    sns.jointplot(x='gen', y='price', data=df)
    #plt.show()
    sns.jointplot(x='battery_power', y='price', data=df)
    #plt.show()
    sns.jointplot(x='px_height', y='price', data=df)
    #plt.show()
    sns.jointplot(x='px_width', y='price', data=df)
    #plt.show()

    #2.5
    index_list = ['ram', 'battery_power']
    df_tmp = df.copy()
    for index in index_list:
        df_tmp[index] = pd.qcut(df_tmp[index], 5)
    pivot_table = np.round(pd.pivot_table(df_tmp, values='price', index=index_list,columns='gen', aggfunc=np.mean), 1)
    #print(pivot_table)
    pivot_table.to_csv('Task_2.5_pivot_table.csv')

if __name__ == '__main__':
    Task2()