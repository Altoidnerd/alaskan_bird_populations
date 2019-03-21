#!/usr/bin/env python3

def filter_dataframe_by_keyword(df, *keywords, cols=['AttrDefinition']):
    """
    filter_by_keyword(pd.dataframe::df, str::*keywords, list::cols=['AttrDefinition']) -> pd.DataFrame
    
    returns the rows for which any of the columns in kwarg 'cols' contain 
    any of the strings in *keywords. exactly match any of the words in *words.
    
    By default, cols='AttrDefinition' so the function will return the rows
    with a match in AttrDefinition only.  You can pass a list of columns instead to match
    over other columns.
    """

    import copy
    import sys
    
    target_dict = dict()
    keeper_idx_set = set()
    
    for column in cols:
        for keyword in keywords:
            
            for idx in range(len(df)):
                #if keyword in str(df.iloc[idx]['AttrDefinition']):
                if keyword in str(df.iloc[idx][column]):
                    keeper_idx_set.add(idx)
            
    keeper_idx_list = list(keeper_idx_set)
    keeper_idx_list.sort()
    #print(keeper_idx_list)
    
    for idx in keeper_idx_list: 
        target_dict[idx] = df.iloc[idx]

#     fdf = pd.DataFrame.from_dict(target_dict,orient='index')
#     return fdf    

    return pd.DataFrame.from_dict(target_dict, orient='index')


def main():
    pass

if __name__=='__main__':
    main()


