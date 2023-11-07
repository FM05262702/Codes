# Filip Mazur
# 07/11/2023
# Linear Search

list = [1, 2, 7, 11, 20, 30, 74, 31, 86, 99, 4]

search_term = int(input("Enter a search term: "))

found = False

x = 0



while (found == False and x < len(list)):
    
    if (search_term == list[x]):

        found = True

    x = x + 1



if (found == True):

    print("Found date item")

else:
    
    print("Not found date item")
