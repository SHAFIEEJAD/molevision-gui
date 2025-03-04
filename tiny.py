import subprocess
import sys

def run_remote_command(command, password):
    try:
        # Build the full command to echo the password and run sudo
        full_command = f'sudo {command}'

        # Run the command
        process = subprocess.Popen(
            full_command,                # Command as a string
            shell=True,                  # Run in shell for piping
            stdout=subprocess.PIPE,      # Capture stdout
            stderr=subprocess.PIPE,      # Capture stderr
            universal_newlines=True      # Handle output as text
        )
    except Exception as e:
        print(f"An error occurred while running '{command}': {e}")
        return -1
def run_sudo_command(command, password):
    try:
        # Build the full command to echo the password and run sudo
        full_command = f'echo "{password}" | sudo -S {command}'

        # Run the command
        process = subprocess.Popen(
            full_command,                # Command as a string
            shell=True,                  # Run in shell for piping
            stdout=subprocess.PIPE,      # Capture stdout
            stderr=subprocess.PIPE,      # Capture stderr
            universal_newlines=True      # Handle output as text
        )

        # Capture the output and errors
        stdout, stderr = process.communicate()

        # Check if the command was successful
        if process.returncode == 0:
            print(f"Command '{command}' executed successfully!")
            print(stdout)  # Optionally print the command output
        else:
            print(f"Command '{command}' failed with error: {stderr}")

        return process.returncode

    except Exception as e:
        print(f"An error occurred while running '{command}': {e}")
        return -1

def run_multiple_sudo_commands(password):
    # Define your sudo commands
    commands = [
        "mount 192.168.137.23:/home/molevision/Desktop/mmwave",               # First sudo command
        "mount -t /home/ubuntu/Desktop/mmwave",  # Example: Restarting a service
        "systemctl enable --now ssh"             # Example: Updating package lists
      ]

    # Loop through each command and execute it
    for command in commands:
        result = run_sudo_command(command, password)
        if result != 0:
            print(f"Stopping execution, command '{command}' failed.")
            break
    #subprocess.run(["sudo","ssh"," molevision@192.168.137.23"]);
    remote_command = "ssh molevision@192.168.137.23"
    remote_result =  run_remote_command(remote_command, password)
        

def run_python_script(id):
    print(f'running {id}')
    #subprocess.run([f'/usr/bin/python3 /home/molevision/Desktop/mmwave/mmwave_p.py {id}'], #shell=True)
    process = subprocess.Popen(
        ['python3',f'/home/molevision/Desktop/mmwave/mmwave_p.py {id}'],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        universal_newlines = True,
        shell=True
    )
    while True:
        output = process.stdout.readline()
        if output =='' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc= process.poll()
    return rc
        
if __name__ == "__main__":
    id= sys.argv[1]
    # Run multiple sudo commands with a password
    password = "53215404"  # Replace with the actual sudo password
    run_multiple_sudo_commands(password)
    run_python_script(id)

