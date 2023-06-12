from config.configuration import config_mockaroo
from logic.execute import execute_repeat
from logic.insert_from_external_source import get_from_mockaroo

def main():
    params, url = config_mockaroo()
    _, sql_script = get_from_mockaroo(url, params)
    execute_repeat(query=sql_script, times=300)

if __name__ == '__main__':
    main()