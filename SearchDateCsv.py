from InterfaceNotes import SearchDate, __str__
import csv


# Класс поиска заметки по дате в файле notes.csv
class SearchDateCsv(SearchDate):
    @staticmethod
    def search_by_date(date):
    # Чтение из файла
        with open("notes.csv", "r") as file:
           reader = csv.reader(file, delimiter=';')
           notes = list(reader) 
        
        # Нахождение заметки по введенной пользователем дате
        found = False
        for note in notes:
            if date in note[3]:
            # Вывод найденной заметки
               found = True
               print(note)
        if not found:
            print("Заметка не найдена!")
            return  
            
        return None