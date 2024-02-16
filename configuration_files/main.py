"""
Section should have key and values
"""

import configparser

config = configparser.ConfigParser()
filename = 'info.ini'


def update_file(new_config):
    with open('example.ini', 'w') as configfile:
        new_config.write(configfile)


def get_sections_info():
    config.read(filename)
    print("Available Sections : ")
    for index, section in enumerate(config.sections()):
        print("[%2d] - %s" % (index + 1, section))
    return config.sections()


def get_section_info(section):
    config.read(filename)
    if section in config.sections():
        return config[section]
    else:
        print("Given section %s is not available" % section)
        return None


def get_section_key_info(section, key):
    print(f"section : {section}, key: {key}")
    config.read(filename)
    if config.has_section(section):
        if config.has_option(section, key):
            return config.get(section, key)
        else:
            print("Given key %s is not available" % key)
    else:
        print("Given section %s is not available" % section)
        return None


def read():
    sections = get_sections_info()

    def validate_section(section_index):
        return int(section_index) - 1 < len(sections)

    while True:
        print("*" * 100)
        print("%30s %30s %30s " % ("[D] Display the sections",
                                   "[SS] Select the Section",
                                   "[SK] Select the Section Key"))
        print("*" * 100)
        selected_option = input("Enter your option :")
        selected_option = selected_option.lower()
        if selected_option == 'd':
            get_sections_info()
        elif selected_option == 'ss':
            selected_section = input("Select the section :")
            if validate_section(selected_section):
                section_data = get_section_info(sections[int(selected_section) - 1])
                print(section_data)
                for sk, sv in section_data.items():
                    print(sk, sv)
            else:
                print('Invalid Section!')
        elif selected_option == 'sk':
            selected_section = input("Select the section :")
            selected_key = input("Select the key :")
            if validate_section(selected_section):
                key_section_info = get_section_key_info(sections[int(selected_section) - 1], selected_key)
                print(key_section_info)
                new_value = input("If you wish to change, Enter the new value : ")
                if new_value:
                    config.set(sections[int(selected_section) - 1], selected_key, new_value)
                    update_file(config)
            else:
                print('Invalid Section! Please select valid one.')

        else:
            print('Invalid option!')


def write():
    dict_data = {}
    for i in range(1, 16):
        dict_data.update({f"test-{i}": {j: f'This is test {i}-{j}' for j in range(1, 6)}})

    for key, value in dict_data.items():
        if isinstance(value, dict):
            config[key] = value

    with open("info.ini", 'w') as confile:
        config.write(confile)
    print(f"{'-' * 50}\nData written to file succesfully!\n{'-' * 50}")


def main():
    while True:
        print("*" * 100)
        print("Choose an option : %25s %25s %25s" % ("[E] Exit",
                                                     "[W] Write",
                                                     "[R] Read"))
        print("*" * 100)
        option = input(">> : ")
        option = option.lower()
        if option == 'e':
            exit(0)
        elif option.startswith('r'):
            read()
        elif option.startswith('w'):
            write()
        else:
            print("Invalid Option!")


if __name__ == '__main__':
    main()
