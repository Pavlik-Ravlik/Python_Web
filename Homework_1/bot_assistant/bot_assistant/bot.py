import os
import sys
import pathlib
import pickle
from bot_assistant import parser_check

from bot_assistant.virtual_assistant import AddressBook
# from Notebook import Notebook
from bot_assistant.Notebook import Note
from bot_assistant.sorter import Sorter
from bot_assistant.bot_help import Bot_help
from bot_assistant.bot_setting import Bot_setting
from bot_assistant.my_utils import split
from abc import ABC, abstractclassmethod

module_directory = os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))


class BaseUserInterface(ABC):
    
    @abstractclassmethod
    def display_message(self, message):
        raise NotImplementedError

    @abstractclassmethod
    def get_user_input(self, prompt):
        raise NotImplementedError

    @abstractclassmethod
    def clear_screen(self):
        raise NotImplementedError


class ConsoleUserInterface(BaseUserInterface):
    def display_message(self, message):
        print(message)

    def get_user_input(self, prompt):
        return prompt

    def clear_screen(self):
        os.system('clear')

class Bot_assistant:

    def __init__(self, user_interface) -> None:
        self.interactive_mode = 0
        self.addressbook = None  # адресная книга
        self.notebook = None  # книга заметок
        self.bothelp = None
        self.load_setting()

        self.com_key = ''
        self.cur_name = None
        self.cur_phone = None
        self.cur_email = None
        self.user_interface = user_interface

        # self.setting_key = None

    def load_setting(self):
        bs = self.read_from_file(f'{module_directory}/Setting.bin')
        if bs is None or not isinstance(bs, Bot_setting):
            bs = Bot_setting()
        self.botsetting = bs

    def read_from_file(self, filename):
        path_bin = pathlib.Path(filename)
        unpacked = None
        if path_bin.exists():
            try:
                with open(path_bin, "rb") as fh:
                    unpacked = pickle.load(fh)
            except Exception:
                pass
        return unpacked

    def check_addressbook(self):
        if self.addressbook is None:
            ab = self.read_from_file(f'{module_directory}/AddressBook.bin')
            if ab is None or not isinstance(ab, AddressBook):
                ab = AddressBook()
            self.addressbook = ab

    def check_notebook(self):
        if self.notebook is None:
            nb = self.read_from_file(f'{module_directory}/NoteBook.bin')
            # if nb is None or not isinstance(nb, Notebook):
            #     nb = Notebook()
            if nb is None or not isinstance(nb, Note):
                nb = Note()
            self.notebook = nb

    def check_bothelp(self):
        if self.bothelp is None:
            self.bothelp = Bot_help()


    def save_to_file(self, filename, saved_class):
        if saved_class is not None:
            path_bin = pathlib.Path(filename)
            with open(path_bin, "wb") as fh:
                pickle.dump(saved_class, fh)

    def save_classes(self):
        self.save_to_file(f'{module_directory}/AddressBook.bin',self.addressbook)
        self.save_to_file(f'{module_directory}/NoteBook.bin', self.notebook)
        self.save_to_file(f'{module_directory}/Setting.bin', self.botsetting)

    # --------------------------------------------------------------------------------
    def fun_add_name(self, contact, value):
        # print(f'Добавляем контакт {contact}')
        self.check_addressbook()
        self.addressbook.rec_add(contact)

    def fun_get_name(self, contact, value):
        # print(f'Проверяем наличие контакта {contact}')
        self.check_addressbook()
        ab = self.addressbook.record_exists(contact)
        self.cur_name = value
        return ab is not None  # True - есть, False - нет

    def fun_del_name(self, contact, value):
        # print(f'Удаляем контакт {contact}')
        self.check_addressbook()
        self.addressbook.rec_delete(contact)

    def fun_add_phone(self, contact, value):
        # print(f'Добавляем телефон {value} контакту {contact}')
        self.check_addressbook()
        self.addressbook.phone_add(contact, value)

    def fun_get_phone(self, contact, value):
        # print(f'Проверяем наличие телефона {value} у контакта {contact}')
        self.check_addressbook()
        self.addressbook.record_exists(contact).phone_exists(value, -1)
        self.cur_phone = value

    def fun_set_phone(self, contact, value):
        # print(f'Заменяем телефон у контакта {contact} на {value}')
        self.check_addressbook()
        if self.cur_phone:
            if value:
                self.addressbook.phone_correct(contact, self.cur_phone, value)
            else:
                self.addressbook.phone_delete(contact, self.cur_phone)
        else:
            self.addressbook.phone_add(contact, value)
        self.cur_phone = None

    def fun_del_phone(self, contact, value):
        # print(f'Заменяем телефон у контакта {contact} на {value}')
        self.check_addressbook()
        self.addressbook.phone_delete(self, contact, value)

    def fun_set_birthday(self, contact, value):
        # print(f'Заменяем дату рождения у контакта {contact} на {value}')
        self.check_addressbook()
        self.addressbook.birthday_save(contact, value)

    def fun_set_address(self, contact, value):
        # print(f'Заменяем адрес у контакта {contact} на {value}')
        self.check_addressbook()
        self.addressbook.record_exists(contact).address_save(value)

    def fun_add_email(self, contact, value):
        # print(f'Добавляем eMail {value} контакту {contact}')
        self.check_addressbook()
        self.addressbook.record_exists(contact).email_add(value)

    def fun_get_email(self, contact, value):
        # print(f'Проверяем наличие eMail {value} у контакта {contact}')
        self.check_addressbook()
        self.addressbook.record_exists(contact).email_exists(value, -1)
        self.cur_email = value

    def fun_set_email(self, contact, value):
        # print(f'Заменяем eMail у контакта {contact} на {value}')
        self.check_addressbook()
        if self.cur_email:
            if value:
                self.addressbook.record_exists(contact).email_update(contact, self.cur_email, value)
            else:
                self.addressbook.record_exists(contact).email_delete(contact, self.cur_phone)
        else:
            self.addressbook.record_exists(contact).email_add(value)
        self.cur_email = None

    def fun_del_email(self, contact, value):
        # print(f'Заменяем eMail у контакта {contact} на {value}')
        self.check_addressbook()
        self.addressbook.record_exists(contact).email_delete(value)

    def fun_set_fullname(self, contact, value):
        # print(f'Заменяем ФИО у контакта {contact} на {value}')
        self.check_addressbook()
        self.addressbook.record_exists(contact).fullname_save(value)

    def fun_add_note(self, tags, note):
        # print(f'Добавляем заметку "{note}" с тегами {tags}')
        self.check_notebook()
        self.notebook.add_note(note, tags)

    def fun_set_note(self, tags, note):
        # print(f'Сохраняем измененную заметку "{note}" с тегами {tags}')
        self.check_notebook()
        self.notebook.edit_note(tags, note)

    def fun_del_note(self, tags, note):
        # print(f'Удаляем заметку с тегами {tags}')
        self.check_notebook()
        self.notebook.delete_note(tags)

    def fun_add_tag(self, tags, note):
        self.check_notebook()
        pass

    def fun_get_tag(self, tags, note):
        self.check_notebook()
        self.notebook.tag_exists(tags)

    def fun_set_tag(self, tags, note):
        self.check_notebook()
        self.notebook.edit_tag(tags, note)

    def fun_del_tag(self, tags, note):
        self.check_notebook()
        pass

    def fun_find_substring(self, substring, tmp):
        # Вывод всех контактов, содержащих подстроку {substring}
        self.check_addressbook()
        self.check_notebook()
        res = self.addressbook.search_records(substring)
        res_n = self.notebook.search_notes_by_substring(substring)
        print(res)

    def fun_find_note(self, substring, tmp):
        # print(f'Вывод всех заметок, содержащих подстроку {substring}')
        self.check_notebook()
        self.notebook.search_notes_by_substring(substring)

    def fun_show_name(self, name='', tmp=''):
        self.check_addressbook()
        if len(name) == 0:
            # Вывод всех записей адресной книги
            ls = ''
            for txt in self.addressbook.view_records(self.botsetting.display_lines):
                if len(ls) == 0:
                    ls = txt
                else:
                    print(ls.rstrip())
                    if input('. . .') == '/q':
                        ls = ''
                        break
                    ls = txt
            if len(ls) > 0:
                print(ls)
        else:
            res = self.addressbook.list_records(name)
            print('\n'.join(res))

    def fun_show_note(self, tag='', tmp=''):
        self.check_notebook()
        if self.notebook and len(tag) == 0:
            print('Вывод всех заметок')
            self.notebook.show()
        else:
            self.notebook.search_notes_by_tag(tag)

    def fun_show_birthday(self, days=7, tmp=''):
        self.check_addressbook()
        # head = f"Список контактів у яких день народження через {days} днів: \n"
        # res = ''
        # for record in self.addressbook.data.values():
        #     if record.birthday.value:
        #         dtb = int(record.days_to_birthday())
        #         if dtb <= int(days):
        #             res += f"{record.view_record()} | до ДР {dtb} днів.\n"
        # if res:
        #     return head + res
        # return "Відсутні контакти у яких день народження через {days} днів"
        return self.addressbook.view_birthdays(self.botsetting.number_of_days)


    # def fn_setting_save(self, contact, value):
    #     print(self.setting_key, contact, value)

    def fn_setting_details_save(self, contact, value):
        self.botsetting.set_request_details(value)

    def fn_setting_birthdays_save(self, contact, value):
        self.botsetting.set_display_birthdays(value)

    def fn_setting_of_days_save(self, contact, value):
        self.botsetting.set_number_of_days(value)

    def fn_setting_lines_save(self, contact, value):
        self.botsetting.set_display_lines(value)

    def fn_setting_language_save(self, contact, value):
        self.botsetting.set_language(value)

    def fun_show_setting(self, contact, value):
        return self.botsetting.view_setting()

    # --------------------------------------------------------------------------------
    def get_param(self, name, required):
        done = True
        while done:
            st = input(f'Введите {name} > ')
            if required and len(st) == 0:
                print('Параметр обязателен!')
            else:
                done = False
        return st

    def fun_hello(self, command, list_params):
        self.interactive_mode = 1
        res = 'Hello! \nHow can I help you?'
        if self.botsetting.display_birthdays:
            self.check_addressbook()
            res = self.addressbook.view_birthdays(self.botsetting.number_of_days) + '\n' + res
        return res

    def fun_exit(self, command, list_params):
        self.save_classes()
        self.interactive_mode = 0
        return 'Good bye!'

    def func_sorter(self, command, list_params):
        sort = Sorter()
        destination = input("Введіть шлях, куди сортувати (за замовчуванням '' - сортування в ту ж папку):")
        sort.run(list_params, destination)
        return 'Ok'

    def get_param_and_exec(self, command, list_params):
        # print(command, list_params)
        cmd_text = ''
        k = command.find('_')
        if k > 0:
            cmd_text = command[0:k]
        pars = self.params.get(command)  # словарь параметров команды
        if pars is None:
            return f'Не найден список параметров команды "{cmd_text}". Обратитесь к разработчику.'
        else:
            k = 0
            for key, val in pars.items():
                done = True
                if val[0] == 0 and self.botsetting.request_details == 0:
                    break
                while done:
                    if val[0] < 0:
                        name = ''
                        st = command
                    else:
                        if k >= len(list_params):  # параметр не задан в команде
                            st = self.get_param(val[1], val[0])  # запрашиваем параметр
                            if st == '/q':
                                return 'Ok'
                        else:
                            st = list_params[k]
                        if k == 0:
                            name = st
                            self.cur_name = name
                    try:
                        res = val[2](self, name, st)
                        k += 1
                        done = False
                    except Exception as e:
                        print(str(e))
            if res is None:
                return 'Ok'
            else:
                return res

    def fn_help(self, command, list_params):
        self.check_bothelp()
        if len(list_params) > 0:
            res = self.bothelp.view_help(list_params[0])
        else:
            ls = ''
            for txt in self.bothelp.view_help_iter(self.botsetting.language, self.botsetting.display_lines):
                if len(ls) == 0:
                    ls = txt
                else:
                    print(ls.rstrip())
                    if input('. . .') == '/q':
                        ls = ''
                        break
                    ls = txt
            res = None if len(ls) == 0 else ls
        return res

    # --------------------------------------------------------------------------------
    """
    Dictionary of valid commands.
    The key is the first word of the command.
    Value - list of command details:
    [0] - максимальное количество параметров комадды.
    [1] - ключ команды по умолчанию
    [2] - функция выполнения команды
    """
    funcs = {
        "hello": [0, '', fun_hello],
        "exit": [0, '', fun_exit],
        #
        "add": [6, 'contact', get_param_and_exec],
        "change": [6, 'contact', get_param_and_exec],
        "delete": [6, 'contact', get_param_and_exec],
        #
        "search": [1, '', get_param_and_exec],
        "show": [0, 'all', get_param_and_exec],
        #
        "help": [1, '', fn_help],
        "setting": [1, '', get_param_and_exec],
        #
        "sort": [1, '', get_param_and_exec]
    }

    keys = {
        "add": ['contact', 'phone', 'birthday', 'address', 'email', 'fullname', 'note'],
        "change": ['contact', 'phone', 'birthday', 'address', 'email', 'fullname', 'note'],
        "delete": ['contact', 'phone', 'email', 'note'],
        "search": ['note'],
        "show": ['all', 'contact', 'note', 'birthday', 'setting'],
        "help": [],
        "setting": ['request_details', 'display_birthdays', 'number_of_days', 'display_lines'],
        "sort": []
    }

    """
    [0] - обязательный ли параметр: 0 - необязательный, 1 - обязательный, -1 - необязательный и не запрашивать
    [1] - наименование параметра при запросе значения
    [2] - функция выполнения операции со значением параметра
    """
    params = {
        "add_contact": {'name': [1, 'Contact Name', fun_add_name],
                        'phone': [0, 'Contact Phone', fun_add_phone],
                        'birthday': [0, 'Contact BirthDay', fun_set_birthday],
                        'email': [0, 'Contact eMail', fun_add_email],
                        'address': [0, 'Contact Address', fun_set_address],
                        'fullname': [0, 'Contact FullName', fun_set_fullname]
                        },
        "add_phone": {'name': [1, 'Contact Name', fun_add_name],
                    'phone': [0, 'Contact Phone', fun_add_phone]
                    },
        "add_birthday": {'name': [1, 'Contact Name', fun_add_name],
                        'birthday': [0, 'Contact BirthDay', fun_set_birthday]
                        },
        "add_email": {'name': [1, 'Contact Name', fun_add_name],
                    'email': [0, 'Contact eMail', fun_add_email]
                    },
        "add_address": {'name': [1, 'Contact Name', fun_add_name],
                        'address': [0, 'Contact Address', fun_set_address]
                        },
        "add_fullname": {'name': [1, 'Contact Name', fun_add_name],
                        'fullname': [0, 'Contact FullName', fun_set_fullname]
                        },
        "add_note": {'tag': [0, 'Note Tag', fun_add_tag],
                    'note': [1, 'Text Note', fun_add_note]
                    },
        #
        "change_contact": {'name': [1, 'Contact Name', fun_get_name],
                           'phone': [0, 'Contact Phone', fun_set_phone],
                           'birthday': [0, 'Contact BirthDay', fun_set_birthday],
                           'email': [0, 'Contact eMail', fun_set_email],
                           'address': [0, 'Contact Address', fun_set_address],
                           'fullname': [0, 'Contact FullName', fun_set_fullname]
                        },
        "change_phone": {'name': [1, 'Contact Name', fun_get_name],
                        'phone': [0, 'Contact Phone', fun_get_phone],
                        'newphone': [0, 'New Contact Phone', fun_set_phone],
                        },
        "change_birthday": {'name': [1, 'Contact Name', fun_get_name],
                            'birthday': [0, 'Contact BirthDay', fun_set_birthday]
                            },
        "change_email": {'name': [1, 'Contact Name', fun_get_name],
                        'email': [0, 'Contact eMail', fun_get_email],
                        'newemail': [0, 'New Contact eMail', fun_set_email]
                        },
        "change_address": {'name': [1, 'Contact Name', fun_get_name],
                        'address': [0, 'Contact Address', fun_set_address]
                        },
        "change_fullname": {'name': [1, 'Contact Name', fun_get_name],
                            'fullname': [0, 'Contact FullName', fun_set_fullname]
                            },
        "change_note": {'tag': [0, 'Note Tag', fun_get_tag],
                        'note': [1, 'Text Note', fun_set_note]
                        },
        #
        "delete_contact": {'name': [1, 'Contact Name', fun_del_name]},
        "delete_phone": {'name': [1, 'Contact Name', fun_get_name],
                        'phone': [1, 'Contact Phone', fun_del_phone]
                        },
        "delete_email": {'name': [1, 'Contact Name', fun_get_name],
                        'email': [1, 'Contact eMail', fun_del_email]
                        },
        "delete_note": {'tag': [1, 'Note Tag', fun_del_note]},
        "delete_tag": {'tag': [1, 'Note Tag', fun_del_tag]},
        #
        "search": {'substring': [1, 'Substring', fun_find_substring]},
        "search_note": {'tag': [1, 'Note Tag', fun_find_note]},
        "show": {'all': [-1, '', fun_show_name]},
        "show_all": {'all': [-1, '', fun_show_name]},
        "show_name": {'name': [1, 'Contact Name', fun_show_name]},
        "show_birthday": {'days': [1, 'Кількість днів', fun_show_birthday]},
        "show_note": {'tag': [0, 'Note Tag', fun_show_note]},
        "show_birthday": {'days': [-1, 'Кількість днів', fun_show_birthday]},
        "show_setting": {'name': [-1, 'Setting Name', fun_show_setting]},
        "sort": {'source': [1, 'Шлях до папки сортування: ', func_sorter]},
        #
        "setting_request_details": {'value': [1, '"запрашивать ли недостающие реквизиты (1 - да, 0 - нет)"', fn_setting_details_save]},
        "setting_display_birthdays": {'value': [1, '"показывать при запуске ближайших именинников (1 - да, 0 - нет)"', fn_setting_birthdays_save]},
        "setting_number_of_days": {'value': [1, '"количество дней для ближайших именинников"', fn_setting_of_days_save]},
        "setting_display_lines": {'value': [1, '"количество строк в порции отображения"', fn_setting_lines_save]},
        "setting_language": {'value': [1, '"язык интерфейса (en - English, ru - русский, uk - український)"', fn_setting_language_save]}
    }

    def parcer(self, command):
        res = ''
        if len(command) > 0:
            self.com_key = ''
            # print(type(command))
            if type(command) == list:
                cm = command
            else:
                cm = split(command)
            cm0 = cm[0].lower()
            lcm = len(cm) - 1
            lfn = self.funcs.get(cm0)
            if lfn is None:
                res += '\n' + str(parser_check.closest_command(cm0, self.funcs.keys()))
            else:
                if len(cm) > 1:  # есть параметры
                    cm1 = cm[1]
                    if cm1.startswith('--'):  # Есть ключ команды
                        cm1 = cm1[2::]
                        self.com_key = cm1
                        cm.pop(1)  # убираем ключ команды
                    else:
                        cm1 = '--'
                else:
                    cm1 = '--'

                if cm1 == '--':  # смотрим ключ по умолчанию
                    cm1 = lfn[1]
                    if len(cm1) > 0:  # есть ключ по умолчанию
                        self.com_key = cm1
                        cm1 = '_' + cm1
                else:
                    # cmk = self.keys.get(cm1)
                    cmk = self.keys.get(cm0)
                    if cmk is None or self.com_key not in cmk:
                        res = f'Недопустимый ключ --{cm1} у команды {cm0}'
                        return res
                    cm1 = '_' + cm1
                cm1 = cm0 + cm1  # добавляем ключ к команде

                ecm = lfn[0]
                cm.pop(0)  # убираем команду из списка

                try:
                    res = lfn[2](self, cm1, cm)
                except Exception as e:
                    res = str(e)
        else:
            # print('Переход в интеактивный режим ввода команд.')
            res = self.fun_hello('hello', [])
        return res

    def clear_screen(self):
        os.system('clear')

    def main(self):
        sys_argv = sys.argv
        # sys_argv = ['bot.py']
        # sys_argv = ['bot.py','show']
        # sys_argv = ['bot.py','add', 'Юрий']
        command = []
        if len(sys_argv) > 1:
            for i in range(len(sys_argv)-1):
                command.append(sys_argv[i+1])
        while True:
            res = self.parcer(command)
            if res is not None:
                ConsoleUserInterface.display_message(res)
            if self.interactive_mode == 0:
                break
            cmd = ConsoleUserInterface.get_user_input('>> ')
            command = split(cmd)
            #ConsoleUserInterface.clear_screen()
        self.save_classes()


if __name__ == "__main__":
    console = ConsoleUserInterface()
    ba = Bot_assistant(console)
    ba.main()
