class Hospital:
    STATUS_CODES = {
        0: "Тяжело болен",
        1: "Болен",
        2: "Слегка болен",
        3: "Готов к выписке"
    }

    def __init__(self):
        self.patients = [1] * 200

    def get_status(self, patient_id):
        try:
            patient_index = self._validate_patient_id(patient_id)
            status_code = self.patients[patient_index]
            return f"Статус пациента {patient_id}: {self.STATUS_CODES.get(status_code, 'Неизвестен')}\n"
        except ValueError as e:
            return f"Ошибка: {e}\n"

    def status_up(self, patient_id):
        try:
            patient_index = self._validate_patient_id(patient_id)
            current_status = self.patients[patient_index]

            if current_status is None:
                return "Пациент уже выписан.\n"

            if current_status == 3:
                response = input("Пациент готов к выписке. Выписать? (да/нет): ").strip().lower()
                if response == 'да':
                    self.patients[patient_index] = None
                    return "Пациент выписан.\n"
                else:
                    return "Статус пациента не изменён.\n"
            else:
                self.patients[patient_index] += 1
                return "Статус пациента повышен.\n"
        except ValueError as e:
            return f"Ошибка: {e}\n"

    def status_down(self, patient_id):
        try:
            patient_index = self._validate_patient_id(patient_id)
            current_status = self.patients[patient_index]

            if current_status is None:
                return "Пациент уже выписан.\n"

            if current_status == 0:
                return "Невозможно понизить статус. Пациент уже в самом низком статусе.\n"
            else:
                self.patients[patient_index] -= 1
                return "Статус пациента понижен.\n"
        except ValueError as e:
            return f"Ошибка: {e}\n"

    def discharge(self, patient_id):
        try:
            patient_index = self._validate_patient_id(patient_id)
            self.patients[patient_index] = None
            return "Пациент выписан.\n"
        except ValueError as e:
            return f"Ошибка: {e}\n"

    def calculate_statistics(self):
        stats = {code: 0 for code in self.STATUS_CODES.keys()}
        stats[None] = 0  # Для выписанных пациентов

        for status in self.patients:
            stats[status] += 1

        result = "Статистика больницы:\n"
        for code, count in stats.items():
            description = self.STATUS_CODES.get(code, "Выписан")
            result += f"{description}: {count}\n"
        return result

    def stop(self):
        return "Работа программы завершена."

    def _validate_patient_id(self, patient_id):
        if not isinstance(patient_id, int) or patient_id <= 0:
            raise ValueError("ID пациента должен быть положительным целым числом.")
        if patient_id > len(self.patients):
            raise ValueError("Пациент с таким ID не существует.")
        return patient_id - 1


def main():
    hospital = Hospital()

    print("Добро пожаловать в систему управления больницей!")

    while True:
        command = input("Введите команду: ").strip().lower()

        if command in ["узнать статус пациента", "get status"]:
            try:
                patient_id = int(input("Введите ID пациента: "))
                print(hospital.get_status(patient_id))
            except ValueError:
                print("ID пациента должен быть целым числом.\n")

        elif command in ["повысить статус пациента", "status up"]:
            try:
                patient_id = int(input("Введите ID пациента: "))
                print(hospital.status_up(patient_id))
            except ValueError:
                print("ID пациента должен быть целым числом.\n")

        elif command in ["понизить статус пациента", "status down"]:
            try:
                patient_id = int(input("Введите ID пациента: "))
                print(hospital.status_down(patient_id))
            except ValueError:
                print("ID пациента должен быть целым числом.\n")

        elif command in ["выписать пациента", "discharge"]:
            try:
                patient_id = int(input("Введите ID пациента: "))
                print(hospital.discharge(patient_id))
            except ValueError:
                print("ID пациента должен быть целым числом.\n")

        elif command in ["рассчитать статистику", "calculate statistics"]:
            print(hospital.calculate_statistics())

        elif command in ["стоп", "stop"]:
            print(hospital.stop())
            break

        else:
            print("Неизвестная команда. Попробуйте снова.\n")


if __name__ == "__main__":
    main()
