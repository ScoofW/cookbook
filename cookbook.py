def create_cook_book(file_name):
    cook_book = {}
    with open(file_name, "r", encoding="utf-8") as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break

            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = file.readline().strip().split(" | ")
                ingredient_name = ingredient_info[0]
                quantity = int(ingredient_info[1])
                measure = ingredient_info[2]
                ingredients.append(
                    {
                        "ingredient_name": ingredient_name,
                        "quantity": quantity,
                        "measure": measure,
                    }
                )

            cook_book[dish_name] = ingredients
            file.readline()  # пропускаем пустую строку между блюдами

    return cook_book


file_name = (
    "recipes.txt"  # предполагается, что файл с рецептами называется 'recipes.txt'
)
cook_book = create_cook_book(file_name)


def get_ingredient(ingredient_string):
    name, quantity, measure = ingredient_string.strip().split(" | ")
    return {"ingredient_name": name, "quantity": int(quantity), "measure": measure}


def get_shop_list_by_dishes(dishes, person_count, recipes):
    shop_list = {}
    for dish in dishes:
        recipe = get_recipe(dish, recipes)
        if recipe:
            for ingredient in recipe:
                name = ingredient["ingredient_name"]
                measure = ingredient["measure"]
                quantity = ingredient["quantity"] * person_count

                if name in shop_list:
                    shop_list[name]["quantity"] += quantity
                else:
                    shop_list[name] = {"quantity": quantity, "measure": measure}

    return shop_list


def get_recipe(recipe_name, recipes):
    if recipe_name in recipes:
        return recipes[recipe_name]
    else:
        print(f"Рецепт для блюда '{recipe_name}' не найден.")
        return None


# Пример использования
dishes = input().split(", ")
person_count = int(input())

result = get_shop_list_by_dishes(dishes, person_count, cook_book)
print(result)
