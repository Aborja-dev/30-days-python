#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
text = 'Thirty' + 'Days' + 'Of' + 'Python' 
print(text)
#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
text = 'Coding' + 'For' + 'All'
print(text)
#3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
#4. Print the variable company using _print()_.
print(company)
#5. Print the length of the company string using _len()_ method and _print()_
print(len(company))
#6. Change all the characters to uppercase letters using _upper()_ method.
print(company.upper())
#7. Change all the characters to lowercase letters using _lower()_ method.
print(company.lower())
#8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
print('capitalize','Coding For All'.capitalize())
print('title','Coding For All'.title())
print('swapcase','Coding For All'.swapcase())
#9. Cut(slice) out the first word of _Coding For All_ string.
word = 'Coding For All'.split(' ')
print(word[0])
#10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
print('Coding For All'.index('Coding'))
print('Coding For All'.find('Coding'))