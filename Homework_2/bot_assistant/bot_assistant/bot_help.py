
class Bot_help:
    help_dict = {
        'en': {
            'header': [
                "This is a bot-assistant.",
                "Bot implemented as a console application.",
                "",
                "Executes commands:"
            ],
            'hello': [
                "'hello' - responds to 'How can I help you?', goes into interactive mode and displays the invitation '>>'.",
                "    The bot goes into interactive mode at startup without any parameters at all."
            ],
            'exit': [
                "'exit' - outputs 'Good bye!' and completes its work interactively."
            ],
#------------------------------------   AddresssBook   ---------------------------------
            'add': [
                "'add [--<key>] [<Name> [<Phone> | <BirthDay> | <Email> | <Address> | <FullName>]]'",
                "  - saves a new contact / phone / birthday / email / address / fullname in the phonebook.",
                "  <key>: {contact | name} | phone | birthday | email | address | fullname}"
            ],
            'change': [
                "'change [--<key>] <Name> [<Phone> | <BirthDay> | <Email> | <Address> | <FullName>]'",
                "    - saves the new phone number / birthday / email / address / fullname of an existing contact in the phonebook.",
                "    <key>: phone | birthday | email | address | fullname"
            ],
            'delete': [
                "'delete [--<key>] <Name> | <Phone>' - deleting a contact by name from the phone book / phone from a contact by name.",
                "    <key>: {contact | name} | phone"
            ],
            'search': [
                "'search <mask>' - search for contacts by fragment of name or by fragment of phone number."
            ],
            'show': [
                "'show [--<key>] [<Name>]' - displays the phone number for the specified contact / displays all saved contacts with phone numbers and birthday.",
                "    <key>: {contact | name} | [all] | note | setting}",
                "'show --setting' - displays all of its current settings."
            ],
#------------------------------------   NoteBook   ---------------------------------
            'add_note': [
                "'add --note <note> [{<tag> | \"<tag1>,...,<tagN>\"]}' - saves a new note."
            ],
            'change_note': [
                "'change --note <tag> [\"<note>\" [{<tag> | \"<tag1>,...,<tagN>\"]}}' - change an existing note."
            ],
            'delete_note': [
                "'delete --note <tag>' - deleting a note by tag."
            ],
            'search_note': [
                "'search --note <mask>' - search for notes by fragment of notes or tags."
            ],
            'show_note': [
                "'show --note [<tag>]' - all notes are displayed if no tag is specified, otherwise only notes containing the specified tag are displayed."
            ],
#------------------------------------   Settings   ---------------------------------
            'set': [
                "'set --<key> <value>' - set the value of the settings key."
                "    <key>: settings keys"
                "        request_details - whether to request in the command mode the missing details of the contact;"
                "        display_birthdays - whether to display, when starting the bot, a list of contacts whose birthday falls within a specified period from the current day;"
                "        number_of_days - number of days from the current day to display the list of contacts whose birthday falls within this period."
                "        language - interface language (en - English, ru - русский, uk - український)"
                "    First, the current value of the key is displayed, then confirmation of the change is requested."
            ],
            'help': [
                "'help' [command] - display command help.",
                "    <key>: bot commands (hello, exit, add, change, delete, search, show, set, help)"
            ],
            'footer': [
                "\n"
                "If the bot is launched with the key and parameters, then it performs the specified operation and exits.",
                "If the request for missing contact details is set in the settings,",
                "then in the process of performing add and change operations, the bot will interactively request the missing details."
            ]
        },
########################################################################################
        'ru': {
            'header': [
                "Это бот-помощник.",
                "Бот реализован в виде консольного приложения.",
                "",
                "Выполняет команды:"
            ],
            'hello': [
                "'hello' - отвечает 'How can I help you?', переходит в интерактивный режим и отображает приглашение '>>'.",
                "    В интерактивный режим бот переходит при запуске вообще без параметров."
            ],
            'exit': [
                "'exit' - в интерактивном режиме выводит 'Good bye!' и завершает свою работу."
            ],
#------------------------------------   AddresssBook   ---------------------------------
            'add': [
                "'add [--<key>] [<Name> [<Phone> | <BirthDay> | <Email> | <Address> | <FullName>]]'",
                "  - сохраняет новый контакт / телефон / день рождения / электронная почта / адрес / полное имя в телефонной книге.",
                "  <key>: {contact | name} | phone | birthday | email | address | fullname}"
            ],
            'change': [
                "'change [--<key>] <Name> [<Phone> | <BirthDay> | <Email> | <Address> | <FullName>]'",
                "    - сохраняет новый номер телефона / день рождения / электронная почта / адрес / полное имя существующего контакта в телефонной книге.",
                "    <key>: phone | birthday | email | address | fullname"
            ],
            'delete': [
                "'delete [--<key>] <Name> | <Phone>' - удаление контакта по имени из телефонной книги или телефона из контакта по имени.",
                "    <key>: {contact | name} | phone"
            ],
            'search': [
                "'search <mask>' - поиск контактов по фрагменту имени / номера телефона / дня рождения / электронной почты / адреса / полнго имени."
            ],
            'show': [
                "'show [--<key>] [<Name>]' - отображает номер телефона, день рождения, электронную почту, адрес, полное имя для указанного контакта",
                "    или отображает все сохраненные контакты со всеми заполненными реквизитами.",
                "    <key>: {contact | name} | [all] | note | setting}",
                "'show --setting' - отображает все текущие настройки."
            ],
#------------------------------------   NoteBook   ---------------------------------
            'add_note': [
                "'add --note <note> [{<tag> | \"<tag1>,...,<tagN>\"]}' - сохраняет новую заметку."
            ],
            'change_note': [
                "'change --note <tag> [\"<note>\" [{<tag> | \"<tag1>,...,<tagN>\"]}}' - изменяет существующую заметку."
            ],
            'delete_note': [
                "'delete --note <tag>' - удаляет заметку по тегу."
            ],
            'search_note': [
                "'search --note <mask>' - сквозной поиск заметок по содержимому и тегам."
            ],
            'show_note': [
                "'show --note [<tag>]' - отображает все заметки, если тег не задан, иначе только заметки с заданным тегом."
            ],
#------------------------------------   Settings   ---------------------------------
            'setting': [
                "'setting --<key> <value>' - установить значение ключа настроек.",
                "    <key>: ключи настроек",
                "        request_details - запрашивать ли в командном режиме недостающие реквизиты контакта;",
                "        display_birthdays - выводить ли при запуске бота список контактов, у которых день рождения попадает в заданный период от текущего дня;",
                "        number_of_days - количество дней от текущего дня для вывода списка контактов, у которых день рождения приходится на этот период.",
                "        language - interface language (en - English, ru - русский, uk - український)",
                "    Сначала выводится текущее значения ключа, затем запрашивается подтверждение изменения."
            ],
            'help': [
                "'help' [command] - отобразить помощь по командам.",
                "    <key>: команды бота (hello, exit, add, change, delete, search, show, set, help)"
            ],
            'footer': [
                "Если бот запускается с ключём и параметрами, то он выполняет заданную операцию и завершает работу.",
                "Если в настройках задан запрос недостающих реквизит контакта,",
                "то в процессе выполнения операций add и change бот в интерактивном режиме запросит недостающие реквизиты."
            ]
        }
    }

    error_text = {
        'en': "Unknown bot command.",
        'ru': "Неизвестная команда бота."
    }

    def view_help(self, command='', language='ru'):
        if language not in self.help_dict:
            language = 'ru'
        lang = self.help_dict.get(language)
        res = ''
        if len(command) == 0:
            for key, help in lang.items():
                # res = res + '\n' + '\n'.join(help) + '\n'
                res = res + '\n'.join(help) + '\n'
        else:
            if command not in lang:
                res = self.error_text.get(language)
                command = 'help'

            help = lang.get(command)
            res = res + '\n' + '\n'.join(help) + '\n'
            # res = res + '\n'.join(help)
        return res

    def view_help_iter(self, language='ru', chunk_size = 20):
        """
        Display the entire address book in chunks of chunk_size entries.

        If chunk_size == None or 0, then all records are displayed in one chunk.
        """
        _index = 0
        _chunk_num = 0
        _chunk_size = chunk_size
        if language not in self.help_dict:
            language = 'ru'
        lang = self.help_dict.get(language)
        res = ''
        try:
            for key, help in lang.items():
                rec = '\n'.join(help) + '\n'
                if len(res) > 0:
                    res = res + '\n' + rec
                else:
                    res = rec
                _index += len(help)
                if (_chunk_size > 0) and (_index // _chunk_size != _chunk_num):
                    yield res
                    _chunk_num += 1
                    res = ''
            if len(res) > 0:
                yield res
        finally:
            return 

##########################################################################################

if __name__ == '__main__':
    bh = Bot_help()
    print (bh.view_help())
    # print (bh.view_help('help','en'))
    # print (bh.view_help('aaa'))
