from config.configuration import config_mockaroo
from logic.execute import execute_repeat
from logic.insert_from_external_source import get_from_mockaroo


def main():
    params, url = config_mockaroo()
    _, sql_script = get_from_mockaroo(url, params)

    try:
        thousand_times = int(input("How many thousand rows to insert into DB ?"))
        execute_repeat(query=sql_script, thousand_times=thousand_times)
    except:
        execute_repeat(query=sql_script)
        print("Executing default: 1 thousand rows")


if __name__ == '__main__':
    main()
