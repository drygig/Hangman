
def check_email(string):
    if (" " not in string) and ("@" in string) and ("@." not in string) and ("." in string):
        print("tak")
        return True
    else:
        print("nie")
        return False

check_email("natalia.dry gas06@gmail.com")