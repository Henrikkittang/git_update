import schedule
import time

def test():
    print('hello there')


schedule.every(5).seconds.do(test)


while True:
    schedule.run_pending()
    time.sleep(1)

"""
with open('main.js', 'r') as file:
    data = file.read()
    file.close()



with open('main.js', 'w') as file:
    file.write(data)
    file.close()
"""