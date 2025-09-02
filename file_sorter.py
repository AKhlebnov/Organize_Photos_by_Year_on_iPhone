from pathlib import Path
import shutil

# Путь к основной папке
source_dir = Path(r"D:\IPHONE Anna\Фото")
years_found = set()
source_dir.joinpath()

# Сначала собираем все года из названий папок
for folder in source_dir.iterdir():
    if folder.is_dir() and folder.name[:4].isdigit():
        year = folder.name[:4]  # Берем первые 4 символа
        if 2000 <= int(year) <= 2030:  # Проверяем, что это разумный год
            years_found.add(year)
            print(f"Найден год: {year} в папке: {folder.name}")

# Создаем папки для каждого года
for year in years_found:
    year_dir = source_dir / year
    year_dir.mkdir(exist_ok=True)
    print(f"Создана/найдена папка для года: {year}")

# Теперь перемещаем файлы
for folder in source_dir.iterdir():
    # Пропускаем уже созданные папки с годами
    if folder.is_dir() and folder.name not in years_found and folder.name[:4].isdigit():
        year = folder.name[:4]
        if year in years_found:
            target_dir = source_dir / year
            
            for file in folder.iterdir():
                if file.is_file():
                    # Формируем новый путь с проверкой на существование
                    new_path = target_dir / file.name
                    counter = 1
                    
                    # Если файл уже существует, добавляем номер
                    while new_path.exists():
                        new_path = target_dir / f"{file.stem}_{counter}{file.suffix}"
                        counter += 1
                    
                    # Перемещаем файл
                    shutil.copy2(str(file), str(new_path))
                    print(f"Скопирован: {file.name} -> {new_path.name}")

print("Сортировка завершена!")