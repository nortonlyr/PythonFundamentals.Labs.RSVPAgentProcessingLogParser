import re


file_name = './data/rsvp_agent_log.dat'
file = open(file_name, 'r')
lines = file.readlines()

print('WARNING: ')
for line in lines:
    if re.search('WARNING', line):
        print((line[0:14] + " --" + re.split(":", line)[4]).strip())