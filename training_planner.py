import random


def fill_parameters(traning_type):
    duration = random.randint(1, 5)
    action = random.randint(20, 90) * M_IN_H * duration
    #if traning_type == 'WLK':


def keybord_int_input(min_border, max_border, var_type):
    while True:
        try:
            int_var = int(input(messeges[var_type]['ANSW']))
            if int_var >= min_border and int_var <= max_border:
                break
            else:
                print(messeges[var_type]['ERROR'])
        except:
            print(messeges[var_type]['ERROR'])
    return int_var


def input_choice_inlist(check_list, var_type):
    while True:
        try:
            print(messeges[var_type]['ANSW'])
            for count in pool_type:
                print(count, end=' ')
            int_var = int(input('\n'))
            if int_var in check_list:
                break
            else:
                print(messeges[var_type]['ERROR'])
        except:
            print(messeges[var_type]['ERROR'])
    return int_var


M_IN_H = 60
pool_type = [10, 15, 25, 35, 50]
training_type = ('SWM', 'RUN', 'WLK')
trainings_type = []
messeges = {
            'NUMB_TR': {'ANSW': 'Введите количество тренировок для рассчета (от 1 до 50)\n',
                       'ERROR': 'Количество тренировок необходимо указывать в целых числах (от 1 до 50)'},
            'WEIGHT': {'ANSW': 'Введите ваш вес в кг, в целых числах (от 40 до 120)\n',
                      'ERROR': 'Вес необходимо указывать в целых числах от (40 до 120)'},
            'HEIGHT': {'ANSW': 'Введите ваш рост в см в целых числах (от 120 до 240)\n',
                      'ERROR': 'Рост необходимо указывать в целых числах от (от 120 до 240)'},
            'POOL': {'ANSW': 'Выберите тип бассейна',
                    'ERROR': 'Введите размер бассейна из списка'}
}
numb_traning = keybord_int_input(1, 50, 'NUMB_TR')
weight = keybord_int_input(40, 120, 'WEIGHT')
for count in range(0, numb_traning):
    trainings_type.append(random.choice(training_type))
if training_type[2] in trainings_type:
    height = keybord_int_input(120, 240, 'HEIGHT')
if training_type[0] in trainings_type:
    length_pool = input_choice_inlist(pool_type, 'POOL')

        






'''packages: List[Tuple[str, List[int]]] = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]'''