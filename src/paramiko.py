import paramiko
ssh_client=paramiko.SSHClient()

print('Enter your hostname:')
hostname = input()

print('Enter your username:')
username = input()

print('Enter your password:')
ssh_client.connect(hostname,username,input())
