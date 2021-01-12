from MobilePriceGeneral import *

class Task3(MobilePriceGeneral):
    def calculate_ordinal_features(self):
        core_list = ['single', 'dual', 'triple', 'quad', 'penta', 'hexa', 'hepta', 'octa']
        self.df['cores_ord'] = pd.Categorical(self.df.cores, ordered=True, categories=core_list).codes+1
        speed_list = ['low', 'medium', 'high']
        self.df['speed_ord'] = pd.Categorical(self.df.speed, ordered=True, categories=speed_list).codes+1
        wifi_list = ['none', 'n', 'g', 'b', 'a']
        self.df['wifi_ord'] = pd.Categorical(self.df.wifi, ordered=True, categories=wifi_list).codes+1

    def calculate_nominal_features(self):
        self.df['bluetooth_bin']=np.where(self.df['bluetooth'] =='Yes',1,0)
        self.df['sim_dual_bin'] = np.where(self.df['sim'] =='Dual',1,0)
        self.df['screen_bin'] = np.where(self.df['screen'] == 'Touch',1,0)

    def show_heatmap(self):
        corr_new = self.df.corr()
        plt.figure(figsize = (8,6))
        sns.heatmap(corr_new)
        plt.show()


if __name__ == '__main__':
    task3 = Task3()
    #3.1
    task3.calculate_ordinal_features()
    #3.2
    task3.calculate_nominal_features()
    #3.3
    task3.show_heatmap()
    #3.4
    # task3.df.to_csv('mobile_prices_converted.csv')