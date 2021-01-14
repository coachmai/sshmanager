#!/usr/bin/env python3
import json
from pathlib import Path
from subprocess import call


class Color(object):
    BLUE = '\033[94m'
    GREEN = "\033[92m"
    RED =  "\033[91m"
    END = '\033[0m'


def main():
    config_path = Path.home().joinpath('.ssh/ssh_servers.json')

    print(config_path)

    with open(str(config_path)) as f:
        servers = json.load(f)

    commands = []
    for i, server in enumerate(servers):
        pr = "{}@{}".format(server['user'], server['host'])
        command = "ssh " + pr
        if 'port' in servers[i]:
            #print("port is " + str(server['port']))
            pr += ":" + str(server['port'])
            command += " -p " + str(server['port'])
        if 'pem' in servers[i]:
            #print("pem is " + server['pem'])
            pr += ", " + server['pem']
            ip = str(Path.home().joinpath('.ssh/' + server['pem']))
            command += " -i " + ip
        commands.append(command)
        print(Color.BLUE, i + 1, Color.END, Color.RED, server['name'], Color.END, pr)
        #print(Color.BLUE, i + 1, Color.END, "{}@{}:{} {}".format(server['user'], server['host'], server['port'], server['pem']))

    print('\nCan I have your number?\n> ', end='')
    ch = int(input())
    #choice = servers[int(input()) - 1]
    #call(['ssh', '-l', choice['user'], '-p', str(choice['port']), choice['host']])
    if ch == 0 or ch >= len(commands):
        return
    ch = ch - 1
    # print(commands[ch].split(' '))
    call(commands[ch].split(' '))
    #call(commands[ch])

if __name__ == '__main__':
    main()
