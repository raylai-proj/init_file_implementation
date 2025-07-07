from init_file_implementation import string_func


def main():
    string = "test __init__"
    print(f"string length is {string_func.get_length(string)}.")
    print(f"string uppercase is {string_func.get_upper(string)}")
    print(f"string lowercase is {string_func.get_lower(string)}")


if __name__ == "__main__":
    main()
