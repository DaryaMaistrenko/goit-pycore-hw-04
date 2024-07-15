def get_cats_info(path):
    try:
        cats_info = []
        
        # Відкриття файлу та читання даних
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Обробка кожного рядка файлу
        for line in lines:
            try:
                cat_id, name, age = line.strip().split(',')
                cat_dict = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_info.append(cat_dict)
            except ValueError:
                # У випадку помилки формату пропускаємо рядок
                continue
        
        return cats_info
    
    except FileNotFoundError:
        # У випадку відсутності файлу
        print(f"Файл {path} не знайдено.")
        return []
    except Exception as e:
        # Інші можливі помилки
        print(f"Сталася помилка: {e}")
        return []

# Приклад виклику функції
path = 'main - task 2.txt'
print(get_cats_info(path))
