from MobilePriceGeneral import *

class Task1(MobilePriceGeneral):

    def addCoulnms(self):
        #1.3
        self.df['resolution'] = self.df.px_height * self.df.px_width

        #1.4
        self.df['DPI_W'] = (self.df['px_width']/self.df['sc_w']) / 2.54

        #1.5
        self.df['call_ratio'] = self.df['battery_power'] / self.df['talk_time']

        #1.6
        self.df['memory'] /= 1024

    def describe(self):
        # self.df.describe().to_csv("Task_1.7_describe.csv")
        print(f"describe():\n{self.df.describe()}")

    def histMap(self):
        self.df.hist(column='price')
        plt.xlabel("Count")
        plt.ylabel("Price")
        #plt.show()

if __name__ == '__main__':
    task1 = Task1()
    #1.3 - 1.6
    task1.addCoulnms()
    #1.7
    task1.describe()
    #1.8
    task1.histMap()

    # task1.df.to_csv("Task_1.3_1.4_1.5_1.6.csv")

