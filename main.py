from pysnap import *
import sys
import datetime

s = Snapchat()

s.login(sys.argv[1], sys.argv[2])

# Get list of friends
friends = s.get_friends()

# Get friends' usernames
friends = [friend['name'] for friend in friends]

# Get best friends of these friends
bests = s.get_other_best_friends(friends)

# If file already exists
try:
	f = open('scores.csv', 'r')
	# Get headers
	content = f.read()
	line = content.split('\n')[0]
	f.close()
	friends = line.split(',')
except:
	f = open('scores.csv', 'w')
	f.write('date\n')
	content = 'date\n'
	f.close()
	# Of course, this means you can't have a friend named 'date'.
	# But I don't, so it's okay.
	friends = ['date']

scores = {}
for username, attrs in bests.iteritems():
	scores[username] = attrs['score']
	if username not in friends:
		friends.append(username)

line = datetime.datetime.now().strftime('%c') + ','
for friend in friends[1:]:
	# Just in case you got unfriended
	# Probably for being creepy and graphing people's snapchat scores
	# But whatever
	line += str(scores[friend]) if friend in scores else ''
	line += ','

# Replace first line with new friends list
content = '\n'.join([','.join(friends)] + (content.split('\n')[1:]))

# Add new data
content += '\n'
content += line

f = open('scores.csv', 'w')
f.write(content)
f.close()
