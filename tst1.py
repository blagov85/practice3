def couple(my_list):
    new_list = []
    for item in my_list:
        if item % 2 == 0:
            new_list.append(item)
    return new_list

def main():
    new_list = []
    for item in range(1, 11):
        new_list.append(item)


list_figures = [2,3,5,6,7,8,9,10]
print(couple(list_figures))
print(main())