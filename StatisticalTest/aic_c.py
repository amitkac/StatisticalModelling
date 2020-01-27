"""
    Name: Amit Kachroo
    ----- class for AIC test
    email : amitkac@gmail.com
"""
import pandas as pd
from scipy.stats import exponweib
import numpy as np
from scipy.stats import (gamma, rayleigh, norm,  nakagami, expon,
                         lognorm)


class aic2():

    def __init__(self, data):
        self.data = data
        # self.fitDist()

    def fitDist(self):

        n = len(self.data)

        # gamma distribution
        gammaParam = gamma.fit(self.data)
        gammaNumPar = len(gammaParam)
        gammaSum = -1*np.sum(np.log(gamma.pdf(self.data, *gammaParam)))
        aicGamma = 2*gammaNumPar+2*gammaSum + (2*gammaNumPar*(gammaNumPar+1)
                                               / (n-gammaNumPar-1))

        # rayleigh distribution
        rayleighParam = rayleigh.fit(self.data)
        rayleighNumPar = len(rayleighParam)
        rayleighSum = -1*np.sum(np.log(rayleigh.pdf(self.data,
                                                    *rayleighParam)))
        aicRayleigh = 2*rayleighNumPar+2*rayleighSum+(2*rayleighNumPar
                                                      * (rayleighNumPar+1) /
                                                      (n-rayleighNumPar-1))

        # normal distribution
        normParam = norm.fit(self.data)
        normNumPar = len(normParam)
        normSum = -1*np.sum(np.log(norm.pdf(self.data, *normParam)))
        aicNorm = 2*normNumPar+2*normSum+(2*normNumPar*(normNumPar+1)
                                          / (n-normNumPar-1))

        # LogNormal distribution
        logNormParam = lognorm.fit(self.data)
        logNormNumPar = len(logNormParam)
        logNormSum = -1*np.sum(np.log(lognorm.pdf(self.data, *logNormParam)))
        aicLogNorm = 2*logNormNumPar+2*logNormSum+(2*logNormNumPar *
                                                   (logNormNumPar+1)
                                                   / (n-logNormNumPar-1))

        # Nakagami distribution
        nakagamiParam = nakagami.fit(self.data)
        nakagamiNumPar = len(nakagamiParam)
        nakagamiSum = -1*np.sum(np.log(nakagami.pdf(self.data,
                                                    *nakagamiParam)))
        aicNakagami = 2*nakagamiNumPar+2*nakagamiSum+(2*nakagamiNumPar *
                                                      (nakagamiNumPar+1)
                                                      / (n-nakagamiNumPar-1))

        # exponential distribution
        exponParam = expon.fit(self.data)
        exponNumPar = len(exponParam)
        exponSum = -1*np.sum(np.log(expon.pdf(self.data, *exponParam)))
        aicExpon = 2*exponNumPar+2*exponSum + (2*exponNumPar *
                                               (exponNumPar+1)
                                               / (n-exponNumPar-1))

        # weibul distribution
        exponweibParam = exponweib.fit(self.data)
        exponweibNumPar = len(exponweibParam)
        exponweibSum = -1*np.sum(np.log(exponweib.pdf(self.data,
                                                      *exponweibParam)))
        aicExpWeib = 2*exponweibNumPar+2*exponweibSum+(2*exponweibNumPar *
                                                       (exponweibNumPar+1)
                                                       / (n-exponweibNumPar-1))

        return (aicGamma, aicRayleigh, aicNorm, aicLogNorm, aicNakagami,
                aicExpon, aicExpWeib)

    @classmethod
    def returnDistData(cls, self):
        gammaParam = gamma.fit(10**(self.data/10))
        gammaDist = gamma.pdf(self.data, *gammaParam)

        rayleighParam = rayleigh.fit(self.data)
        rayleighDist = rayleigh.pdf(self.data, *rayleighParam)

        normParam = norm.fit(self.data)
        normDist = norm.pdf(self.data, *normParam)

        logNormParam = lognorm.fit(self.data)
        lognormDist = lognorm.pdf(self.data, *logNormParam)

        nakagamiParam = nakagami.fit(self.data)
        nakagamiDist = nakagami.pdf(self.data, *nakagamiParam)

        exponParam = expon.fit(self.data)
        exponDist = expon.pdf(self.data, *exponParam)

        exponweibParam = exponweib.fit(self.data)
        weibDist = exponweib.pdf(self.data, *exponweibParam)

        distDF = pd.DataFrame(np.column_stack([gammaDist, rayleighDist,
                                               normDist, lognormDist,
                                               nakagamiDist, exponDist,
                                               weibDist]),
                              columns=['gammaDist', 'rayleighDist',
                                       'normDist', 'lognormDist',
                                       'nakagamiDist', 'exponDist',
                                       'weibDist'])
        self.distDF = distDF

    def getDistGamma(self):
        gammaParam = gamma.fit(self.data)
        gammaDist = gamma.pdf(self.data, *gammaParam)
        return gammaDist

    def getDistNorm(self):
        normParam = norm.fit(self.data)
        normDist = norm.pdf(self.data, *normParam)
        return normDist

        # , aicExpWeib)
