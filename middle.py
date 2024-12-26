class Hospital:
    STATUS_MAP = {
        0: "Тяжело болен",
        1: "Болен",
        2: "Слегка болен",
        3: "Готов к выписке"
    }

    def __init__(self, patient_count=200):
        self.patients = [1] * patient_count  # Все пациенты начинают в статусе "Болен"

    def validate_patient_id(self, patient_id):
        if not isinstance(patient_id, int) or patient_id < 1 or patient_id > len(self.patients):
            raise ValueError(f"Некорректный ID пациента: {patient_id}")
        return patient_id - 1  # Индексы начинаются с 0

    def get_status(self, patient_id):
        patient_index = self.validate_patient_id(patient_id)
        status = self.patients[patient_index]
        return "Пациент выписан" if status is None else self.STATUS_MAP[status]

    def status_up(self, patient_id):
        patient_index = self.validate_patient_id(patient_id)
        current_status = self.patients[patient_index]

        if current_status is None:
            return "Пациент уже выписан."

        if current_status == max(self.STATUS_MAP):
            confirmation = input("Пациент уже в максимальном статусе. Выписать? (да/нет): ").strip().lower()
            if confirmation in ["да", "yes"]:
                self.patients[patient_index] = None
                return "Пациент выписан."
            return "Статус пациента остался неизменным."

        self.patients[patient_index] += 1
        return f"Статус пациента повышен: {self.STATUS_MAP[self.patients[patient_index]]}"

    def status_down(self, patient_id):
        patient_index = self.validate_patient_id(patient_id)
        current_status = self.patients[patient_index]

        if current_status is None:
            return "Пациент уже выписан."

        if current_status == min(self.STATUS_MAP):
            return "Ошибка: Статус пациента не может быть ниже минимального."

        self.patients[patient_index] -= 1
        return f"Статус пациента понижен: {self.STATUS_MAP[self.patients[patient_index]]}"

    def discharge(self, patient_id):
        patient_index = self.validate_patient_id(patient_id)
        self.patients[patient_index] = None
        return "Пациент выписан."

    def calculate_statistics(self):
        stats = {status: 0 for status in self.STATUS_MAP.values()}
        stats["Выписаны"] = 0

        for status in self.patients:
            if status is None:
                stats["Выписаны"] += 1
            else:
                stats[self.STATUS_MAP[status]] += 1

        return stats

    def print_statistics(self):
        stats = self.calculate_statistics()
        print("Статистика больницы:")
        for status, count in stats.items():
            print(f"{status}: {count}")


def main():
    hospital = Hospital()

    while True:
        command = input("Введите команду: ").strip().lower()

        if command in ["стоп", "stop"]:
            print("Работа программы завершена.")
            break

        try:
            if command in ["узнать статус пациента", "get status"]:
                patient_id = int(input("Введите ID пациента: "))
                print(hospital.get_status(patient_id))

            elif command in ["повысить статус пациента", "status up"]:
                patient_id = int(input("Введите ID пациента: "))
                print(hospital.status_up(patient_id))

            elif command in ["понизить статус пациента", "status down"]:
                patient_id = int(input("Введите ID пациента: "))
                print(hospital.status_down(patient_id))

            elif command in ["выписать пациента", "discharge"]:
                patient_id = int(input("Введите ID пациента: "))
                print(hospital.discharge(patient_id))

            elif command in ["рассчитать статистику", "calculate statistics"]:
                hospital.print_statistics()

            else:
                print("Неизвестная команда. Попробуйте снова.")

        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
