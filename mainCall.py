"""
  Author: Amit Kachroo,
  date: 01/23/2020
  email : amitkac@gmail.com
  requires -f <filename with path> -c <column number> -sr <skiprows>
 """


import argparse as ap
from dataPreprocessing import csvDataProcessing as dp
from StatisticalTest import aic_c as aic
from Plots import HvPlot


def main():

    argP = ap.ArgumentParser()
    argP.add_argument('-f', '--file', required='True',
                      help='csv file name with complete path')
    argP.add_argument('-c', '--column', help='column number',
                      default=0, type=int)
    argP.add_argument('-sr', '--skipRows', help='rows to skip',
                      default=1, type=int)
    args = argP.parse_args()
    datax = dp.fileRead(args.file, args.column, args.skipRows)
    dp.fileRead.csvRead(datax)
    # print(data.df.dtype)
    distDataDB = datax.df

    # ---for testing------
    # distDataDB['rvs'] = rayleigh.rvs(3, 2, 4096)

    #  make sure your data is +ve
    aicCall = aic.aic2(distDataDB)
    aicCall.returnDistData(aicCall)
    distDF = aicCall.distDF
    distDF['data'] = distDataDB[['data']]
    # print(distDF.head())

    print('2. fitting various distributions--------------------------')
    aicData = aicCall.fitDist()

    print('3. plotting various distributions-----------------------')

    HvPlot.plots(distDF, aicData)

    print('4. ------done-----------')


if __name__ == "__main__":
    main()
