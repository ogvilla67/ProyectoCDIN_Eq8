# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:34:22 2020

@author: oscar
"""

class mylib:
    
    def dqr(data):
        import pandas as pd
        
        columns = pd.DataFrame(list(data.columns.values),columns=['Nombres'],index=list(data.columns.values))
    
        data_types = pd.DataFrame(data.dtypes,columns=['Data_Types'])
    
        missing_values = pd.DataFrame(data.isnull().sum(),columns=['Missing_Values'])
    
        present_values = pd.DataFrame(data.count(),columns=['Present_Values'])
    
        unique_values = pd.DataFrame(columns=['Unique_Values'])
        for col in list(data.columns.values):
            unique_values.loc[col] = [data[col].nunique()]
        
        min_values = pd.DataFrame(columns=['Min'])
        for col in list(data.columns.values):
            try:
                min_values.loc[col] = [data[col].min()]
            except:
                pass
        
        max_values = pd.DataFrame(columns=['Max'])
        for col in list(data.columns.values):
            try:
                max_values.loc[col] = [data[col].max()]
            except:
                pass
    
        return columns.join(data_types).join(missing_values).join(present_values).join(unique_values).join(min_values).join(max_values)
