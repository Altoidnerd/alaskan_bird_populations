#!/usr/bin/env python3
import pandas as pd
import time
import datetime
import numpy as np

def filter_by_keyword_csv(input_csv, *keywords, cols=['AttrDefinition'], verbose=False, outfile=None):
    """

    #################### WARNING: SLOWWWWWWWW CODE ################################
    #
    # Set verbose=True for status updates because this function is not optimized  #
    #
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

        max_num_iters = len(cols)*len(keywords)
        print("For a total of {} iterations.\n".format(max_num_iters))

        print("This function is not optimized.  Expect delays.\n")

 
    keyword_set = set(keywords)
   
    matches_output_column = []

    
    for idx in range(len(df)):

        descriptors = ''
        
        for column in cols:
            
            if verbose and idx%5000==0:
                now = time.time()
                elapsed = now - start
                print("Working on col {}, idx={}\t\tElapsed time: {} seconds".format(column, idx, elapsed))
                
            descriptors +=  str(df.iloc[idx][column]).lower()
            descriptor_set = set(descriptors.split())

        matches = descriptor_set.intersection(keyword_set)
        
    

        if len(matches) != 0:
            keeper_idx_set.add(idx)
            matches_output_column.append(str(list(matches)).replace('[','').replace(']',''))

  

    print(len(df))
    print(len(matches_output_column))
    
    keeper_idx_list = list(keeper_idx_set)
    keeper_idx_list.sort()
#   print(keeper_idx_list)

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
    outputdf['matched by keyword'] = matches_output_column 
    print(matches_output_column[1:20])
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


