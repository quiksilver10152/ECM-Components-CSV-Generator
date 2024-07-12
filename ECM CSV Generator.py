# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 10:42:06 2024

@author: quiks
"""

# --------------------------------------------------------- Necessary Libraries  ---------------------------------------------------------
import os
import deareis          
import pandas as pd

# --------------------------------------------------------- Change These Variables -------------------------------------------------------------
ECM = 'R(RC)W'
directory = r'C:\Users\quiks\OneDrive\Documents\SEEDS\DATA\WHY'

# --------------------------------------------------------- Plug and Chug -------------------------------------------------------------
paramsECM = ['Experiment']
results = pd.DataFrame([])
for root, dirs, files in os.walk(directory):
    for filename in files:
        temp = [filename]
        data = deareis.parse_data(os.path.join(root, filename))
        settings = deareis.FitSettings(ECM, method = '10', weight = 'AUTO', max_nfev = 10000) 
        fit = deareis.fit_circuit(data[0], settings)
        for d in fit.parameters.keys():
            for e in fit.parameters[d]:
                temp.append(fit.parameters[d][e].value)
                temp.append(fit.parameters[d][e].stderr)
        temp = pd.DataFrame(temp).T
        results = pd.concat([results, temp])
        print((len(results) / len(files)) * 100)
        
for d in fit.parameters.keys():
    paramsECM.append(d)
    paramsECM.append(d + ' Error')
paramsECM[1:3] = ['R_sol', 'R_sol Error']     
results.columns = paramsECM
results.to_csv('out.csv')        
        
       