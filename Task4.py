from MobilePriceGeneral import *


class Task4(MobilePriceGeneral):
    def by4grid(self):
        g = sns.PairGrid(self.df, vars=['px_height', 'px_width', 'ram', 'price'], hue='gen', palette='RdBu_r')
        g.map(plt.scatter, alpha=0.8)
        g.add_legend()
        #plt.show()

    def fourD(self):
        coreNumb = [0, 'single', 'dual', 'triple', 'quad', 'penta', 'hexa', 'hepta', 'octa']
        coreNumbc = pd.Categorical(self.df['cores'], ordered=True, categories=coreNumb).codes
        plt.scatter(self.df['px_width'], self.df['px_height'], s=coreNumbc, c=self.df['price'], alpha=0.5)
        plt.colorbar()
        for ar in [1, 4, 8]:
            plt.scatter([], [], c='k', alpha=0.3, s=ar, label=coreNumb[ar])
        plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='core sizes:')
        #plt.show()

    def pricesComp(self):
        tempData = pd.DataFrame(self.df[['ram', 'gen', 'battery_power', 'price']])
        tempData['price_2'] = self.df2['price_2']
        # print(tempData.head())
        sns.heatmap(tempData.corr(), annot=True, cmap="YlGnBu")
        #plt.show()


if __name__ == '__main__':
    task4 = Task4()
    #4.1
    task4.by4grid()
    #4.2
    task4.fourD()
    #4.3
    task4.pricesComp()
