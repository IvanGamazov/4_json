import json
from pprint import pprint


def load_data(filepath):
    with open(filepath) as data_file:
        return json.load(data_file)


def pretty_print_json(data):
    print(json.dumps(data, indent=4))


def main():
    filepath = input("Enter file path --> ")
    data = load_data(filepath)
    pprint("Our readable JSON-file:")
    pretty_print_json(data)

if __name__ == '__main__':
    main()
