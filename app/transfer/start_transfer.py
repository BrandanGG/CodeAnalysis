import os
import paramiko
from dotenv import load_dotenv  # Import load_dotenv

# Load .env file located in /home/codeguard/CodeAnalysis/app/.env
load_dotenv()
def paramiko_con():
    try:
        # Fetch environment variables correctly
        IP = os.getenv('cgip')
        PORT = int(os.getenv('port'))  # Convert port to integer
        USERNAME = os.getenv('username')
        PKPATH = os.getenv('sshkey')  # Ensure this matches the correct env variable name

        print(f"Connecting to {IP} on port {PORT} as {USERNAME} with key {PKPATH}")
        
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Load private key
        pk = paramiko.RSAKey(filename=PKPATH)

        # Connect to the server
        ssh.connect(hostname=IP, port=PORT, username=USERNAME, pkey=pk)
        print("Connected successfully to the server.")

        # Execute the command
        
        stdin, stdout, stderr = ssh.exec_command('pwd')
        print("Command output:", stdout.read().decode())
        print("Error output:", stderr.read().decode())
        ssh.close()
        print("Connection closed.")
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials.")
    except paramiko.SSHException as sshException:
        print("Unable to establish SSH connection:", sshException)
    except Exception as e:
        print("Exception occurred:", e)

paramiko_con()