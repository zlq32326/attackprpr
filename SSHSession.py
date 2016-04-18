#coding = utf-8
_author_ ='dj'
import pexpect
PROMPT = ['#', '>>>', '>', '/$']
def send_Command(child,cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)
def connect(user, host, password):
    ssh_newKey = 'Are you sure you want to continue connecting'
    connStr = 'ssh' + user + '@' + host
    child = prxpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newKey, '[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connecting')
        return
    child.sendline(password)
    child.expect(PROMPT)
    return child
def main():
    host = 'localHost'
    user = 'root'
    password = 'toor'
    child = connect(user, host, password)
    send_command(child, 'cat/etc/shadow|grep root')

if _name_ == '_main_':
    main()
