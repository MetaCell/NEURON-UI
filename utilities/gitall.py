#!/usr/bin/python

#
#	Utility script for mass git operatiosn on geppetto repos listed in ./config.json
#
#	Usage:
# 	gitall branches: print current branch of each repo
#
#	gitall checkout <branch> : checkout <branch> on each repo
#
#	gitall pull <remote> <branch> : execute git pull on each repo
#
#	gitall fetch <remote> <branch> : execute git fetch on each repo
#
#

import os
import sys
import getopt
import subprocess
import json
from subprocess import call

config = {

    "repos": [
        {
            "name": "NEURON_UI",
            "url": "..",
        },
        {
            "name": "org.geppetto.frontend.jupyter",
            "url": "../org.geppetto.frontend.jupyter",
        },
        {
            "name": "org.geppetto.frontend",
            "url": "../org.geppetto.frontend.jupyter/src/jupyter_geppetto/geppetto/",
        },
        {
            "name": "Geppetto Neuron",
            "url": "../org.geppetto.frontend.jupyter/src/jupyter_geppetto/geppetto/src/main/webapp/extensions/geppetto-neuron/",
        }
    ]
}


def incorrectInput(argv, msg):
    print msg
    sys.exit()

def main(argv):
    command = []
    if(len(argv) == 0):
        incorrectInput(argv, 'Too few paramaters')

    elif(argv[0] == 'push'):
        command = ['git', 'push', argv[1], argv[2]]

    elif(argv[0] == 'add'):
        command = ['git', 'add', argv[1]]

    elif(argv[0] == 'commit'):
        command = ['git', 'commit', argv[1], argv[2]]

    elif(argv[0] == 'branches'):
        command = ['git', 'rev-parse', '--abbrev-ref', 'HEAD']

    elif(argv[0] == 'reset'):
        command = ['git', 'reset', '--hard', 'HEAD']

    elif(argv[0] == 'status'):
        command = ['git', argv[0]]

    elif(argv[0] == 'remote'):
        for repo in config['repos']:
            print repo['name'] + '  ' + subprocess.check_output(['git', 'remote', 'add', 'mlolson', 'https://github.com/mlolson/' + repo['name'] + '.git'], cwd=os.path.join(config['sourcesdir'], repo['name']))
        return

    elif(argv[0] == 'checkout'):
        if(len(argv) == 2):
            command = ['git', 'checkout', argv[1]]
        elif(len(argv) == 3):
            command = ['git', 'checkout', argv[1], argv[2]]
        else:
            incorrectInput(argv, 'Expected <=3 paramaters')

    elif(argv[0] == 'pull' or argv[0] == 'fetch'):
        if(len(argv) == 1):
            command = ['git', argv[0]]
        elif(len(argv) == 2):
            command = ['git', argv[0], argv[1]]
        elif(len(argv) == 3):
            command = ['git', argv[0], argv[1], argv[2]]
        else:
            incorrectInput(argv, 'Too many paramaters')

    else:
        incorrectInput(argv, 'Unrecognized command')

    for repo in config['repos']:
        try:
            print repo['name'] + '  ' + subprocess.check_output(command, cwd=repo['url'])
        except:
            print "Error -- trying next repo"


if __name__ == "__main__":
    main(sys.argv[1:])
