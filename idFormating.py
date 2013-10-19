''' A specific object to gather BSSID sources and targets from files, perhaps also to gather output from simple commands '''

import sys, fileinput

filename = 'test-01.csv'   # later change this to 'flagsCaptured-01.csv'
target_BSSID = '0'
source_BSSID = '0'
deauth_BSSID = '0'

'''
this whole function should probably be rewritten as it uses a find and replace construct, just need some test output
'''
'''
for target_BSSID in fileinput.input([filename], inplace = True):
    target_BSSID = target_BSSID.replace(x,y)                      where x and y are string variables, pretty sure i need to use a seperate function to specify string type though
    # sys.stdout is redirected to file
    sys.stdout.write(target_BSSID)
'''
line_number = 0

with open(filename) as targets_file:           #targets_file = open(filename, encoding = locale)
    #now it's simply a function with temp. vars
    for targets_line in targets_file:          #each line in file is now included as a variable string in targets_line
        print(targets_line)
        line_number += 1
        #print('{:>4} {}'.format(line_number, targets_line.rstrip()))   
        #apply formatting of strings then output to file below this
        #figure out what wildcards are in python to search for types of words in strings
