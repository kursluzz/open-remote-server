import subprocess

EVENTS = ['shutdown']

def do(act):
    if act in EVENTS:
        globals()[act]()

def shutdown():
    subprocess.call(["shutdown", "-p", "-f"])



