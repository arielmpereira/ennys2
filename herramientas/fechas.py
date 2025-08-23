def edad(fecha_nacimiento, fecha):
    res = fecha.year - fecha_nacimiento.year
    if fecha.month < fecha_nacimiento.month:
        res -= 1
    elif fecha.month == fecha_nacimiento.month and fecha.day < fecha_nacimiento.day:
        res -= 1
    return res