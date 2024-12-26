

# ui.py
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
        "calculate statistics": commands.calculate_statistics
    }

    print("Добро пожаловать в систему автоматизации больницы.")
    while True:
        command = input("Введите команду: ").strip().lower()
        translated_command = TRANSLATIONS.get(command, command)
        if translated_command in command_map:
            if translated_command in ["get status", "status up", "status down", "discharge"]:
                patient_id = input("Введите ID пациента: ")
                try:
                    result = command_map[translated_command](patient_id)
                    if translated_command == "status up" and result == "ready_to_discharge":
                        confirm = input("Пациент готов к выписке. Выписать? (да/нет): ").strip().lower()
                        if confirm in ["да", "yes"]:
                            result = commands.discharge(patient_id)
                    print(result)
                except ValueError as e:
                    print(f"Ошибка: {e}")
            else:
                result = command_map[translated_command]()
                if isinstance(result, dict):
                    print("Статистика больницы:")
                    for status, count in result.items():
                        print(f"  {status}: {count}")
                else:
                    print(result)
        elif translated_command == "stop":
            print("Работа завершена.")
            break
        else:
            print("Ошибка: Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
