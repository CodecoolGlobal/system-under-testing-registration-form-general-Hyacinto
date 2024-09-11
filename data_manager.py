import json
import bcrypt
import os


METADATA = {
    "students": {"file": "student_data.json", "list_key": "students"},
    "users": {"file": "user_data.json", "list_key": "users"}
}
STUDENT_DATA_FILE_PATH = "data.json"
STUDENT_LIST_KEY = "students"
USER_DATA_FILE_PATH = "users.csv"
PASSWORD_KEY = "password"


def init_data():
    for key, value in METADATA.items():
        if not os.path.isfile(value["file"]):
            initial_data = {value["list_key"]: []}
            with open(value["file"], "w") as file:
                json.dump(initial_data, file)


def read_data(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data


def add_data(entity, data):
    if not data:
        raise ValueError("Trying to save empty data")
    if entity not in METADATA:
        raise AttributeError(f"We cannot handle {entity} data, only these: {METADATA.keys()}")
    file_path = METADATA[entity]["file"]
    current_data = read_data(file_path)
    current_data[METADATA[entity]["list_key"]].append(data)
    with open(file_path, "w") as file:
        json.dump(current_data, file)


def read_students():
    file_content = read_data(METADATA["students"]["file"])
    return file_content[METADATA["students"]["list_key"]]


def add_student(data):
    add_data("students", data)


def add_user(user_data):
    hashed_password = encrypt_password(user_data[PASSWORD_KEY])
    user_data.update({PASSWORD_KEY: hashed_password})
    add_data("users", user_data)


def encrypt_password(original_password):
    encoded = original_password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded, salt).decode("utf-8")
    return hashed_password


def check_login(user_data):
    user_metadata = METADATA["users"]
    users = read_data(user_metadata["file"])[user_metadata["list_key"]]
    for user in users:
        if user["username"] == user_data["username"]:
            result = bcrypt.checkpw(user_data["password"].encode("utf-8"), user["password"].encode("utf-8"))
            return result
    return False
