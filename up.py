import subprocess
import time
import random
import string

def execute_command(command, input_data=None):
    try:
        subprocess.run(command, shell=True, check=True, input=input_data, text=True, timeout=30)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e}")

def generate_random_username():
    return ''.join(random.choices(string.ascii_lowercase, k=10))

def main():
    # Buka CMD
    execute_command("start cmd")

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

    # Inisialisasi npm dengan scope
    execute_command("npm init --scope=@WanXcoinG", input_data=generate_random_username() + "\n" + ('\n' * 7))

    # Delay 5 detik
    time.sleep(5)

    # Publish dengan akses publik
    execute_command("npm publish --access public")

if __name__ == "__main__":
    main()
