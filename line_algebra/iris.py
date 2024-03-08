import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import datasets


def plot_iris(iris, col1, col2):
    sns.lmplot(x=col1, y=col2,
               data=iris,
               hue="Species",
               fit_reg=False)

    plt.xlabel(col1)

    plt.ylabel(col2)

    plt.title('Iris species shown by color')

    plt.show()


if __name__ == '__main__':

    iris = datasets.load_iris()

    species = [iris.target_names[x] for x in iris.target]

    iris = pd.DataFrame(iris['data'], columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])

    iris['Species'] = species

    iris['count'] = 1

    result = iris[['Species', 'count']].groupby('Species').count()

    plot_iris(iris, 'Petal_Width', 'Sepal_Length')

    plot_iris(iris, 'Sepal_Width', 'Sepal_Length')
