from pysnap import *
import sys
import datetime

s = Snapchat()

s.login(sys.argv[1], sys.argv[2])

# Get list of friends
friends = s.get_friends()

# Get friends' usernames as a string of a list
friends = [friend['name'] for friend in friends]

# Get best friends of these friends
bests = s.get_other_best_friends(friends)

# If file already exists
try:
	f = open('scores.csv', 'r')
	# Get headers
	line = f.readline()
	f.close()
	parts = line.split(',')
	# Get friends and their column index
	friends = {name: index for index, name in enumerate(parts[1:])}
	nextIndex = len(parts)
except:
	f = open('scores.csv', 'w')
	f.write('date,\n')
	f.close()
	friends = {}
	nextIndex = 1

scores = {}
for username, attrs in bests.iteritems():
	scores[username] = attrs['score']

for username, score in scores.iteritems():
	
