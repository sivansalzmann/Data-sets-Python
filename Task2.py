from Main import *

def Task2():
    # 1.1
    df1 = pd.read_csv('mobile_price_1.csv')
    corr = df1.corr()
    sns.heatmap(corr, cmap='YlGnBu', vmin=-1, vmax=1)
    plt.show()

    # 1.2
# ______________________________
# data = np.genfromtxt("mobile_price_1.csv", delimiter=",",skip_header=True, usecols=range(1, 11))
# plt.imshow(data, cmap='hot', interpolation='nearest')
# plt.show()
# ________________________________
# df1 = pd.read_csv('mobile_price_1.csv')
# corr = df1.corr()
# ax = sns.heatmap(
#     corr,
#     vmin=-1, vmax=1, center=0,
#     cmap=sns.diverging_palette(20, 220, n=200),
#     square=True
# )
# ax.set_xticklabels(
#     ax.get_xticklabels(),
#     rotation=45,
#     horizontalalignment='right'
# )
# plt.imshow(ax)
# plt.show()

# ______________________________________________
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.heatmap(df1.corr(), center=0, cmap='Blues')
# ax.set_title('heatmap')

if __name__ == '__main__':
    Task2()