sentence = "Hola mundo. Curso de Python."
i = 0
while i < len(sentence):
    if sentence[i] == ".":
        print(i)
        break
    
    i += 1