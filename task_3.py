import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для Windows-консолі
init(autoreset=True)

def print_directory_structure(directory: Path, prefix: str = ""):
    """
    Рекурсивно виводить структуру директорії з кольорами.
    """
    if not directory.exists():
        print(Fore.RED + f"❌ Шлях '{directory}' не існує.")
        return
    if not directory.is_dir():
        print(Fore.RED + f"❌ Шлях '{directory}' не є директорією.")
        return

    entries = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "┗━ " if is_last else "┣━ "

        if entry.is_dir():
            print(prefix + Fore.BLUE + connector + entry.name + "/")
            new_prefix = prefix + ("   " if is_last else "┃  ")
            print_directory_structure(entry, new_prefix)
        else:
            print(prefix + Fore.GREEN + connector + entry.name)


if len(sys.argv) != 2:
    print("🔧 Використання: python hw03.py <шлях_до_директорії>")
    sys.exit(1)

dir_path = Path(sys.argv[1])
print(Fore.YELLOW + f"📂 Структура директорії: {dir_path.resolve()}\n")
print_directory_structure(dir_path)