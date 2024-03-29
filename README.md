# ImageAI (редактор изображений)

В проекте реализовано декстопное приложение для редактирования изоражений разных форматов.
В редакторе реализовано множество базовых функций улучшения фотографий, а также доступна функция нейрокисти, которая заполняет пропуски.

## Установка приложения

1) **Сделайте клон репозитория:**

    ```bash
    git clone https://github.com/Dianochka-L/ImageAI.git
    ```

2) **Создайте и активируйте виртуальное окружение Anaconda в дириктории вашего проекта:**

    ```bash
    conda create --name .conda python=3.11
    conda activate .conda
    ```

3) **Установите все необходимые зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

## Запуск

```bash
python main.py
```

## Структура

- app - модуль с частями приложения
    + __init__.py
    + controllers - это модуль с классами различных частей приложения
        - errors.py - ошибки, которые отслеживаются при работе программы
        - hello_controller.py - контроллер приветственного окна
        - main_controller.py - контроллер главного окна редактора
        - utils.py - функция для обработки изображений
        - __init__.py
    + ui - модуль
        - __init__.py
        - icons - папка с иконками для интерфейса
        - hello_window.py - загрузка интерфейса приветственного окна
        - main_window.py - загрузка интерфейса главного окна редактора
        - resources_rc.py -сокомпилированные ресурсы для интерфейса
- main.py - файл, в котором настраивается и запускается приложение
- .gitignore
- README.md
- requirements.txt - файл, в котором перечисленны зависимости
