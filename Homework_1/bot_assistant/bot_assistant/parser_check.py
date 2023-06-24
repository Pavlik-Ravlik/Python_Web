import difflib


def closest_command(input_string, command_list):
    if input_string.lower() not in command_list:
        suggestion = difflib.get_close_matches(input_string, command_list, n=2, cutoff=0.55)
        res = f'Невідома команда "{input_string}".'
        if suggestion:
            res = res + f" Можливо ви мали на увазі: {', '.join(suggestion)}."
        return res

