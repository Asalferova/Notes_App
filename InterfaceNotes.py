from abc import abstractmethod
import datetime


# Класс, реализующий интерфейс
class InterfaceNotes:

    # Инициализация значений
    def __init__(self, title, description):
        self.data_log = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.title = title
        self.description = description


    def __str__(self):
        return (str(self.id) + ';' + str(self.title) + ';' + str(self.description) + ';' + str(self.data_log))
        


# Класс сохранения и чтения из файла
class PersistenceManager:
    @abstractmethod
    def save_file():
        pass

    @abstractmethod
    def read_file():
        pass


# Класс поиска заметок по айди
class SearchId:
    @abstractmethod
    def search_by_id():
        pass


# Класс поиска заметок по дате
class SearchDate:
    @abstractmethod
    def search_by_date():
        pass


# Класс редактирования
class Edit:
    @abstractmethod
    def edit_note():
        pass


# Класс удаления
class Remove:
    @abstractmethod
    def remove_note(id):
        pass