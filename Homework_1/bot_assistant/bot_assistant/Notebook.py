from datetime import datetime
from time import sleep
import pickle
from abc import ABC, abstractclassmethod


class AbstractNote(ABC):
    
    @abstractclassmethod
    def hello(self):
        pass

    @abstractclassmethod
    def add_note(self):
        pass

    @abstractclassmethod
    def search_notes_by_tag(self):
        pass

    @abstractclassmethod
    def search_notes_by_substring(self):
        pass

    @abstractclassmethod
    def edit_note(self):
        pass
    
    @abstractclassmethod
    def tag_exists(self):
        pass

    @abstractclassmethod
    def edit_tag(self):
        pass

    @abstractclassmethod
    def delete_note(self):
        pass

    @abstractclassmethod
    def delete_all(self):
        pass

    @abstractclassmethod
    def sort_notes_by_tag(self):
        pass

    @abstractclassmethod
    def show(self):
        pass

    @abstractclassmethod
    def note_generator(self):
        pass

    @abstractclassmethod
    def save_to_bin(self):
        pass

    @abstractclassmethod
    def load_from_bin(self):
        pass

    @abstractclassmethod
    def display(self):
        pass


class Note(AbstractNote):
    
    # Функція ініціалізації змінних.
    def __init__(self):
        self.notes = []
        self.dates = None

    def display(self):
        return self.notes
    
    # Функція привітання
    def hello(self):
        command = 'Список доступних команд.\nAdd - добавить новую заметку.\nfind - поиск заметки по тегу или по записи.\nEdit - редактировать заметку по индексу.\nDelete - удалить заметку по индексу.\nSort - сортировать заметку по тегу.\nShow all - Для показу всіх нотатків і тегів.\nShow num - Для показу нотатків за кількістю.\nClose - вийти из заметок.\n>>>> '
        return command

    # Функція для добавлення нотатків та тегів по ним.
    def add_note(self, note_text, tags):
        note = {}

        if len(tags) == 0 or tags == ['']:
            tags = '#'
            note['tags'] = tags

        elif len(note_text) == 0 or note_text == '':
            note_text = 'Empty'
            note = {'text': note_text}
        elif len(note_text) > 120:
            raise ValueError('Нельзя записать больше 120 символов.')

        note = {'text': note_text, 'tags': tags}
        self.notes.append(note)
        self.dates = datetime.now()
        delay = 2
        print(
            f"Заметка - {note_text} по тегу или тегам {tags} - сохранена.\n Время - {self.dates.strftime('%Y-%B-%d === %H:%M:%S')}")
        sleep(delay)

    # Функція для пошуку текста по тегу.
    def search_notes_by_tag(self, keyword):
        found_notes = []
        delay = 1

        for note in self.notes:
            if keyword in note['tags']:
                found_notes.append(note)

        if found_notes and found_notes != 'Empty':
            print("Найдены заметки:")
            for note in found_notes:
                print(note['text'])
                sleep(delay)
        else:
            print("Заметки не найдены.")
            sleep(delay)

    # Функція для пошуку текста по тегу.
    def search_notes_by_substring(self, keyword):
        found_notes = []
        delay = 1

        for note in self.notes:
            if keyword in note['text']:
                found_notes.append(note)

        if found_notes and found_notes != 'Empty':
            print("Найдены заметки:")
            for note in found_notes:
                print(note['text'])
                sleep(delay)
        else:
            print("Заметки не найдены.")
            sleep(delay)

    # Функція для редагування нотатку.
    def edit_note(self, keyword, new_text):

        for note in self.notes:

            if keyword in note['tags']:
                note['text'] = new_text

            self.dates = datetime.now()
            print("Заметка отредактирована.")

    # Перевірка наявності тега.
    def tag_exists(self, keyword):
        for note in self.notes:
            return keyword in note['tags']
        raise Exception(f'Тег "{keyword}" не знайдений серед нотаток!')

    # Функція для редагування тегу.
    def edit_tag(self, keyword, new_text):

        for note in self.notes:

            if keyword in note['tags']:
                note['tags'] = new_text

            self.dates = datetime.now()
            print("Заметка отредактирована.")

    # Функція дял видалення замітки.
    def delete_note(self, keyword):

        for note in self.notes:

            if keyword in note['tags']:
                note['text'] = 'Empty'
                print(f"Заметка удалена.")

            else:
                print("Тег не существует.")

    # Функція для видалення всього.
    def delete_all(self):
        note = self.notes
        note.clear()
        print('Всі замітки та теги видаленні')

    # Функція для сортування нотатків по тегам.
    def sort_notes_by_tag(self, tag):
        sorted_notes = []

        for note in self.notes:

            if tag in note['tags']:
                sorted_notes.append(note)

        if sorted_notes:
            sorted_notes.sort(key=lambda x: x['text'])
            print(f"Отсортированные заметки: {sorted_notes}")

            for note in sorted_notes:
                print(note['text'])

        else:
            print("Заметки с указанным тегом не найдены.")

    # Для показу всіх нотатків та тегів.
    def show(self):

        for numbering, dic_t in enumerate(self.notes, 1):
            stroka = ''

            if len(dic_t['tags']) > 1:
                for a in dic_t['tags']:
                    stroka += a + ' '
            else:
                for a in dic_t['tags']:
                    stroka += a

            tags = stroka
            text = dic_t['text']
            print('{:^2}|{:^10}|==={:^10}==='.format(numbering, tags, text))

        return 'Заметок больше нет'

    # Функція генератор для нотатків та тегів по заданній кількості.
    def note_generator(self, index):
        index = 0

        while int(index) < len(self.notes):

            yield self.notes[index:index+2]
            index += 2

    # Функція для зберігання нотатків та тегів.
    def save_to_bin(self, filename):

        with open(filename, 'wb') as file:
            pickle.dump(self.notes, file)

    # Функція для загрузки нотатків та тегів.
    def load_from_bin(self, filename):

        with open(filename, 'rb') as file:
            self.notes = pickle.load(file)


class BaseInterface:

    def display(self, notes, dates):
        pass


class GuiInterface(BaseInterface):

    def display(self, notes, dates):
        pass

class ConsoleInterface(BaseInterface):

    def display(self, notes, dates):
        pass
