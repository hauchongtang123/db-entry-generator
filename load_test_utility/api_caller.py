import requests
import csv
import time

import config.configuration as config


def main():
    api_config = config.config_api()
    base_url = api_config['base_url']
    # guard clause
    if base_url is None:
        Exception("Unable to call API with no base_url")

    url = f"{base_url}/v1/PromoCode/GetList?Status=1&StartDate=2023-05-24T11:17:33.000&EndDate=2023-06-19T11:17:33" \
          f".000&SortCol=discount_value&SortDir=asc&Page=((page))&Size=((size))&Keyword=OFF"

    data = simulate_pagination(url=url, first_page=1, last_page=10, size=15, stride=1)

    write_to_column_csv(data, col_name='Page=1-10;Size=1', filename='timing_data_1.csv')


def simulate_pagination(url="", first_page=1, last_page=2, size=1, stride=1):
    data = []
    for idx in range(first_page, last_page, stride):
        url = url.replace("((page))", str(idx))
        url = url.replace("((size))", str(size))
        start_time = time.time()
        response: requests.Response = requests.get(url, verify=False)
        end_time = time.time()
        check_response(response=response)
        time_elapsed = end_time - start_time
        data.append(time_elapsed)
    data = list(map(lambda x: str(x), data))
    return data


def check_response(response: requests.Response):
    if response.status_code != 200:
        print(f'Error: Status Code: {response.status_code}')
        ConnectionAbortedError()
    else:
        return None


def write_to_column_csv(data, col_name: str, filename: str):
    with open(file=filename, mode='w') as file:
        writer = csv.writer(file)
        data = [col_name] + data
        # Write data to CSV file
        for item in data:
            writer.writerow([item])


if __name__ == '__main__':
    main()
