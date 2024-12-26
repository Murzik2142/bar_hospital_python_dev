from models import Hospital

class HospitalCommands:
    def __init__(self, hospital):
        self.hospital = hospital

    def get_status(self, patient_id):
        index = self.hospital.validate_patient_id(patient_id)
        if index is not None:
            status = self.hospital.patients[index]
            print(f"Статус пациента {patient_id}: {self.hospital.STATUS_MAP.get(status, 'Неизвестен')}")

    def status_up(self, patient_id):
        index = self.hospital.validate_patient_id(patient_id)
        if index is not None:
            if self.hospital.patients[index] is None:
                print(f"Пациент {patient_id} уже выписан.")
                return

            if self.hospital.patients[index] == 3:
                confirm = input("Пациент готов к выписке. Выписать? (да/нет): ").strip().lower()
                if confirm in ["да", "yes"]:
                    self.hospital.patients[index] = None
                    print(f"Пациент {patient_id} выписан.")
                else:
                    print(f"Пациент {patient_id} остаётся в статусе 'Готов к выписке'.")
            else:
                self.hospital.patients[index] += 1
                print(f"Статус пациента {patient_id} повышен до '{self.hospital.STATUS_MAP[self.hospital.patients[index]]}'.")

    def status_down(self, patient_id):
        index = self.hospital.validate_patient_id(patient_id)
        if index is not None:
            if self.hospital.patients[index] is None:
                print(f"Пациент {patient_id} уже выписан.")
                return

            if self.hospital.patients[index] == 0:
                print(f"Ошибка: Пациент {patient_id} уже имеет минимальный статус 'Тяжело болен'.")
            else:
                self.hospital.patients[index] -= 1
                print(f"Статус пациента {patient_id} понижен до '{self.hospital.STATUS_MAP[self.hospital.patients[index]]}'.")

    def discharge(self, patient_id):
        index = self.hospital.validate_patient_id(patient_id)
        if index is not None:
            self.hospital.patients[index] = None
            print(f"Пациент {patient_id} выписан.")

    def calculate_statistics(self):
        stats = {"Выписан": 0}
        for status in self.hospital.STATUS_MAP.values():
            stats[status] = 0

        for patient in self.hospital.patients:
            if patient is None:
                stats["Выписан"] += 1
            else:
                stats[self.hospital.STATUS_MAP[patient]] += 1

        print("Статистика больницы:")
        for status, count in stats.items():
            print(f"  {status}: {count}")

    def stop(self):
        print("Работа завершена.")
        exit()