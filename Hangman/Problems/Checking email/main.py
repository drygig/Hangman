def check_email(string):
    if " " in string:
        return False
    elif "@" not in string:
        return False
    elif "@." in string:
        return False
    elif "." not in string[string.find("@"):]:
        return False
    else:
        return True
