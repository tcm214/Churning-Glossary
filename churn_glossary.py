#! python3

#Run: churn [abbr] [definition]*
#enter just an abbr to request a definition
#enter abbr and definition to create entry

'''
Need to organize this and comment it!  Works tho..
'''


import sys, shelve



def yes_no(string):
	answer = input(string)
	if (answer.lower() == 'yes') or (answer.lower() == 'y'):
		return 1
	elif (answer.lower() == 'q') or (answer.lower() == 'quit'):
		sys.exit()
	else:
		return 0


definition = ''
abbr = sys.argv[1].upper()
if len(sys.argv) > 2:
	definition = sys.argv[2]
	for arg in sys.argv[3:]:
		definition += (' ' + arg)


with shelve.open('churn_gloss') as churn_dic:
	try:
		if churn_dic[abbr]:
			if churn_dic[abbr] == definition:
				print('Already got it...')
				print('{}: {}'.format(abbr, churn_dic[abbr]))
			elif definition:
				confirm = yes_no('Change {} definition from \n{}\nto\n{}? (y/n): '.format(abbr, churn_dic[abbr], definition))
				if confirm:
					churn_dic[abbr] = definition
					print('Definition Changed!')
				else:
					print('{}: {}'.format(abbr, churn_dic[abbr]))
					print('\nNothing changed!')
				
			else:
				print('{}: {}'.format(abbr, churn_dic[abbr]))

	except KeyError:
		if definition:
			confirm = yes_no('Save {} as {}? (y/n):'.format(abbr, definition))
			if confirm:
				print('SAVED')
			else:
				print('No definition saved for ' + abbr)
		else:
			print('No definition found for ' + abbr)
			definition = input('Enter a definition or RETURN to exit:')
			if definition:
				churn_dic[abbr] = definition
				print('\n{}: {}'.format(abbr, churn_dic[abbr]))
				print('SAVED')
			else:
				print('Nothing Saved!')
				sys.exit()

