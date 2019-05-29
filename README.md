# Enzyme_filter.py 
Re site finder is an online tool (http://resitefinder.appspot.com/) designed to help users create novel restriction sites in coding sequences without perturbing the corresponding amino acids. Given a coding sequence, re site finder uncovers all possible locations in which the user can introduce a silent mutation that generates a restriction enzyme recognition sequence. 

If a plasmid sequence is given, re site finder will only search for and display silent mutations in the coding sequence that result in unique restriction sites; otherwise, re site finder will find and display all possible silent mutations in the coding sequence that result in recognition sequences. 

However, as all posibilities are taken into account, the results files tend to be long, which could hinder our search. This script filters the .csv result file generated by re site finder to easiy find what we are looking for. The script will discard all restriction sites that are not plaindromic sequences by default. Apart from that, the user can also filter the results to search for a specific enzyme and/or in a specific region of the input sequence.

To run the program:
> python enzyme_filter.py <file_name> <enzyme_name> <initial_position> <final_position>
