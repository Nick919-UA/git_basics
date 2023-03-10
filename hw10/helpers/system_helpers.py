import json


def get_file_data(path):
    file = open(path, "r")
    data_list = json.loads(file.read())
    file.close()
    return data_list


def save_list_to_file(data, path):
    file = open(path, "w")
    data_in_json = json.dumps(data)
    file.write(data_in_json)
    file.close()


def save_to_file(data: dict, path: str):
    data_list = get_file_data(path)
    if len(data_list) < 1:
        data["id"] = 1
    else:
        data["id"] = len(data_list) + 1
    data_list.append(data)
    save_list_to_file(data_list, path)
