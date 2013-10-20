''' 
Working -- Stand alone program meant to be a function when complete
A specific object to gather BSSID sources and targets from files, perhaps also to gather output from simple commands
'''

import sys, fileinput, re

filename = 'test-01.csv'                               #later change this to 'flagsCaptured-01.csv'
regex = re.compile(r'\b..:..:..:..:..:..\b')           #Regex for BSSID
patte = re.compile(r'.......$')                        #Regex for ESSID
line_number = 0                                        #Might be useful later
interesting_BSSID = []
potential_ESSID = []
targets = []
'''
this whole function should probably be rewritten as it uses a find and replace construct, just need some test output
'''
'''
for target_BSSID in fileinput.input([filename], inplace = True):
    target_BSSID = target_BSSID.replace(x,y)                      where x and y are string variables, pretty sure i need to use a seperate function to specify string type though
    # sys.stdout is redirected to file
    sys.stdout.write(target_BSSID)
'''

with open(filename) as targets_file:           #targets_file = open(filename, encoding = locale)
    #now it's simply a function with temp. vars
    for targets_line in targets_file:          #each line in file is now included as a variable string in targets_line
        #target_BSSID = [string for string in targets_line if re.match(regex, string)]             #this assumes a list rather than substrings
        result = regex.findall(targets_line)
        another = patte.search(targets_line)

        '''                                                              This block of code only retrieves the first match and excludes the rest
        matchobj = regex.search(targets_line)
        if matchobj:
          result = matchobj.group()
        else:
          result = ""
        '''

        #print(result)
        if (result != []):
          interesting_BSSID.append(result)                    #creates list of lists
          potential_ESSID.append(another.group())             #creates a list of ESSIDs
          #print(interesting_BSSID, ' ', potential_ESSID)      #remove when complete
        line_number += 1                                      #might be useful later

print(interesting_BSSID)
print(potential_ESSID)
print(len(interesting_BSSID))                                 #remove when complete
lengths = [len(x) for x in interesting_BSSID]                 #gathers the size of each sublist into a new list
print(lengths)                                                #remove when complete

'''
The next part formats the BSSIDs and ESSIDs into a more usable format that will be easier to work with later on.
Perhaps this should be a function that modifys passed in args, or returns a value with the other argument modified.

Need to look at multiple lists with the same BSSID in the second element
'''

'''
This code is such an unelegant pile of shit haha, maybe I'll change it one day!
Loop ftw!
'''

i = 0
while(len(interesting_BSSID[i]) == 1):
  temp = interesting_BSSID[i][0]
  k = 0
  while(lengths[k] == 1):                                                        #Finds where the list lengths = 2
    k += 1
  while(k < len(interesting_BSSID)):
    if(interesting_BSSID[i][0] == interesting_BSSID[k][1]):
      temp += interesting_BSSID[k][0]
    k += 1
  targets.append(temp)
  i += 1

print(targets)                                                                   #Need to fix targets.append() because it's not adding lists, just adding elements into a list

        #target_BSSID = re.search(regex, targets_line)                           #/b is a search boundry
        #print(target_BSSID.group(0))
        #print(targets_line)
        #line_number += 1
        #print('{:>4} {}'.format(line_number, targets_line.rstrip()))   
        #apply formatting of strings then output to file below this
        #figure out what wildcards are in python to search for types of words in strings
