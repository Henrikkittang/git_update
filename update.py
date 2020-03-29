
import subprocess
import git
import os

def test():

    status = subprocess.check_output(['git', 'remote', 'show', 'https://github.com/Henrikkittang/git_update']).decode('utf-8')

    if('up to date' in status):
        with open('main.js', 'r') as file:
            data = file.read()
            file.close()

        subprocess.Popen(['git', 'pull', 'https://github.com/Henrikkittang/git_update', 'master'])

        with open('main.js', 'w') as file:
            file.write(data)
            file.close()

test()

"""
import schedule
import time

schedule.every(5).seconds.do(test)
while True:
    schedule.run_pending()
    time.sleep(1)"""
