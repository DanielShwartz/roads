import pandas as pd
from geopy.distance import geodesic
import scipy.spatial.distance

import numpy as np
import datetime
import statsmodels.api as sm
import sklearn.model_selection
from scipy import stats

import scipy.sparse as sp

import statsmodels.formula.api as smf
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

FILENAME = "excels\\Raw_Data.xlsx"
SHEET_NAME = "org_data"
LOG_PATH = 'excels\logs\\'


def create_distance_matrix(data, name):
    dat = data[['google lat','google lnt']]
    f = lambda u, v: geodesic(u, v).km
    Y = scipy.spatial.distance.cdist(dat, dat, f)
    Y=pd.DataFrame(Y)
    dat=pd.concat([data,Y],axis=1)
    dat.to_excel(LOG_PATH+"name.xlsx")
    # np.savetxt(LOG_PATH+name, Y, delimiter=",")
    #should i use google distance matrix too?


if __name__ == "__main__":
    data = pd.read_excel(FILENAME, sheet_name=SHEET_NAME)
    create_distance_matrix(data, "distances.csv")
