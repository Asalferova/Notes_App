from InterfaceNotes import Edit, __str__
import csv

# Класс редактирования заметки в файле notes.csv
class EditCsv(Edit):
    def edit_note(id):
    # Чтение из файла
        with open("notes.csv", "r") as file:
           reader = csv.reader(file, delimiter=';')
           notes = list(reader)
    
    # Нахождение заметки для редактирования
        found = False
        for note in notes:
            if note[0] == id:
            # Редактирование заметки
               found = True
               newTitle = input("Введите новый заголовок для заметки: ")
               newNote = input("Введите текс новой заметки: ")
               note[1] = newTitle
               note[2] = newNote
               print("Заметка отредактирована! ", note)
               break
        if not found:
            print("Заметка не найдена")
            return
    
    # Перезапись заметки в файл
        with open("notes.csv", "w", newline="") as file:
           writer = csv.writer(file, delimiter=';')
           writer.writerows(notes)