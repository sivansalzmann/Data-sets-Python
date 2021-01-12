from MobilePriceGeneral import *



class Task2(MobilePriceGeneral):

    def show_correlation_heatmap(self):
        corr = self.df.corr()
        mask = np.triu(np.ones_like(corr, dtype=bool))
        f, ax = plt.subplots(figsize=(8, 6))
        ax.set_title("Correlation Heatmap")
        cmap = sns.diverging_palette(200, 10, as_cmap=True)
        sns.heatmap(corr, mask=mask, cmap=cmap, center=0, square=True, linewidths=.5)
        # plt.show()

    def show_correlated_with_price(self): #add describe
            print(f"Features correlated with the device price shown in the matrix : ram, gen, battery_power ")

    def show_correlated_with_price_catagories(self):
        features = {'bluetooth': [0,1], 'cores': [6,0,7,5,4,2,1,3], 'speed': [1,2,0], 'sim':[0,1], 'wifi':[4,1,0,2,3]}
        price = self.df['price']

        for feat, pos in features.items():
            temp = self.df[feat].astype('category')
            temp.cat.categories = pos
            temp = temp.astype('float')
            print("correlation of {} feature: {}".format(feat,price.corr(temp)))


    def show_pivot_table(self):
        ram = pd.cut(self.df['ram'], [0,1000,2000,3000,4000])
        battery = pd.cut(self.df['battery_power'],[500,1000,1500,2000])
        pivot_table = self.df.pivot_table('price', [ram,battery], 'gen')
        print(self.df.pivot_table('price', [ram,battery], 'gen'))
        # pivot_table.to_csv('Task_2.5_pivot_table.csv')

if __name__ == '__main__':
    task2 = Task2()
    #2.1
    task2.show_correlation_heatmap()
    #2.2
    task2.show_correlated_with_price()
    #2.3
    task2.show_correlated_with_price_catagories()
    #2.4
    task2.show_relation_by_price(x='ram')
    task2.show_relation_by_price(x='gen')
    task2.show_relation_by_price(x='battery_power')
    #2.5
    task2.show_pivot_table()