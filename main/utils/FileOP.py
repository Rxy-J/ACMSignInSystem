import os

from DK.settings import BASE_DIR

TEMP_PATH = os.path.join(BASE_DIR, "main/temp")
if not os.path.exists(TEMP_PATH):
    os.makedirs(TEMP_PATH)

def setTemp(path: str):
    file = os.path.split(path)[-1]
    return os.path.join(TEMP_PATH, file)

def removeFile(path: str):
    if os.path.isfile(path):
        os.remove(path)
    else:
        raise Exception("要删除的路径不是文件")