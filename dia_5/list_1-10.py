
def print_results(results):
   list = results
   print(
       '''####0 Days of Python Dia 5: Listas
         1. Declare an empty list
         R={}
         2. Declare a list with more than 5 items
         R={}
         3. Find the length of your list
         R={}
         4. Get the first item, the middle item and the last item of the list
         R={}
         5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
         R={}
         6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
         R={}
         7. Print the list using _print()_
         R={}
         8. Print the number of companies in the list
         R={}
         9. Print the first, middle and last company
         R={}
         10. Print the list after modifying one of the companies
         R={}
   '''.format(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9])
   )

result = []
#1. Declare an empty list
empty = []
result.append(empty)
#2. Declare a list with more than 5 items
_list = [2,3.6,3+5j,'hola', 789, 54]
result.append(_list)
#3. Find the length of your list
result.append(len(_list))
#4. Get the first item, the middle item and the last item of the list
result.append([_list[0], _list[len(_list)//2], _list[-1]])
#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_type = ['Abraham', 20, 1.78, 'single', 'mi casa Av1']
result.append(mixed_data_type)
#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
result.append('it companies' + f'{it_companies}')
#7. Print the list using _print()_
result.append(it_companies)
#8. Print the number of companies in the list
result.append(len(it_companies))
#9. Print the first, middle and last company
result.append([it_companies[0], it_companies[len(it_companies)//2], it_companies[-1]])
#10. Print the list after modifying one of the companies
list2 = it_companies.copy()
list2 = list2[1:]
result.append(list2)

print_results(result)
