def create_cook_book(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = file.readline().strip().split(' | ')
                ingredient_name = ingredient_info[0]
                quantity = int(ingredient_info[1])
                measure = ingredient_info[2]
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            
            cook_book[dish_name] = ingredients
            file.readline()  # пропускаем пустую строку между блюдами
    
    return cook_book

# Пример использования
file_name = 'recipes.txt'  # предполагается, что файл с рецептами называется 'recipes.txt'
cook_book = create_cook_book(file_name)
print(cook_book)

