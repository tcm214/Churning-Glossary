#! python3

#Run: churn [abbr] [definition]*
#enter just an abbr to request a definition
#enter abbr and definition to create entry


import sys, shelve



def deleteCheck(command, entry):
	'''
	check if they want to delete something instead of add or look up.  this will be rarely used.
	'''
	if (command.lower() == 'del') or (command.lower() == 'delete'): # gotta use .lower() cuz DELETE looks like a boolean or something
		with shelve.open('churn_gloss') as churn_dic:
			try:
				del churn_dic[entry]
				print(entry + ' Deleted')
			except KeyError:
				print(entry + ' Not Found.')
		
		sys.exit()
	return


def yes_no(string):
	'''
	trying to use this more.  little yes/no prompt with quit check included.  returns 1 (True) if y or yes
	'''
	answer = input(string)
	if (answer.lower() == 'yes') or (answer.lower() == 'y'):
		return 1
	elif (answer.lower() == 'q') or (answer.lower() == 'quit'):
		sys.exit()
	else:
		return 0


definition = ''
abbr = sys.argv[1].upper()

#check if they want to delete something first
deleteCheck(abbr, sys.argv[2])

#if a def has been entered, create definition string
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





#churn_dic.close()
