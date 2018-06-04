from Xlib import display
import os


def beep(x):
    os.system("echo -n '\a';sleep 0.2;" * x)


def main():
    while True:
        data = display.Display().screen().root.query_pointer()._data
        if data["root_x"] == 0 and data["root_y"] == 0:
            beep(1)
        # print(f'{data["root_x"]} - {data["root_y"]}')


if __name__ == '__main__':
    main()
