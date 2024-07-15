def total_salary(path):
    try:
        # Відкриття файлу та читання даних
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Перевірка, чи файл не пустий
        if not lines:
            return (0, 0)
        
        total_salary = 0
        count = 0
        
        # Обробка кожного рядка файлу
        for line in lines:
            try:
                surname, salary = line.strip().split(',')
                total_salary += int(salary)
                count += 1
            except ValueError:
                # У випадку помилки формату пропускаємо рядок
                continue
        
        # Розрахунок середньої заробітної плати
        if count == 0:
            return (0, 0)
        
        average_salary = total_salary / count
        
        return (total_salary, average_salary)
    
    except FileNotFoundError:
        # У випадку відсутності файлу
        print(f"Файл {path} не знайдено.")
        return (0, 0)
    except Exception as e:
        # Інші можливі помилки
        print(f"Сталася помилка: {e}")
        return (0, 0)

# Приклад виклику функції
path = 'main - task 1.txt'
print(total_salary(path))


