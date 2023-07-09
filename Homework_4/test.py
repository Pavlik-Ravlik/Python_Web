def do_POST(self):
    filename = 'storage/data.json'
    date = datetime.now()

    data = self.rfile.read(int(self.headers['Content-Length']))
    print(data)

    data_parse = urllib.parse.unquote_plus(data.decode())
    print(data_parse)

    data_dict = {username: message for username, message in [
        el.split('=') for el in data_parse.split('&')]}
    print(data_dict)

    data_dict_date = {str(date): data_dict}

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            existing_data = json.load(file)
        data_dict_date.update(existing_data)

    with open(filename, 'w') as file:
        json.dump(data_dict_date, file, ensure_ascii=False, indent=4)

    self.send_response(302)
    self.send_header('Location', '/')
    self.end_headers()
