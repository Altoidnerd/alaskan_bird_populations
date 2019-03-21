#!/usr/bin/env python3
import pandas as pd
import os


print("cur dir:\t", os.getcwd())

readiness_dfs = pd.read_excel('Target_Readiness_Definition.xlsx', sheet_name = [0,1,2,3] )
# loads the readiness targets as a list of dictionaries; d[0,1,2,3]->P,S,R,T
training_df = readiness_dfs[3]


catalog_dfs = pd.read_excel('AFDS_Catalog_transvoyant_C3IoT.xlsx', sheet_name=[0,1])
attribute_catalog, entity_catalog = catalog_dfs[0], catalog_dfs[1]



####################################################
#
#. Correct column names in attr, entity dfs
#
#
# Rename entity catalog columns
#
#####################################################
oldcols = list(entity_catalog.columns)
newcols = list(entity_catalog.iloc[0])

colsDict = dict()

for i, col in enumerate(oldcols):
    colsDict[col] = newcols[i]
    
entity_catalog = entity_catalog.rename(columns=colsDict)
    
####################################################
#
# Rename attribute catalog columns
#
#####################################################    

    
oldcols = list(attribute_catalog.columns)
newcols = list(attribute_catalog.iloc[0])

colsDict = dict()

for i, col in enumerate(oldcols):
    colsDict[col] = newcols[i]
    
attribute_catalog = attribute_catalog.rename(columns=colsDict)
    
# entity_catalog.to_csv('a4_entity_catalog.csv')
# attribute_catalog.to_csv('a4_attribute_catalog.csv')

def main():
    
    edf = entity_catalog
    adf = attribute_catalog

    print("\n"+'#'*80+'\n'+' '*20+'Driving Factors'+'\n'+'#'*80)
    for i in range(len(training_df)):
        print(training_df.driving_factor[i].split())
 

    print("\n"+'#'*80+'\n'+' '*20+'Entity Defs'+'\n'+'#'*80)
    for i in range(50): 
        try:
            print(edf.Definition[i].split())
        except AttributeError:
            pass

    print("\n"+'#'*80+'\n'+' '*20+'Attribute Defs'+'\n'+'#'*80)
    for i in range(50): 
        try:
            print(adf.AttrDefinition[i].split())
        except AttributeError:
            pass

if __name__ == '__main__':
    main()
    
