# temperature converter

TEMPERATURE_SCALES = {
    'Celsius': 'C',
    'Fahrenheit': 'F',
    'Kelvin': 'K'
}

def convert_temperature(value, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
        else:
            return value
    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32) / 1.8
        elif output_scale == 'K':
            return (value + 459.67) * 5 / 9
        else:
            return value
    elif input_scale == 'K':
        if output_scale == 'C':
            return value - 273.15
        elif output_scale == 'F':
            return value * 9 / 5 - 459.67
        else:
            return value
    else:
        return value
    
while True:
    try:
        user_temp = float(input("Введіть температуру: "))
        user_input_scales = input("Введіть шкалу з якої хочете конвертувати 'С - цельсій', 'F - Фаренгейт' та 'K - Кельвін': ").upper()
        user_output_scales = input("Введіть шкалу в яку хочете конвертувати 'С - цельсій', 'F - Фаренгейт' та 'K - Кельвін': ").upper()
        
        if user_input_scales in TEMPERATURE_SCALES.values() or user_output_scales in TEMPERATURE_SCALES.values():
            print("Невірно введена шкала")
            continue
        
        convert_value = convert_temperature(user_temp, user_input_scales, user_output_scales)
        print(f"Ви перевели {user_temp} з {user_input_scales} в {user_output_scales} і отримали {convert_value}")
    
    except ValueError:
        print("Невірні данні, спробуйте ще раз")
        continue

        
    