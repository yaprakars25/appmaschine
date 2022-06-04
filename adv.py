import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")
def adv_prediction(TV, Radio, Newspaper):
    df = pd.read_csv("/Users/arslan/Desktop/hrk/adv.py")
    #df
    X = df.drop(columns= "sales")
    y = df["sales"]
    model = LinearRegression()
    model.fit(X,y)
    X_test = np.array([TV, Radio, Newspaper])
    X_test = X_test.reshape((1, -1))
    return model.predict(X_test)[0]
# print(adv_prediction(244.1, 15.7, 88))

