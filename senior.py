class Hospital:
    STATUS_MAP = {
        0: "Тяжело болен",
        1: "Болен",
        2: "Слегка болен",
        3: "Готов к выписке"
    }

    def __init__(self, num_patients=200):
        self.patients = [1] * num_patients

    def validate_patient_id(self, patient_id):
        try:
            patient_id = int(patient_id)
            if patient_id < 1 or patient_id > len(self.patients):
                raise ValueError("ID не существует.")
            return patient_id - 1
        except ValueError:
            print("Ошибка: Введите корректный положительный номер ID пациента.")
            return None

    def get_status(self, patient_id):
        index = self.validate_patient_id(patient_id)
        if index is not None:
            status = self.patients[index]
            print(f"Статус пациента {patient_id}: {self.STATUS_MAP.get(status, 'Неизвестен')}")

    def status_up(self, patient_id):
        index = self.validate_patient_id(patient_id)
        if index is not None:
            if self.patients[index] is None:
                print(f"Пациент {patient_id} уже выписан.")
                return

            if self.patients[index] == 3:
                confirm = input("Пациент готов к выписке. Выписать? (да/нет): ").strip().lower()
                if confirm in ["да", "yes"]:
                    self.patients[index] = None
                    print(f"Пациент {patient_id} выписан.")
                else:
                    print(f"Пациент {patient_id} остаётся в статусе 'Готов к выписке'.")
            else:
                self.patients[index] += 1
                print(f"Статус пациента {patient_id} повышен до '{self.STATUS_MAP[self.patients[index]]}'.")

    def status_down(self, patient_id):
        index = self.validate_patient_id(patient_id)
        if index is not None:
            if self.patients[index] is None:
                print(f"Пациент {patient_id} уже выписан.")
                return

            if self.patients[index] == 0:
                print(f"Ошибка: Пациент {patient_id} уже имеет минимальный статус 'Тяжело болен'.")
            else:
                self.patients[index] -= 1
                print(f"Статус пациента {patient_id} понижен до '{self.STATUS_MAP[self.patients[index]]}'.")

    def discharge(self, patient_id):
        index = self.validate_patient_id(patient_id)
        if index is not None:
            self.patients[index] = None
            print(f"Пациент {patient_id} выписан.")

    def calculate_statistics(self):
        stats = {"Выписан": 0}
        for status in self.STATUS_MAP.values():
            stats[status] = 0

        for patient in self.patients:
            if patient is None:
                stats["Выписан"] += 1
            else:
                stats[self.STATUS_MAP[patient]] += 1

        print("Статистика больницы:")
        for status, count in stats.items():
            print(f"  {status}: {count}")

    def stop(self):
        print("Работа завершена.")
        exit()


def main():
    hospital = Hospital()
    commands = {
        "узнать статус пациента": hospital.get_status,
        "get status": hospital.get_status,
        "повысить статус пациента": hospital.status_up,
        "status up": hospital.status_up,
        "понизить статус пациента": hospital.status_down,
        "status down": hospital.status_down,
        "выписать пациента": hospital.discharge,
        "discharge": hospital.discharge,
        "рассчитать статистику": hospital.calculate_statistics,
        "calculate statistics": hospital.calculate_statistics,
        "стоп": hospital.stop,
        "stop": hospital.stop
    }

    print("Добро пожаловать в систему автоматизации больницы.")
    while True:
        command = input("Введите команду: ").strip().lower()
        if command in commands:
            if command in ["узнать статус пациента", "get status", "повысить статус пациента", "status up", "понизить статус пациента", "status down", "выписать пациента", "discharge"]:
                patient_id = input("Введите ID пациента: ")
                commands[command](patient_id)
            else:
                commands[command]()
        else:
            print("Ошибка: Неизвестная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()