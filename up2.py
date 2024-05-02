import subprocess
import time
import random

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e}")

def main():
    # Infinite loop for npm initialization and publishing
    while True:
        # Inisialisasi npm dengan menjalankan script Python 'pac.py'
        execute_command("python pac.py")

        # Publish dengan akses publik
        execute_command("npm publish --access public")

        # Wait for some time before running again (adjust as needed)
        time.sleep(60)  # Wait for 1 minute before running again

if __name__ == "__main__":
    main()
