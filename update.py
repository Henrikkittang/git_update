


with open('main.js', 'r') as file:
    data = file.read()
    file.close()



with open('main.js', 'w') as file:
    file.write(data)
    file.close()
