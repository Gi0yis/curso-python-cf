# Match --> switch
# _: --> default

score = 5

match score:
    case 10:
        print("Muchas felicidades, tu calificación es 10.")
    case 9 | 8:
        print("Flicidades tu calificación es aprobatoria.")
    case 6 | 7:
        print("Aprobaste la materia.")
    case _:
        print("Lo sentimos calidficación NO aprobatoria.")