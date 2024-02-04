import sys

# завантажуємо рядки з файло логів і вертаємо список
def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            list_of_logs = []
            for line in fh.readlines():
                parameters_dict = parse_log_line(line.strip())
                list_of_logs.append(parameters_dict)
            return list_of_logs
    except FileNotFoundError:
        print(f"\nFile is not found by this path {file_path}") 

# вибираємо оремо дату, час, рівень, повідомлення
# та записуємо у словник
def parse_log_line(line: str) -> dict:
    line_parameters = {}
    patameters_list = line.split(" ")
    our_date, our_time, our_level, *message = patameters_list
    our_message = " ".join(message).strip()
    line_parameters['date'] = our_date
    line_parameters['time'] = our_time
    line_parameters['level'] = our_level
    line_parameters['message'] = our_message
    return line_parameters

# фільтруємо логи по рівню
# та виводимо список логів відповідно до рівня
def filter_logs_by_level(logs: list, level: str) -> list:
    if logs is not None:
        list_of_level = filter(
            lambda item_line: item_line.get('level') == level.upper(),
                logs
            )
        print(f"\n\tДеталі логів для рівня '{level.upper()}':")
        for item_line in list_of_level:
            print(f"\t{item_line['date']} {item_line['time']} - {item_line['message']}")
        return list_of_level

# рахуємо кількість логів кожного рівня
# та вертаємо все як список
def count_logs_by_level(logs: list) -> dict:
    if logs is not None:
        counting_dict = {}
        count_info = 0
        count_debug = 0
        count_error = 0
        count_warning = 0
        try:
            for item_line in logs:
                if item_line.get('level') == "INFO":
                    count_info += 1
                elif item_line.get('level') == "DEBUG":
                    count_debug += 1
                elif item_line.get('level') == "ERROR":
                    count_error += 1
                elif item_line.get('level') == "WARNING":
                    count_warning += 1
            counting_dict = {
                'INFO' : count_info,
                'DEBUG' : count_debug,
                'ERROR' : count_error,
                'WARNING' : count_warning
            }
            return counting_dict
        except TypeError:
            print("\nPlease check entered path to the file")

# виводимо загальний список всіз рівнів і їх кільклсті
def display_log_counts(counts: dict):
    if counts is not None :
        try:
            print("\tРівень логування  |  Кількість")
            print("\t------------------|-----------")
            print(f"\tINFO--------------|  {counts.get('INFO')}")
            print(f"\tDEBUG-------------|  {counts.get('DEBUG')}")
            print(f"\tERROR-------------|  {counts.get('ERROR')}")
            print(f"\tWARNING-----------|  {counts.get('WARNING')}")
        except AttributeError:
            print("\nPlease check entered path to the file")

# головна логіка
def main():
    entered_arguments = sys.argv
    # виконується якщо введено 2 аргументи (зі шляхом до файлу)
    if len(entered_arguments) >= 2:
        path_to_file = entered_arguments[1]
        display_log_counts(
            count_logs_by_level(
                load_logs(path_to_file)
                )
            )
        # виконується якщо введений рівень (третій аргумент)
        if len(entered_arguments) == 3:
            log_level = entered_arguments[2]
            if log_level.lower() in ['info', 'debug', 'error', 'warning']:
                filter_logs_by_level(
                    load_logs(path_to_file),
                    log_level
                )
            else:
                print("Type correctly name of the level please")
    else:
        print("Please use correct quantity of arguments.")

if __name__=="__main__":
    main()
