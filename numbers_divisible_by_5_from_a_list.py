#Iterate the given list of numbers and print only those numbers which are divisible by 5
number_list = list()
number_list.append(10)
number_list.append(20)
number_list.append(33)
number_list.append(46)
number_list.append(55)
print(number_list)

given_list_len = 0
print('the ones that are divisible by 5 are:')
while given_list_len < len(number_list):
    if number_list[given_list_len] % 5 == 0:
        print (number_list[given_list_len])
    given_list_len += 1