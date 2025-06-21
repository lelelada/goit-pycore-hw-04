def total_salary(path):
    try:
        # Відкриваємо файл для читання з кодуванням UTF-8
        with open(path, 'r', encoding='utf-8') as file:
            total = 0     # Загальна сума зарплат
            count = 0     # Кількість розробників

            # Обходимо кожен рядок у файлі
            for line in file:
                # Розділяємо рядок по комі на прізвище та зарплату
                parts = line.strip().split(',')
                
                # Перевіряємо, чи правильно розділений рядок
                if len(parts) == 2:
                    try:
                        # Перетворюємо зарплату з рядка у число
                        salary = float(parts[1])
                        total += salary   # Додаємо до загальної суми
                        count += 1        # Збільшуємо лічильник працівників
                    except ValueError:
                        # Обробка помилки, якщо зарплата не є числом
                        print(f"Невірний формат зарплати в рядку: {line.strip()}")
                else:
                    # Повідомлення, якщо рядок некоректний
                    print(f"Пропущено некоректний рядок: {line.strip()}")

        # Якщо жодного коректного рядка не було
        if count == 0:
            return (0, 0)
        
        # Обчислюємо середню зарплату
        average = total / count
        return (total, average)

    except FileNotFoundError:
        # Повідомлення, якщо файл не знайдено
        print(f"Файл за шляхом '{path}' не знайдено.")
        return (0, 0)
    except Exception as e:
        # Загальна обробка будь-якої іншої помилки
        print(f"Сталася помилка при обробці файлу: {e}")
        return (0, 0)

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")        