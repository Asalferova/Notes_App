from InterfaceNotes import Remove, __str__
import csv


# Класс удаления заметки в файле notes.csv
class RemoveCsv(Remove):
    @staticmethod
    def remove_note(id):
    # Чтение из файла
        with open("notes.csv", "r") as file:
           reader = csv.reader(file, delimiter=';')
           notes = list(reader)
        # Нахождение заметки для удаления 
        # и добавление остальных заметок в созданный массив для последующего перезаписываняия файла
        lines = []
        for note in notes:
            if (id != note[0]):
                lines.append(note)
        # Перезаписывание файла с исключением найденной заметки
        with open("notes.csv", "w", newline = '') as file:
            writer = csv.writer(file, delimiter=';')
            for line in lines:
                writer.writerow(line)
            print("Заметка удалена!", line)