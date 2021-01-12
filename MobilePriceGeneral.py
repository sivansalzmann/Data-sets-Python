import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class MobilePriceGeneral:
    def __init__(self):
        self.df = pd.read_csv('Data/mobile_price_1.csv',index_col="id")
        self.df2 = pd.read_csv('Data/mobile_price_2.csv', index_col="id")
        self._pre_process()

    def _pre_process(self):
        self.clean_data()
        self.transform()

    def transform(self):
        self.df.price = self.df.price.astype(int)  # lots of decimals

    def clean_data(self):
        self.df['f_camera'] = self.df['f_camera'].fillna(0)
        self.df['camera'] = self.df['camera'].fillna(0)

        # probably noise, there's no phone with < 100 px
        f = self.df.loc[(self.df.px_height > 100)]

        # probably noise, there's no phone with < 2cm screen width
        df = self.df.loc[(self.df.sc_w > 2)]

    def show_relation_by_price(self, x, y='price'):
        sns.jointplot(x=x, y=y, data=self.df)
        plt.show()

    def price_func(self,_df):
        bat = np.random.normal(1.5,0.5,2000)
        ram = np.random.normal(1.2,0.5,2000)
        gen = np.random.normal(1100,80,2000)

        p = self.df.battery_power*bat + self.df.ram*ram + self.df.gen*gen +np.random.triangular(-200,200,300,2000)
        return np.round(p/10,2)



