#1
my_dict = {'Данил':2003, "Дмитрий":2004,'Михаил':2005}
print(my_dict)
print(my_dict['Данил'])
print(my_dict.get('Денис'))
my_dict.update({'Марина':2002,'Владимир Красное Солнышко':988})
print(my_dict)
del my_dict['Владимир Красное Солнышко']
print(my_dict)
#2
my_set = {1,2,1,2,3, True , 4.04, "Касиопей", (9,8,7)}
print(my_set)
my_set.update([7,8,9,10,11])
print(my_set)
my_set.remove(2)
print(my_set)