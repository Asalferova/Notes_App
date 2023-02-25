from InterfaceNotes import SearchId, __str__
import csv


# Класс поиска заметки по дате в файле notes.csv
class SearchIdCsv(SearchId):
    @staticmethod
    def search_by_id(id):
    # Чтение из файла
        with open("notes.csv", "r") as file:
           reader = csv.reader(file, delimiter=';')
           notes = list(reader) 
        
        # Нахождение заметки по введенному пользователем айди
        found = False
        for note in notes:
            if id == note[0]:
            # Вывод найденной заметки
               found = True
               print(note)
        if not found:
            print("Заметка не найдена!")
            return  
            
        return None