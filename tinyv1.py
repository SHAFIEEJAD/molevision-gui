import subprocess
import sys

def commands(command):
    try:
        result = subprocess.run(command,shell=True,check=True,text=True,input='53215404')
        return result.returncode
        
    except subprocess.CalledProcessError as e:
        print("Error : {e}")
        return e.returncode

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("id not provided")
        sys.exit(1)
    
    id = sys.argv[1]
    



    commands('echo "53215404" | sudo -S mount 192.168.137.23:/home/molevision/Desktop/mmwave')
    commands('echo "53215404" | sudo -S mount -t /home/ubuntu/Desktop/mmwave')
    commands('echo "53215404" | sudo systemctl enable --now ssh')
    commands(f'echo "53215404" | sudo ssh molevision@192.168.137.23 python3 /home/molevision/Desktop/mmwave/mmwave_p.py {id}')
    sys.exit(0)
