#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('Coding For All People'.rfind('l'))
#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))
#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

#26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
#27. Does '\'Coding For All' start with a substring _Coding_?
print('\'Coding For All'.startswith('Coding'))
#28. Does 'Coding For All' end with a substring _coding_?
print('Coding For All'.startswith('coding'))
#39. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
print('&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;')
print('   Coding For All      '.strip())
#31. Which one of the following variables return True when we use the method isidentifier():
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
#32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(libraries))