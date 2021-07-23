from pprint import pprint

def cook_book_f():
    cook_book = {}
    with open("recipes.txt", "r", encoding="utf-8") as f:
      for line in f:
        dish_name = line.strip()
        ingredients_quantity = int(f.readline().strip())
        ingredients_list = []
        for ingredients in range(ingredients_quantity):
          data = f.readline().strip()
          data_ingredient = data.split('|')
          data_ingredient_dict = {}
          data_ingredient_dict["ingredient_name"] = data_ingredient[0]
          data_ingredient_dict["quantity"] = data_ingredient[1]
          data_ingredient_dict["measure"] = data_ingredient[2]
          ingredients_list.append(data_ingredient_dict)
        f.readline()
        cook_book[dish_name] = ingredients_list
    return cook_book


# print(cook_book_f())


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = cook_book_f()
    dishes_list = list(dishes)
    result = {}
    for dish_name in dishes_list:
        if dish_name in cook_book:
            for dish in cook_book[dish_name]:
                ingredients = {}
                ingredient_name = dish['ingredient_name']
                ingredients['measure'] = dish['measure']
                ingredients['quantity'] = int(dish['quantity']) * person_count
                if dish['ingredient_name'] in result:
                    ingredients['quantity'] += int(dish['quantity']) * person_count
                result[ingredient_name] = ingredients

    return result


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], person_count=2))


