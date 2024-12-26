from models import Hospital
from commands import HospitalCommands

TRANSLATIONS = {
    "узнать статус пациента": "get status",
    "повысить статус пациента": "status up",
    "понизить статус пациента": "status down",
    "выписать пациента": "discharge",
    "рассчитать статистику": "calculate statistics",
    "стоп": "stop"
}

def main():
    hospital = Hospital()
    commands = HospitalCommands(hospital)
    command_map = {
        "get status": commands.get_status,
        "status up": commands.status_up,
        "status down": commands.status_down,
        "discharge": commands.discharge,
        "calculate statistics": commands.calculate_statistics,
        "stop": commands.stop
    }

    print("Добро пожаловать в систему автоматизации больницы.")
    while True:
        command = input("Введите команду: ").strip().lower()
        translated_command = TRANSLATIONS.get(command, command)
        if translated_command in command_map:
            if translated_command in ["get status", "status up", "status down", "discharge"]:
                patient_id = input("Введите ID пациента: ")
                command_map[translated_command](patient_id)
            else:
                command_map[translated_command]()
        else:
            print("Ошибка: Неизвестная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
