import subprocess
import time
import random

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e}")

def main():

    execute_command("git add .")
    time.sleep(3)

    execute_command("git init")
    time.sleep(3)

    execute_command("git add README.md")
    time.sleep(3)

    execute_command('git commit -m "first commit"')
    time.sleep(10)

    execute_command("git branch -M main")
    time.sleep(10)

    execute_command("git remote add origin https://github.com/WanXcodinG/testingg.git")
    time.sleep(10)

    # Push ke branch utama
    execute_command("git push -u origin main")
    time.sleep(10)

    # Tambahkan user npm
    execute_command("npm adduser")

    # Tunggu 10 detik
    time.sleep(30)

    # Publish npm
    execute_command("npm publish")

    # Tunggu 10 detik
    time.sleep(10)

    # Inisialisasi npm dengan menjalankan script Python 'pac.py'
    execute_command("python pac.py")

    # Publish dengan akses publik
    execute_command("npm publish --access public")

if __name__ == "__main__":
    main()
