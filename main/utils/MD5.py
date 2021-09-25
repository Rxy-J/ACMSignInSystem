import hashlib

def getMD5(info) -> str:
    if type(info) != str:
        info = str(info)
    tool = hashlib.md5()
    tool.update(info.encode(encoding="UTF-8"))
    return tool.hexdigest() 


if __name__ == "__main__":
    print(getMD5("asdf"))