courses = (
#      0         1        2            3            4
    "Python", "Django", "Ruby", "Ruby on Rails", "MySQL", "C#"
)

# var1, var2, var3, var4, var5 = courses[0], courses[1], courses[2], courses[3], courses[4]
                            #       Tupla
#var1, var2, var3, var4, var5 = "Python", "Django", "Ruby", "Ruby on Rails", "MySQL"

# var1, var2, var3, var4, var5, var6 = courses # --> desempaquetado de Tuplas

# _
# var1, _, var3, var4, var5, _ = courses # --> ignorar valores de tupla

# var1,var2, *sub_cursos = courses # --> agupar valores
# var1,var2, *sub_cursos, last_value = courses
# var1,var2, *sub_cursos, _, last_value = courses
var1,var2, *_, last_value = courses

print(
    var1, var2, last_value
)