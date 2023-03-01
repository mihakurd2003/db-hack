# Скрипт для электронного журнала

Скрипт для электронного журнала, позволяющий изменять данные

### Как установить

- Скачайте код и поместите script.py на сервере в папку рядом с файлом manage.py
```
git clone https://github.com/mihakurd2003/db-hack.git
```

Python3 должен быть уже установлен.
### Как пользоваться файлом script.py
- В терминале набирайте любую из команд:
```
python3 script.py --fix_marks "<ФИО или ФИ ученика>"
```
или
```
python3 script.py -U "<ФИО или ФИ ученика>"
```
- Исправляет оценки ученику.
---
```
python3 script.py --remove_chastisements "<ФИО или ФИ ученика>"
```
или
```
python3 script.py -D "<ФИО или ФИ ученика>"
```
- Удаляет плохие замечания ученика.
---
```
python3 script.py --create_commendation "<ФИО или ФИ ученика>, <Предмет учащегося>"
```
или
```
python3 script.py -A "<ФИО или ФИ ученика>, <Предмет учащегося>"
```
- Создаёт похвальную запись на последний проведённый урок по заданному предмету
 ---