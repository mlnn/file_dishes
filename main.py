def read_cook_book(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
             dish_file = line.strip().lower()
             list_line_indigrients = []
             count = int(f.readline())
             for i in range(count):
                line_indigrients = f.readline().split(' | ')
                list_line_indigrients.append({'ingridient_name': line_indigrients[0].strip().lower(), 'quantity': int(line_indigrients[1]),
                                        'measure': line_indigrients[2].strip()})
             cook_book[dish_file] = list_line_indigrients
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = read_cook_book('dishes')
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))

def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')

    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()