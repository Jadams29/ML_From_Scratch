## Algorithms

* [Linear Regression](https://github.com/Jadams29/ML_From_Scratch/tree/master/Linear_Regression)


#### Least Squares

<img src="img/Least_Square_Formula.png" width="320" height="80">

For every data point you take the known y value and subtract the predicted y value then square the result.
We then add up all of the results and try to minimize this summation.

```python
# Not actual code
min(sumation([(actual_y - predicted_y)^2]))
```

#### Deviation

```python
# Not actual code
x_deviation = (x - x_mean)
y_deviation = (y - y_mean)
```

#### Deviation Product

```python
# Not actual code
(x_deviation)(y_deviation)
```

#### Expanded Slope

<img src="img/Expanded_Slope_Formula.png" width="320" height="80">

<img src="img/Expanded_Slope_Formula_Explained.png" width="320" height="120">

```python
# Not actual code
# Slope expanded out
b_1 = (sumation(x-x_mean)(y-y_mean))/(sumation((x-x_mean)^2))

# Exactly the same as
b_1 = (sumation(Deviation Product)/sumation(x_deviation^2))
```

#### Y Intercept

<img src="img/Y_Intercept.png" width="260" height="80">

```python
b_0 = y_mean - (b_1 * x_mean)
```



[![Licensed under the MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Microsoft/BosqueLanguage/blob/master/LICENSE.txt)
[![PR's Welcome](https://img.shields.io/badge/PRs%20-welcome-brightgreen.svg)](#contribute)
