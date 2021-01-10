from Main import *
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.ensemble import ExtraTreesClassifier
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
    # corrmat = df1.corr()
    # top_corr_features = corrmat.index
    # plt.figure(figsize=(20, 20))
    # map = sns.heatmap(df1[top_corr_features].corr(), annot=True, cmap="YlGnBu")
    # plt.show()
    # 1.2




    model = ExtraTreesClassifier()
    model.fit(X, y)
    print(model.feature_importances_)
    feat_importances = pd.Series(model.feature_importances_, index=X.columns)
    feat_importances.nlargest(10).plot(kind='barh')
    plt.show()


    # bestfeatures = SelectKBest(score_func=chi2, k=10)
    # fit = bestfeatures.fit(X, y)
    # dfscores = pd.DataFrame(fit.scores_)
    # dfcolumns = pd.DataFrame(X.columns)
    # featureScores = pd.concat([dfcolumns, dfscores], axis=1)
    # featureScores.columns = ['Specs', 'Score']
    # print(featureScores.nlargest(10, 'Score'))




if __name__ == '__main__':
    Task2()