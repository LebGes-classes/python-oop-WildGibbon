class Ship:
    """
    Данный класс описывает корабль.
    """

    def __init__(self, name = "default", displacement = 1, current_location = "RUSSIA"):
        """
        Инициализация корабля

        Args:
            name: Имя корабля
            displacement: Водоизмещение
            current_location: Текущая локация

        """

        self._current_location = current_location
        self._displacement = displacement
        self._name = name

    def get_name(self):
        return self._name

    def get_displacement(self):
        return self._displacement

    def set_name(self, name):
        """
        Задает имя, если строка пустая, то имени присваивается значение по умолчанию

        Args:
            name: Имя
        """

        if name != "":
            self._name = name
        else:
            self._name = "default"

    def set_displacement(self, displacement):
        """
        Задает водоизмещение, если указано ненатуральное значение, то значение не присваивается

        Args:
            displacement: водоизмещение
        """

        if displacement <= 0:
            print("Invalid displacement, should be positive")
        else:
            self._displacement = displacement

    def view(self):
        """
        Выводит состояние корабля в консоль
        """

        print(f"Имя: {self._name}")
        print(f"Локация: {self._current_location}")
        print(f"Водоизмещение: {self._displacement}")

    def upgrade_displacement(self, upgrade_number):
        """
        Улучшает водоизмещение на заданное значение, если значение отрицательное, то не улучшает

        Args:
            upgrade_number: Число улучшения водоизмещения
        """

        if upgrade_number >= 0:
            self._displacement += upgrade_number
        else:
            print("Invalid upgrade, should be positive")

    def sail_into_some_place(self, place_name):
        """
        Меняет локацию корабля на заданную

        Args:
            place_name: Место, куда корабль приплывает
        """

        self._current_location = place_name
        print(f"Вы приплыли в {place_name}")


class ShipsControlMenu:
    """
    Данный класс считывает действия пользователя, а затем передает их кораблям
    """

    def __init__(self, ships_list):
        """
        Инициализация меню

        Args:
            ships_list: Корабли, контролируемые меню
        """

        self._ships = ships_list
        self._menu_opened = False

    def open(self):
        """
        Запускает цикл работы меню
        """

        self._menu_opened = True
        while self._menu_opened:
            print("Введите номер корабля для управления им(нумерация с нуля): ")

            selected_ship = self.__get_list_index_input(self._ships)
            self._ships[selected_ship].view()
            self.__do_command(input("Введите команду для работы с кораблем: \n"), selected_ship)

            print()

    # делать статическим? сделал универсальным кстати
    def __get_list_index_input(self, selection_list):
        """
        Считывает введенный пользователем индекс элемента заданного списка, до тех пор пока ввод не будет корректным,
        затем возвращает этот индекс

        Args:
            selection_list: Оперируемый список

        Returns:
            Введенный пользователем индекс
        """

        input_num = input()

        while input_num not in "0123456789" or (len(selection_list) - 1 < int(input_num) < 0):
            print("Неправильно набран номер")

            input_num = input()

        return int(input_num)

    def __do_command(self, command, ship_number):
        """
        Применяет заданную команду к заданному кораблю

        Args:
             command: Команда
             ship_number: Корабль, к которому применяется команда
        """

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