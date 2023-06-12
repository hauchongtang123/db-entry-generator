import requests

def get_from_mockaroo(source, params):
    # Make request to Mockaroo endpoint
    response = requests.get(url=source, params=params)
    sql_script = ""
    if response.status_code == 200:
        sql_script = response.content.decode()
        print("Generated SQL file downloaded successfully!")
    else:
        print("Error downloading SQL file")
        ConnectionAbortedError()

    if sql_script == "":
        EOFError()
    print("Successfully retrieved script!")
    return response, sql_script