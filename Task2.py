from Main import *
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

def Task2():
    # 1.1
    # option 1:
    #  df1 = pd.read_csv('mobile_price_1.csv')
    # corr = df1.corr()
    # sns.heatmap(corr, cmap='YlGnBu', vmin=-1, vmax=1)
    # plt.show()
    # option 2:
    df1 = pd.read_csv('mobile_price_1.csv')
    X = df1.iloc[:, 0:20]
    y = df1.iloc[:, -1]
    corrmat = df1.corr()
    top_corr_features = corrmat.index
    plt.figure(figsize=(20, 20))
    map = sns.heatmap(df1[top_corr_features].corr(), annot=True, cmap="YlGnBu")
    plt.show()
    # 1.2


    # X = df1.iloc[:, 0:20]
    # y = df1.iloc[:, -1]
    # bestfeatures = SelectKBest(score_func=chi2, k=10)
    # fit = bestfeatures.fit(X, y)
    # dfscores = pd.DataFrame(fit.scores_)
    # dfcolumns = pd.DataFrame(X.columns)
    # featureScores = pd.concat([dfcolumns, dfscores], axis=1)
    # featureScores.columns = ['Specs', 'Score']
    # print(featureScores.nlargest(10, 'Score'))
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