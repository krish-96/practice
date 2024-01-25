"""
Inspect module will be helpful if you are trying to inspect the code through code

It also provides information about the stack and trace information.
Stack will be useful to get the information like
- From where the function was called/Who's the caller
- line number
- filename
-index
etc...

"""
import inspect
import os
import time

import apscheduler_

if inspection := inspect.stack()[0]:
    print(f"{'*' * 30} : From Module : baseLevel {'*' * 30}")
    print(inspection.function)
    print(inspection.lineno)
    print(inspection.filename)
    print(os.path.basename(inspection.filename))
    # print(f"{'*' * 90}")


def main():
    print(f"==>  From main function")
    if inspection := inspect.stack()[1]:
        print(f"{'*' * 30} : From Function : firstLevel {'*' * 20}")
        print(inspection.function)
        print(inspection.lineno)
        print(inspection.filename)
        print(os.path.basename(inspection.filename))
    # print(f"{'*' * 90}")


class MainClass():
    def inscpect(self):
        if inspection := inspect.stack()[1]:
            print(f"{'*' * 30} : From Class - Method : secondLevel {'*' * 10}")
            print(inspection.function)
            print(inspection.lineno)
            print(inspection.filename)
            print(os.path.basename(inspection.filename))
            print(f"{'*' * 90}")

    apscheduler_.start_scheduler()
    count = 0
    while True:
        count += 1
        time.sleep(5)
        print(f"count : {count}")


if __name__ == '__main__':

    main()
    MainClass().inscpect()
