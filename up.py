import subprocess
import time
import random

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e}")

def main():
    # Buka CMD
   

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
    execute_command("npm init --scope=@WanXcoinG")
    time.sleep(2)

    # Menunggu prompt untuk nama paket
    p = subprocess.Popen(['npm', 'init', '--scope=@WanXcoinG'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    p.wait(timeout=5)  # Menunggu prompt muncul dalam 5 detik

    # Kirim package name acak
    random_package_name = "fake_package_" + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    p.stdin.write(random_package_name + "\n")
    p.stdin.flush()

    # Menanggapi permintaan konfirmasi dari npm init
    confirmation_response = "yes\n"
    p.stdin.write(confirmation_response)
    p.stdin.flush()

    # Delay 5 detik
    time.sleep(5)

    # Publish dengan akses publik
    execute_command("npm publish --access public")

if __name__ == "__main__":
    main()
