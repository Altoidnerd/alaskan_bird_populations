#!/usr/bin/env python3
import pandas as pd
import time
import datetime

def filter_by_keyword_csv(input_csv, *keywords, cols=['AttrDefinition'], verbose=False, outfile=None):
    """
    
    #################### WARNING: SLOWWWWWWWW CODE ################################
    # Set verbose=True for status updates because this function is not optimized  #
    ###############################################################################
    
    
    
    filter_by_keyword_csv(plaintext csv::input_csv, str::*keywords, list::cols=['AttrDefinition'], verbose=False, outfile=None) -> pd.DataFrame
    
    Saves a csv containing the rows for which any of the columns in kwarg 'cols' contain 
    any of the strings in *keywords. exactly match any of the words in *words.
    
    By default, cols='AttrDefinition' so the function will return the rows
    with a match in AttrDefinition only.  You can pass a list of columns instead to match
    over other columns.
    
    Set verbose=True for status updates because this function is SLOOOOOWWWWWW.
    
    """

    
    df = pd.read_csv(input_csv)
    
    start = time.time()
    
    # this dict will become the output dataframe
    target_dict = dict()
    # set of indices to "keep"
    keeper_idx_set = set()
    
    if verbose:
        print("Begin filter function call {}\n".format(datetime.datetime.now().ctime()))
        print("Function has been passed {} keywords and {} columns:".format(len(keywords), len(cols)))
        print("The keywords are: {}".format(keywords))
        print("The columns are: {}\n".format(cols))
        print("This function is not optimized.  Expect delays.\n")
    
    for column in cols:
        
        for keyword in keywords:
            
            if verbose:
                now = time.time()
                elapsed = now - start
                print("working on col {}, keyword \"{}\"]\t".format(column, keyword) +"Elapsed time: {} seconds".format(elapsed))
                
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


    if verbose:
        end = time.time()
        elapsed = end - start
        print("\nElapsed time: {} seconds".format(elapsed))
        print("End filter function call {}".format(datetime.datetime.now().ctime()))
        
    outputdf = pd.DataFrame.from_dict(target_dict, orient='index')

    
    if outfile == None:
        print("Warning: No output file specified.")
        outfile = input_csv+'.out'
        print("saving to {}".format(outfile))
        
        outputdf.to_csv(input_csv+'.out')
    
    else:
        if verbose:
            print("saving to {}".format(outfile))
        outputdf.to_csv(outfile)


def main():
    keywords = ['timestamp', 'Element']
    filter_by_keyword_csv('variables_with_full_attribute_name.csv', *keywords, cols=['EntityName', 'AttrDefinition'],verbose=True, outfile='a.out.csv')


if __name__=='__main__':
    main()


