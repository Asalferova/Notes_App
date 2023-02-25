from InterfaceNotes import PersistenceManager, __str__


# Класс сохранения заметки в файле notes.csv
class SaveCsv(PersistenceManager):
    def save_file(self):
        # Открытие файла и запись заметки
        file = open('notes.csv', 'a')
        file.write(str(self.id) + ';' + str(self.title) + ';' + str(self.description) + ';' + str(self.data_log) + '\n')
        file.close()

    @staticmethod
    def read_file():
    # Считывание данных из файла
        with open('notes.csv', 'r') as file:
           print(file.read())
