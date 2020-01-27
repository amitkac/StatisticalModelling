"""
    Author: Amit Kachroo
    --Class for csv reading
    email : amitkac@gmail.com
"""
import pandas as pd
import numpy as np


class fileRead():

    def __init__(self, fin, colNum, skRow):
        self.fin = fin
        self.colNum = colNum
        self.skRow = skRow
        # self.csvRead()

    @classmethod
    def csvRead(cls, self):
        print('1. reading "{}"------------------------'.format(self.fin))
        df = pd.read_csv(self.fin, names=['data'], skiprows=self.skRow,
                         usecols=[self.colNum], header=0,
                         dtype=np.float32)
        df = df.dropna()
        # print(df.head())
        self.df = df
