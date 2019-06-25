from __future__ import division, print_function
import sys


def palindrome (seq):
    """Define what a palindromic sequence is
    """
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    complement_seq = ''.join([complement[base] for base in seq[::-1]])
    return seq == complement_seq


def re_position (re_site_file=None, enzyme_name=None, initial_position=0, final_position=1000000):
    """Filter the results of a .csv file
    """
    if re_site_file is None:
        print("ENTER at least THE FILE NAME")
        sys.exit()
    re_site = open(re_site_file)
    for line in re_site:
        line = line.strip() # Get rid of starting and trailing whitespace
        if not line or line.startswith("#"):
            continue
        info = line.split(",")
        num_changes = info[0]
        position = int(info[1])
        enzyme = info[2]
        initial_seq = info[3]
        new_seq = info[4]
        site_len = len(initial_seq)
        if enzyme_name in (None, enzyme, "all") and palindrome(new_seq) and initial_position <= (position) <= final_position:
            print("The enzyme", enzyme, "cuts", new_seq, "at position", position,
                  "by introducing", num_changes, "silent mutation(s) in the original sequence", initial_seq)


##Enter the filters from the comand line
if __name__ == '__main__':
    # Map command line arguments to function arguments
    if len(sys.argv) >= 4:
        sys.argv[3] = int(sys.argv[3])
        if len(sys.argv) >= 5:
            sys.argv[4] = int(sys.argv[4])
        re_position(*sys.argv[1:])
