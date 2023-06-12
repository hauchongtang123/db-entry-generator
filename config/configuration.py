from configparser import ConfigParser

def config(filename='./env/database.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db

def config_mockaroo(filename='./env/source.ini', section='mockaroo'):
    parser = ConfigParser()
    files = parser.read(filename)

    source = {}
    url = ""
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            if param[0] == 'url':
                url = param[1]
                continue
            source[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return source, url