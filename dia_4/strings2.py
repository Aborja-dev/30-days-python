#11. Replace the word coding in the string 'Coding For All' to Python.
text = 'Coding For All'[6:]

print('Python' + text)
#12. Change Python for Everyone to Python for All using the replace method or other methods.
print('Python For All'.replace('Python', 'Everyone'))
#13. Split the string 'Coding For All' using space as the separator (split()) .
print('Coding For All'.split(' '))
#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
#15. What is the character at index 0 in the string _Coding For All_.2
print('Coding For All'[0])
#16. What is the last index of the string _Coding For All_.
print('Coding For All'[-1])
#17. What character is at index 10 in "Coding For All" string.
print('Coding For All'[10])
#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
text = 'Python For Everyone'.split(' ')
_slice = slice(0,1)
print(text[0][0], text[1][0], text[2][0])
#19. Create an acronym or an abbreviation for the name 'Coding For All'.
text = 'Coding For All'.split(' ')
_slice = slice(0,1)
print(text[0][_slice], text[1][_slice], text[2][_slice])
#20. Use index to determine the position of the first occurrence of C in Coding For All.
print('Coding For All'.index('C'))
#21. Use index to determine the position of the first occurrence of F in Coding For All.
print('Coding For All'.index('F'))