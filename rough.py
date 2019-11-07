import filemodify2
import subprocess
import os

command = 'python /home/jgarg/Documents/python/programs/filemodify2.py'
# p1 =subprocess.call('{} -c'.format(command), stdout=subprocess.PIPE)
# print (p1)
# filemodify2.copy_file('/home/jgarg/Documents/a.txt', '/home/jgarg/Downloads/a.txt')
# p1= subprocess.call('echo $?', stdout=subprocess.PIPE, )
# p1= subprocess.call('{} -c'.format(command), shell=True
# def p1():
#     p1=subprocess.Popen('{} -c'.format(command), stdout=subprocess.PIPE)
#     p2=subprocess.Popen('/home/jgarg/Documents/a.txt', stdin=p1.stdout, stdout=subprocess.PIPE)
#     p3=subprocess.Popen('/home/jgarg/Downloads/a.txt', stdin=p2.stdout, stdout=subprocess.PIPE)
#     p4=p3.stdout
#     return p4
#
# p1()

def p2():
    filemodify2.copy_file('/home/jgarg/Documents/a.txt', '/home/jgarg/Downloads/a.txt')
    p2= subprocess.call('echo $?', shell=True)
    return p2


