#!/usr/bin/env python3
import pandas as pd
import time
import datetime
import numpy as np
import sys
import os

def filter_by_keyword_csv(input_csv, *keywords, cols=['AttrDefinition'], verbose=False, outfile=None):

    """
    ################################################################
    #
    # Set verbose=True for status updates if runtime is long
    #
    ################################################################

   

    filter_by_keyword_csv(plaintext csv::input_csv, str::*keywords, list::cols=['AttrDefinition'], verbose=False, outfile=None) -> pd.DataFrame

    Saves a csv containing the rows for which any of the columns in kwarg 'cols' contain
    any of the strings in *keywords. exactly match any of the words in *words.

    By default, cols='AttrDefinition' so the function will return the rows
    with a match in AttrDefinition only.  You can pass a list of columns instead to match
    over other columns.
    
    OPTIONS:
        Print to standout output by setting outfile='stdout'.
            useage:  ./filter_by_keywords3.py $( cat keywords.txt) > example.out 
    
        Set verbose=True for status updates if runtime is long.

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
                print("Working on col {}, idx={}\t\t\tElapsed time: {:.4f} seconds".format(column, idx, elapsed))
                
            descriptors +=  str(df.iloc[idx][column]).lower().replace('.',' ').replace(',',' ').replace("_", ' ')
            descriptor_set = set(descriptors.split())

        matches = descriptor_set.intersection(keyword_set)
        
    

        if len(matches) != 0:
            keeper_idx_set.add(idx)
            matches_output_column.append(str(list(matches)).replace('[','').replace(']',''))

  
# these should be the same ...
#    print(len(df))
 #   print(len(matches_output_column))
    
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
    
    
    if outfile == None:
        print("Warning: No output file specified.")
        outfile = input_csv+'.out'
        print("saving to {}".format(outfile))

        outputdf.to_csv(input_csv+'.out')


    elif outfile == 'stdout':
        outputdf.to_csv('.tmpfile')
        for line in open('.tmpfile').readlines():
            sys.stdout.write(line)
        os.remove('.tmpfile')

        
    
    else:
        if verbose:
            print("saving to {}".format(outfile))
        outputdf.to_csv(outfile)


def main():

    if len(sys.argv) > 1:
        keywords = sys.argv
    else:
        print("Using default keyswords: ['timestamp', 'Element','aircraft','missile']")
        keywords = ['timestamp', 'Element','aircraft','missile']

    filter_by_keyword_csv('variables_with_full_attribute_name.csv', *keywords, cols=['EntityName', 'AttrDefinition'],verbose=True, outfile='stdout')


if __name__=='__main__':
    main()


