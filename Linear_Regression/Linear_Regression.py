from matplotlib import pyplot
from LinearRegressionScripts import*
from sklearn.datasets import make_regression  # Used to create a testing regression dataset
from sklearn.datasets.california_housing import fetch_california_housing

import numpy as np

if __name__ == "__main__":
    # Slope-intercept form of a line
    #       y = (mx) + b
    #           x = random variable
    #           m = slope of the line ~ Rise/Run
    #           b = y-intercept
    #           y-intercept is the point at which the line crosses the y axis ~ where x=0
    #
    # Alternate Slope
    #       y = B_0 + (B_1*X)
    #           B_0 = b == y-intercept
    #           B_1 = m == slope of the line ~ Rise/Run

    # test = np.random.standard_normal
    #
    # X, y = make_regression(n_samples=100, n_features=1, noise=20)   # Generate regression dataset
    # X = np.ravel(X)
    # pyplot.scatter(X, y)    # Plot regression dataset
    # pyplot.show()   # Display chart
    # print()

    data = np.array([[34, 108, 64, 88, 99, 51], [5, 17, 11, 8, 14, 5]], np.int32)
    testObject = LinearRegression(data)
    print(testObject.get_yValue(74))
    testObject.graph_data(True)
    testObject.set_yIntercept()
    testObject.set_sumOfSquaresTotal()
    testObject.set_sumOfSquaresError()
    testObject.get_coefficientOfDetermination()
    testObject.get_xStandardDeviation()
    testObject.get_xZScores()
    testObject.get_yZScores()
    testObject.graph_zScores()
    testObject.set_meanSquareError()
    testObject.set_standardError()
    print()
