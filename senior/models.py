# models.py

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
            raise ValueError("Введите корректный положительный номер ID пациента.")