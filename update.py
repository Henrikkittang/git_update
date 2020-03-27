import schedule
import time
import subprocess


def test():
    with open('main.js', 'r') as file:
        data = file.read()
        file.close()

    output = subprocess.check_output(['git', 'pull', 'https://github.com/Henrikkittang/git_update', 'master'])

    with open('main.js', 'w') as file:
        file.write(data)
        file.close()

schedule.every(5).seconds.do(test)
while True:
    schedule.run_pending()
    time.sleep(1)
