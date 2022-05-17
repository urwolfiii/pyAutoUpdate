import json, os, zipfile, shutil
from urllib.request import urlretrieve

global setting


class settings:  # this is the class that will be used to store the settings
    def __init__(self, path) -> None:
        self.path = path
        with open(self.path, "r") as f:
            self.data = json.load(f)
        self.server = self.data["server"]
        self.port = self.data["port"]
        self.version = self.data["version"]
        self.tree = self.data["tree"]
        return


def get_config(path: str = "auto_update.json"):
    global setting
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"File {path} not found, try to create it or change the path"
        )
    setting = settings(path)


def get_update_info() -> None:  # Gets the version from the server and saves it to a file so it can be checked later. (This is done so the user doesn't have to wait for the update to be downloaded every time they run the program instead it will be downloaded once and then the user can just run the program again, in the install_update function, the version will be checked and if it is different it will download the update and replace the old one.)
    global setting
    url = f"{setting.server}:{setting.port}/get_update_info/{setting.tree}"
    urlretrieve(url, "auto_update_version.txt")
    return


def backup_files() -> bool:
    if not os.path.exists("./backup"):
        os.makedirs("./backup")
    try:
        for i in os.listdir():
            shutil.copy(i, "./backup")
        return True
    except PermissionError:
        return False


def install_update() -> None:  # Actual update, checks if the version installed is the newest version available if not it will download the newest version and unzip it so it can replace the old one.
    global setting
    with open("auto_update_version.txt", "r") as f:
        new_version = f.read()
        if not new_version == setting.version:
            print(f"Update available, version: {new_version}")
        else:
            return
    backup_files()
    urlretrieve(
        f"{setting.server}:{setting.port}/install_update/{setting.tree}", "update.zip"
    )
    if not os.path.exists("temp"):
        os.mkdir("temp")
    with zipfile.ZipFile("update.zip") as z:
        z.extractall("temp")
    setting.data["version"] = new_version
    with open(setting.path, "w") as f:
        json.dump(setting.data, f)
    root = "./"
    for filename in os.listdir(os.path.join(root, "temp")):
        shutil.move(os.path.join(root, "temp", filename), os.path.join(root, filename))
    os.remove("update.zip")
    return


def full_update(
    path: str = "auto_update.json", start_command="py .\_main.py", backup=True, version="stable"
) -> None:  # This is the same as install_update + get_update_info just in one function it also starts a Program after updating.
    global settings
    get_config(path)
    if version != "stable":
        setting.tree = version
    get_update_info()
    install_update()
    try:
        with open() as f:
            x = f.read()
        if not setting.version == x:
            os.system(start_command)
    except:
        pass
    return


full_update()
