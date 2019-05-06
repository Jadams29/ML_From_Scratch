from matplotlib import pyplot as plt
from matplotlib import lines as mlines
import numpy as np
import math

def least_squares(y, y_pred):
    ## Sumation((y - y_pred)^2)
    return


class LinearRegression:
    def __init__(self, data):
        self.Data = data
        self.yIntercept = None
        self.slope = None
        self.sumOfSquaresRegression = None      # The sum of the squares due to regression
        self.sumOfSquaresError = None
        self.sumOfSquaresTotal = None
        self.xMean = None
        self.yMean = None
        self.centroid = None

    def get_sumOfSquaresTotal(self):
        if self.SST is None:
            self.set_SST()
        return self.SST

    def set_sumOfSquaresTotal(self):
        # Baseline for SSR and SSE to compare
        if self.Data is None:
            print("We do not have any data to work with")
            return
        if self.yMean is None:
            self.set_yMean()
        self.sumOfSquaresTotal = np.sum(np.square(self.Data[1] - self.yMean))
        return

    def get_sumOfSquaresError(self):
        if self.sumOfSquaresError is None:
            self.set_sumOfSquaresError()
        return self.sumOfSquaresError

    def set_sumOfSquaresError(self):
        if self.Data is None:
            print("We do not have any data to work with")
            return
        yValueVectorized = np.vectorize(self.get_yValue)
        predictedY = yValueVectorized(self.Data[0])     # Sending each X value into get_yValue function
        self.sumOfSquaresError = np.sum(np.square(self.Data[1] - predictedY))
        print()

    def get_sumOfSquaresRegression(self):
        if self.sumOfSquaresRegression is None:
            self.set_sumOfSquaresRegression()

    def set_sumOfSquaresRegression(self):
        if self.Data is None:
            print("We do not have any data to work with")
            return
        if self.sumOfSquaresTotal is None:
            self.set_sumOfSquaresTotal()
        if self.sumOfSquaresError is None:
            self.set_sumOfSquaresError()
        self.sumOfSquaresRegression = self.sumOfSquaresTotal - self.sumOfSquaresError
        return

    def get_yValue(self, tempX):
        if self.slope is None:
            self.set_slope()
        if self.yIntercept is None:
            self.set_yIntercept()
        y = (self.slope * tempX) + self.yIntercept
        return y

    def get_centroid(self):
        if self.centroid is None:
            print("The centroid has not been established.")
            return
        return self.centroid

    def set_centroid(self):
        if self.xMean is None:
            self.set_xMean()
        if self.yMean is None:
            self.set_yMean()
        self.centroid = [self.get_xMean(), self.get_yMean()]

    def get_slope(self):
        if self.slope is None:
            self.set_slope()
        return self.slope

    def set_slope(self):
        if self.Data is None:
            print("The data is empty.")
            return
        if self.centroid is None:
            self.set_centroid()
        # Subtract xMean from each X data point
        tempX = self.Data[0] - self.centroid[0]

        # Subtract yMean from each Y data point
        tempY = self.Data[1] - self.centroid[1]

        # Multiple tempX by tempY then add up the vector
        numerator = np.sum(tempX * tempY)

        # Essentially take tempX and square all the values then add up the vector
        denominator = np.sum(np.square(tempX))

        self.slope = numerator/denominator
        return

    def get_data(self):
        if self.Data is None:
            print("The data has not been generated.")
            return
        return self.Data

    def set_data(self, data):
        self.Data = data
        return

    def get_yIntercept(self):
        if self.yIntercept is None:
            print("The value of the Y-Intercept is currently not calculated. Please set the Y-Intercept")
            return
        return self.yIntercept

    def set_yIntercept(self):
        # self.yMean - slope * xMean
        if self.centroid is None:
            self.set_centroid()
        if self.slope is None:
            self.set_slope()
        self.yIntercept = self.centroid[1] - (self.slope * self.centroid[0])
        return

    def get_xMean(self):
        if self.xMean is None:
            print("The mean of X has not been calculated. Please set the mean for X")
            return
        return self.xMean

    def set_xMean(self):
        try:
            self.xMean = np.mean(self.Data[0])
        except Exception as err:
            print("An error occurred when attempting to calculate the mean of X. ", err)
        return

    def get_yMean(self):
        if self.yMean is None:
            print("The mean of Y has not been calculated. Please set the mean for Y")
            return
        return self.yMean

    def set_yMean(self):
        try:
            self.yMean = np.mean(self.Data[1])
        except Exception as err:
            print("An error occurred when attempting to calculate the mean of Y. ", err)
        return

    def graph_data(self, withRegressionLine):
        plt.figure()
        plt.scatter(self.Data[0], self.Data[1])
        if withRegressionLine:
            if self.Data is None:
                print("The data has not been set")
                return
            if self.yIntercept is None:
                self.set_yIntercept()
            if self.slope is None:
                self.set_slope()

            x1 = np.min(self.Data[0])
            x2 = np.max(self.Data[0])
            y1 = (self.slope * x1) - self.yIntercept
            y2 = (self.slope * x2) - self.yIntercept
            plt.plot([x1, x2], [y1, y2], color='r')
            plt.show()
        return
