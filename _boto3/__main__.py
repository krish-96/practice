import atexit
import getpass

print('Main module')


def close_the_resources():
    print('Close the resources...!')


atexit.register(close_the_resources)


def main():
    print("From %s" % __name__)
    while True:
        print(f'{"*" * 90}\nPress CTRL + C to exit\n{"*" * 90}')
        services_list = ['s3', 'ec2', 'SQS', 'Lambda', 'RDS', 'VPC', 'SubNet', 'IGW-InternetGateWay']
        for index, service in enumerate(services_list):
            print("[%d] %s" % (index + 1, service))
        # option = int(input("Please Choose an option: "))
        option = int(getpass.getpass("Please Choose an option: "))
        if option <= len(services_list):
            print("Valid option")
        else:
            print('\n', '-' * 90)
            print('Invalid option!!')
            continue
        is_confirmed = input("You have chosen the option :%s \n Please confirm (Y/N): " % services_list[option - 1])
        if is_confirmed not in ('Y', 'y'):
            print("You can select the correct option!")
            continue
        print("The right option you chosen is :%s" % (services_list[option - 1]))


if __name__ == '__main__':
    main()
