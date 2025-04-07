def error():
    try:
        raise Exception("error1")
    except KeyError as ex:
        raise Exception("error2") from ex
error()