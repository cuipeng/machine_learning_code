import numpy as np
from sklearn.linear_model import LinearRegression

x = [[1], [2], [3], [4]]
y = [[2], [4], [6], [8]]

model = LinearRegression()
model.fit(x, y)

predicted = model.predict(np.array(5))

print predicted