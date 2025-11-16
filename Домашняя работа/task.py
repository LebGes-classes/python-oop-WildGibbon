from tkinter import Menu


class Ship:
    def __init__(self, name = "default", displacement = 1, current_location = "RUSSIA"):
        self._current_location = current_location
        self._displacement = displacement
        self._name = name

    def get_name(self):
        return self._name

    def get_displacement(self):
        return self._displacement

    def set_name(self, name):
        if name != "":
            self._name = name
        else:
            self._name = "default"

    def set_displacement(self, displacement):
        if displacement <= 0:
            print("Invalid displacement, should be positive")
        else:
            self._displacement = displacement

    def view(self):
        print(f"Имя: {self._name}")
        print(f"Локация: {self._current_location}")
        print(f"Водоизмещение: {self._displacement}")

    def upgrade_displacement(self, upgrade_number):
        if upgrade_number >= 0:
            self._displacement += upgrade_number
        else:
            print("Invalid upgrade, should be positive")

    def sail_into_some_place(self, place_name):
        self._current_location = place_name
        print(f"Вы приплыли в {place_name}")


class ShipsControlMenu:
    def __init__(self, ships_list):
        self._ships = ships_list
        self._menu_opened = False

    def open(self):
        self._menu_opened = True
        while self._menu_opened:
            selected_ship = self.__get_ship_number_input()
            self._ships[selected_ship].view()
            self.__do_command(input("Введите команду для работы с кораблем: \n"), selected_ship)

            print()

    def __get_ship_number_input(self):
        input_num = int(input("Введите номер корабля для управления им(нумерация с нуля): "))

        while input_num < 0 or input_num > len(self._ships) - 1:
            print("Неправильно набран номер")

            input_num = int(input("Введите номер корабля для управления им: "))

        return input_num

    def __do_command(self, command, ship_number):
        match command:
            case "sail":
                self._ships[ship_number].sail_into_some_place(input("Введите локацию, куда вы хотите приплыть: "))
            case "upgrade":
                self._ships[ship_number].upgrade_displacement(
                    int(input("Введите количество, на которое требуется улучшить водоизмещение: ")))
            case "rename":
                self._ships[ship_number].set_name(input("Введите новое имя корабля: "))
            case "exit":
                self._menu_opened = False

class Main:
    def __init__(self):
        ship1 = Ship("DODSTER", 100500, "MYXINO")
        ship2 = Ship("TURBODOG", 15, "NEW YORK")
        menu = ShipsControlMenu([ship1, ship2])
        menu.open()

Main()