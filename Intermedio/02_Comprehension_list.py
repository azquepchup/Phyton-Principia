# Comprehension List
sep = ("=" * 123) 



normal_list = [1, 2, 3, 4, 5, 6, 7, 8] #lista normal
print(normal_list)

comprehension_list = [i for i in range(9)]
print(comprehension_list)

my_string = "Las patas de gabo"
comprehension_list = [i for i in my_string]
print(comprehension_list)

print(sep)

comprehension_listm = [i * 2 for i in range(9)] #multimplico por cualquier cosa hasta puede ser por el mismo numero
print(comprehension_listm)

comprehension_listexp2 = [i * i for i in range(9)] # serian potencias de 2
print(comprehension_listexp2)

print(sep)

def sum_number (number):
    number += 10
    return number

compr_sum = [sum_number(i) for i in range(9)]
print(compr_sum)