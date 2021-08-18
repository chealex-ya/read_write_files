import os
import pprint

file_path = os.path.join(os.getcwd(), "recipes.txt")

# Задача 1

cook_book = {}
book_counter = {}

with open (file_path) as file:
    for line in file:
        list_of_ingridients = []
        name = line.strip()
        counter = int(file.readline())
        new_list = []
        for i in range(counter):
            list_of_ingridients = list(file.readline().split(sep='|'))
            ingridient =    {
                            'ingridient_name' : list_of_ingridients[0],
                            'quantity' : list_of_ingridients[1],
                            'measure' : list_of_ingridients[2].rstrip()
                             }
            new_list.append(ingridient)
        cook_book[name] = new_list
        book_counter[name] = counter
        file.readline()

    pp = pprint.PrettyPrinter()
    print('Моя кулинарная книга: \n')
    pp.pprint(cook_book)


# Задача 2

    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}
        for d in dishes:
            for k, v in cook_book.items():
                if k == d:
                    for i in range(book_counter.get(d)):
                        if v[i].get('ingridient_name') not in shop_list.keys():
                            new_quantity = int(v[i].get('quantity'))*person_count
                            shop_list[v[i].get('ingridient_name')] = {'measure' : v[i].get('measure'), 'quantity' : new_quantity}
                        else:
                            new_quantity = (int(v[i].get('quantity'))*person_count) + int((shop_list.get(v[i].get('ingridient_name'))).get('quantity'))
                            shop_list[v[i].get('ingridient_name')] = {'measure': v[i].get('measure'),'quantity': new_quantity}
        pp = pprint.PrettyPrinter()
        print("\nСписок покупок: \n")
        pp.pprint(shop_list)

    # Для проверки повторяемости ингридиентов, изменил состав блюда "Запеченый картофель" -
    # также добавил соевый соус.

    get_shop_list_by_dishes(['Запеченный картофель', 'Утка по-пекински'], 10)