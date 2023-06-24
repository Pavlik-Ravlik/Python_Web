class Bot_setting:
    request_details = 1  # запрашивать ли в командном режиме недостающие реквизиты контакта;
    display_birthdays = 0  # выводить ли при запуске бота список контактов, у которых день рождения попадает в заданный период от текущего дня;
    number_of_days = 7  # количество дней от текущего дня для вывода списка контактов, у которых день рождения приходится на этот период.
    display_lines = 10  # количество отображаемых строк в одной порции вывода списка контактов или заметок
    language = "ru" # язык интерфейса (en - English, ru - русский, uk - український)

    setting_lang = {}
    errors = ''

    def get_request_details(self):
        return str(self.request_details)

    def get_display_birthdays(self):
        return str(self.display_birthdays)

    def get_number_of_days(self):
        return str(self.number_of_days)

    def get_display_lines(self):
        return str(self.display_lines)

    def get_language(self):
        return self.language

    setting_dict = {
        'en': {
            'header': [
                "Bot settins.",
                '',
                None
            ],
            'request_details': [
                "Whether to request missing contact details in command mode.",
                get_request_details
            ],
            'display_birthdays': [
                "Should the bot launch a list of contacts whose birthday falls within a specified period from the current day.",
                get_display_birthdays
            ],
            'number_of_days': [
                "Number of days from the current day to display a list of contacts whose birthday falls within this period.",
                get_number_of_days
            ],
            'display_lines': [
                "The number of rows to display in one portion of the output list of contacts or notes.",
                get_display_lines
            ],
            'language': [
                "Interface language (en - English, ru - Russian, uk - Ukrainian).",
                get_language
            ]
        },
        'ru': {
            'header': [
                "Настройки бота.",
                '',
                None
            ],
            'request_details': [
                "Запрашивать ли в командном режиме недостающие реквизиты контакта.",
                get_request_details
            ],
            'display_birthdays': [
                "Выводить ли при запуске бота список контактов, у которых день рождения попадает в заданный период от текущего дня.",
                get_display_birthdays
            ],
            'number_of_days': [
                "Количество дней от текущего дня для вывода списка контактов, у которых день рождения приходится на этот период.",
                get_number_of_days
            ],
            'display_lines': [
                "Количество отображаемых строк в одной порции вывода списка контактов или заметок.",
                get_display_lines
            ],
            'language': [
                "Язык интерфейса (en - English, ru - русский, uk - український).",
                get_language
            ]
        },
        'uk': {
            'header': [
                "Налаштування боту.",
                None
            ],
            'request_details': [
                "Чи вимагати в командному режимі реквізити контакту, якого не вистачає.",
                get_request_details
            ],
            'display_birthdays': [
                "Чи виводити при запуску бота список контактів, у яких день народження потрапляє у заданий період від поточного дня.",
                get_display_birthdays
            ],
            'number_of_days': [
                "Кількість днів від поточного дня для виведення списку контактів, у яких день народження припадає на цей період.",
                get_number_of_days
            ],
            'display_lines': [
                "Кількість рядків, що відображаються в одній порції виведення списку контактів або нотаток.",
                get_display_lines
            ],
            'language': [
                "Мова інтерфейсу (en - English, ru - російська, uk - українська).",
                get_language
            ]
        }
    }

    error_dict = {
        'en': "Invalid value '{value}' for setting '{key}'",
        'ru': "Недопустимое значение '{value}' для настройки '{key}'",
        'uk': "Неприпустиме значення '{value}' для налаштування '{key}'"
    }
    def __init__(self):
        self.init_language()

    def init_language(self):
        self.setting_lang = self.setting_dict.get(self.language)
        self.errors = self.error_dict.get(self.language)

    def set_request_details(self, value):
        if value not in ['0', '1']:
            raise Exception(self._errors.replace('{value}', value).replace('{key}', 'request_details'))
        self.request_details = int(value)

    def set_display_birthdays(self, value):
        if value not in ['0', '1']:
            raise Exception(self._errors.replace('{value}', value).replace('{key}', 'display_birthdays'))
        self.display_birthdays = int(value)

    def set_number_of_days(self, value):
        if not str(value).isdecimal() or int(value) < 0 or int(value) > 365:
            raise Exception(self._errors.replace('{value}', value).replace('{key}', 'number_of_days'))
        self.number_of_days = int(value)

    def set_display_lines(self, value):
        if not str(value).isdecimal() or int(value) < 0 or int(value) > 50:
            raise Exception(self._errors.replace('{value}', value).replace('{key}', 'display_lines'))
        self.display_lines = int(value)

    def set_language(self, value):
        # if value not in ['en', 'ru', 'uk']:
        if value not in self.error_dict:
            raise Exception(self._errors.replace('{value}', value).replace('{key}', 'language'))
        self.language = value
        self.init_language()

    def view_setting(self, key=''):
        if key:
            lst = self.setting_lang.get(key)
            val = lst[1](self)
            res = key + ' = ' + val + '  - ' + lst[0]
        else:
            res = ''
            sep = '--------------------------------------------------'
            for key, lst in self.setting_lang.items():
                if key == 'header':
                    res = lst[0] +'\n' + sep + '\n'
                else:
                    val = lst[1](self)
                    res = res + key + ' = ' + val + '  - ' + lst[0] +'\n'
            res = res + sep
        return res

    def __repr__(self):
        return self.view_setting()

if __name__ == '__main__':
    bh = Bot_setting()
    # print (bh.setting_dict.get('en').get('request_details'))
    # print (bh.setting_dict.get('en').get('request_details')[1])
    print(bh)
    # print(bh.view_setting('request_details'))
    # bh.set_language('aa')
    bh.set_language('uk')
    print(bh.view_setting('request_details'))
    bh.set_language('en')
    print(bh.view_setting('request_details'))
