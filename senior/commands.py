# commands.py
from models import Hospital

class HospitalCommands:
    def __init__(self, hospital):
        self.hospital = hospital

    def get_status(self, patient_id):
        index = self.hospital.validate_patient_id(patient_id)
        if self.hospital.patients[index] is None:
            raise ValueError(f"Пациент {patient_id} выписан.")
        status = self.hospital.patients[index]
        return self.hospital.STATUS_MAP.get(status, 'Неизвестен')

    def status_up(self, patient_id):
        index = self.hospital.validate_patient_id(patient_id)
        if self.hospital.patients[index] is None:
            raise ValueError(f"Пациент {patient_id} уже выписан.")

        if self.hospital.patients[index] == 3:
            return "ready_to_discharge"
        else:
            self.hospital.patients[index] += 1
            return self.hospital.STATUS_MAP[self.hospital.patients[index]]

    def status_down(self, patient_id):
        index = self.hospital.validate_patient_id(patient_id)
        if self.hospital.patients[index] is None:
            raise ValueError(f"Пациент {patient_id} уже выписан.")

        if self.hospital.patients[index] == 0:
            raise ValueError(f"Пациент {patient_id} уже имеет минимальный статус 'Тяжело болен'.")
        
        # Уменьшаем статус только если не минимальный
        self.hospital.patients[index] -= 1
        return self.hospital.STATUS_MAP[self.hospital.patients[index]]


    def discharge(self, patient_id):
        index = self.hospital.validate_patient_id(patient_id)
        self.hospital.patients[index] = None
        return f"Пациент {patient_id} выписан."

    def calculate_statistics(self):
        stats = {"Выписан": 0}
        for status in self.hospital.STATUS_MAP.values():
            stats[status] = 0

        for patient in self.hospital.patients:
            if patient is None:
                stats["Выписан"] += 1
            else:
                stats[self.hospital.STATUS_MAP[patient]] += 1

        return stats