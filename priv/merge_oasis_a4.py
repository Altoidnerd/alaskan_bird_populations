#!/usr/bin/env python3

def merge_like_oasis_variables(oasis_csv='oasis_variables.csv', origin_csv='variables_with_full_attribute_name.csv', outfile=None):
    """
merge_like_oasis_variables(oasis_csv, origin_csv) -> csv

Take two csvs as arguments and prints all rows from osasis_csv
which have the same name as a variable in origin_csv.
 
    """

    origin_lines = open(origin_csv, 'r').readlines()
    oasis_lines = open(oasis_csv,'r').readlines()

    output = []

    for origin_line in origin_lines:

        output.append(origin_line)
        this_var = origin_line.split(',')[3].lower()

#    oasis_matches = [ line for line in oasis_lines if line.split()[3].lower() == origin_line.split()[3].lower() ] 

    for line in oasis_lines:
        if line.split(',')[3] == this_var:
            output.append(line)

    if outfile == 'stdout':
        for line in output:
            sys.stdout.write(line)

    elif outfile != 'None':
        print('Warning: no output file specified; writing to a.out.csv')
        f = open('a.out.csv','w')
        for line in output:
            f.wirte(line)
        f.close()

    else:
        f = open('a.out.csv','w')
        for line in output:
             f.wirte(line)
        f.close()


        
        

def main():
    merge_like_oasis_variables()

if __name__ == '__main__':
    main()

     
