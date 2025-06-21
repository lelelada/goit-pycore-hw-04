def get_cats_info(path):
    cats_list = []  # Список для зберігання словників про котів

    try:
        # Відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Видаляємо зайві символи на початку і в кінці, ділимо по комах
                parts = line.strip().split(',')

                # Перевіряємо, чи рядок має рівно 3 елементи
                if len(parts) == 3:
                    cat_id, name, age = parts
                    # Додаємо інформацію про кота у вигляді словника
                    cat_info = {"id": cat_id, "name": name, "age": age}
                    cats_list.append(cat_info)
                else:
                    print(f"Пропущено некоректний рядок: {line.strip()}")

        return cats_list

    except FileNotFoundError:
        print(f"Файл не знайдено за шляхом: {path}")
        return []
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return []

cats_info = get_cats_info("cats.txt")
print(cats_info)