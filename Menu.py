from InterfaceNotes import *
from SaveCsv import *
from SearchDateCsv import *
from EditCsv import *
from RemoveCsv import *
from SearchIdCsv import *

class Menu():                                
    def main(self):
        print("Note App")
        print("1. Создать заметку")
        print("2. Показать все заметки")
        print("3. Посмотреть заметку по айди")
        print("4. Выбрать заметки по дате")
        print("5. Редактировать заметку")
        print("6. Удалить заметку")
        print("7. Выход")

        s = input("Ваш выбор: ")
        if (s == "1"):
            n = InterfaceNotes(input("Введите заголовок заметки "), input("Введите текст заметки "))
            SaveCsv.save_file(n)
            print("Заметка создана и сохранена!")
        elif s == "2":
            SaveCsv.read_file()
        elif s == "3":
            SearchIdCsv.search_by_id(input("Введите айди заметки: "))
        elif s == "4":
            SearchDateCsv.search_by_date(input("Введите дату в формате гггг-мм-дд (прим:2022-02-23): "))
        elif s == "5":
            EditCsv.edit_note(input("Введите айди заметки, которую вы хотите отредактировать "))
        elif s == "6":
            RemoveCsv.remove_note(input("Введите айди заметки, которую вы хотите удалить "))
        elif s == "7":
            exit()
        else:
            print("Такой опции нет, попробуйте ещё раз")


a = Menu()
if __name__ == '__main__':
    while True:
        flag = input("Запустить приложение? д/н: ")

        if flag == 'д':
           a.main()
        else: 
            break