name = 'Giovanni'
last_name = 'García'

# 1
# + --> permite unir dos o mas string
full_name = name + ' ' + last_name + ' ' + str(30)

print(full_name)

#2
full_name = ' '.join([name, last_name])

print(full_name)

# 3 (%s)
full_name = 'El nombre completo es: %s %s' %(name, last_name)

print(full_name)