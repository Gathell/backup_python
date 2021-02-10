# Моя первая программа по созданию бэкапов

import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\Users\\pcadmin\\Desktop\\Python"', 'C:\\Users\\pcadmin\\Pictures']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'D:\\Backup' # Подставьте ваш путь.

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y-%m-%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H-%M-%S')

#Запрашиваем комментарийпользователя для имени фаила
comment = input("введите коментарий --> ")
if len(comment) == 0: #проверяем, введен ли коментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
    print('Каталог успешно создан', today)

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "C:\PROGRA~1\WinRAR\WinRAR.exe u -as -dh {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')

    