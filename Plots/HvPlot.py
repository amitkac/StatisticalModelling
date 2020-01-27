"""
    Name: Amit Kachroo
    --- holoview plotting class for the data
    email : amitkac@gmail.com
"""

import holoviews as hv
import hvplot.pandas


class plots():

    def __init__(self, distDF, aicData):
        self.distDF = distDF
        self.aicData = aicData
        self.plotData()

    def plotData(self):
        scatterDataPlot = hv.Scatter(self.distDF[['data']],
                                     label='Scatter plot')
        scatterDataPlot.opts(align='center', height=300, width=450,
                             xrotation=45, fontsize={'title': 16,
                                                     'labels': 14,
                                                     'xticks': 12,
                                                     'yticks': 12})

        distPlot = hv.Distribution(self.distDF[['data']], label='Distribution')
        distPlot.opts(align='center', height=300, width=450,
                      xrotation=45, fontsize={'title': 16,
                                              'labels': 14,
                                              'xticks': 12,
                                              'yticks': 12})

        d = ['Gamma', 'Rayleigh', 'Normal', 'Lognormal', 'Nakagami',
             'Exponential', 'Weibull']
        points = [(d[i], self.aicData[i]) for i in range(7)]

        aicPlot = hv.Points(points, ['distribution', 'score'], label='AIC_c')
        aicPlot.opts(tools=['hover'], color='blue',
                     marker='o', size=10, show_grid=False, line_width=2,
                     align='center', height=300, width=450,
                     xrotation=45, fontsize={'title': 16,
                                             'labels': 14,
                                             'xticks': 12,
                                             'yticks': 12})

        gammaPlot = hv.Points(self.distDF[['data', 'gammaDist']],
                              label='Gamma distribution')
        gammaPlot.opts(align='center', height=300, width=450,
                       xrotation=45, fontsize={'title': 16,
                                               'labels': 14,
                                               'xticks': 12,
                                               'yticks': 12})

        rayelighPlot = hv.Points(self.distDF[['data', 'rayleighDist']],
                                 label='Rayleigh distribution')
        rayelighPlot.opts(align='center', height=300, width=450,
                          xrotation=45, fontsize={'title': 16,
                                                  'labels': 14,
                                                  'xticks': 12,
                                                  'yticks': 12})

        normPlot = hv.Points(self.distDF[['data', 'normDist']],
                             label='Normal distribution')
        normPlot.opts(align='center', height=300, width=450,
                      xrotation=45, fontsize={'title': 16,
                                              'labels': 14,
                                              'xticks': 12,
                                              'yticks': 12})

        lognormPlot = hv.Points(self.distDF[['data', 'lognormDist']],
                                label='Lognormal distribution')
        lognormPlot.opts(align='center', height=300, width=450,
                         xrotation=45, fontsize={'title': 16,
                                                 'labels': 14,
                                                 'xticks': 12,
                                                 'yticks': 12})

        nakagamiPlot = hv.Points(self.distDF[['data', 'nakagamiDist']],
                                 label='Nakagami distribution')
        nakagamiPlot.opts(align='center', height=300, width=450,
                          xrotation=45, fontsize={'title': 16,
                                                  'labels': 14,
                                                  'xticks': 12,
                                                  'yticks': 12})

        exponPlot = hv.Points(self.distDF[['data', 'exponDist']],
                              label='Exponential distribution')
        exponPlot.opts(align='center', height=300, width=450,
                       xrotation=45, fontsize={'title': 16,
                                               'labels': 14,
                                               'xticks': 12,
                                               'yticks': 12})

        weibPlot = hv.Points(self.distDF[['data', 'weibDist']],
                             label='Weibull distribution')
        weibPlot.opts(align='center', height=300, width=450,
                      xrotation=45, fontsize={'title': 16,
                                              'labels': 14,
                                              'xticks': 12,
                                              'yticks': 12})

        layout = hv.Layout(aicPlot + scatterDataPlot + distPlot + exponPlot
                           + rayelighPlot + normPlot + lognormPlot
                           + weibPlot + gammaPlot + nakagamiPlot).cols(3)
        hvplot.show(layout)
