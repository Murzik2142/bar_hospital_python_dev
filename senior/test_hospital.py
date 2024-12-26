import unittest
from models import Hospital
from commands import HospitalCommands

class TestHospital(unittest.TestCase):

    def setUp(self):
        self.hospital = Hospital()
        self.commands = HospitalCommands(self.hospital)

    # Тесты для validate_patient_id
    def test_validate_patient_id_valid(self):
        self.assertEqual(self.hospital.validate_patient_id(1), 0)
        self.assertEqual(self.hospital.validate_patient_id(200), 199)

    def test_validate_patient_id_invalid(self):
        with self.assertRaises(ValueError):
            self.hospital.validate_patient_id(0)
        with self.assertRaises(ValueError):
            self.hospital.validate_patient_id(201)
        with self.assertRaises(ValueError):
            self.hospital.validate_patient_id("abc")

    # Тесты для get_status
    def test_get_status(self):
        self.assertEqual(self.commands.get_status(1), "Болен")

    def test_get_status_after_discharge(self):
        self.commands.discharge(1)
        with self.assertRaises(ValueError):
            self.commands.get_status(1)

    # Тесты для status_up
    def test_status_up(self):
        self.assertEqual(self.commands.status_up(1), "Слегка болен")
        self.assertEqual(self.commands.status_up(1), "Готов к выписке")

    def test_status_up_ready_to_discharge(self):
        self.commands.status_up(1)
        self.commands.status_up(1)
        self.assertEqual(self.commands.status_up(1), "ready_to_discharge")

    def test_status_up_discharge_patient(self):
        self.commands.discharge(1)
        with self.assertRaises(ValueError):
            self.commands.status_up(1)

    # Тесты для status_down
    def test_status_down(self):
        self.commands.status_up(1)
        self.assertEqual(self.commands.status_down(1), "Болен")

    def test_status_down_minimum_status(self):
        # Проверяем, что при минимальном статусе вызывается ValueError
        self.hospital.patients[0] = 0  # Устанавливаем минимальный статус для первого пациента
        with self.assertRaises(ValueError) as context:
            self.commands.status_down(1)
        self.assertIn("Пациент 1 уже имеет минимальный статус", str(context.exception))


    def test_status_down_discharge_patient(self):
        self.commands.discharge(1)
        with self.assertRaises(ValueError):
            self.commands.status_down(1)

    # Тесты для discharge
    def test_discharge(self):
        self.assertEqual(self.commands.discharge(1), "Пациент 1 выписан.")

    def test_discharge_already_discharged(self):
        self.commands.discharge(1)
        self.assertEqual(self.commands.discharge(1), "Пациент 1 выписан.")

    # Тесты для calculate_statistics
    def test_calculate_statistics_initial(self):
        stats = self.commands.calculate_statistics()
        self.assertEqual(stats["Болен"], 200)
        self.assertEqual(stats["Выписан"], 0)

    def test_calculate_statistics_after_changes(self):
        self.commands.status_up(1)  # Болен -> Слегка болен
        self.commands.status_up(2)  # Болен -> Слегка болен
        self.commands.status_up(2)  # Слегка болен -> Готов к выписке
        self.commands.discharge(3)  # Выписываем пациента
        stats = self.commands.calculate_statistics()
        self.assertEqual(stats["Болен"], 197)
        self.assertEqual(stats["Слегка болен"], 1)
        self.assertEqual(stats["Готов к выписке"], 1)
        self.assertEqual(stats["Выписан"], 1)

if __name__ == "__main__":
    unittest.main()
