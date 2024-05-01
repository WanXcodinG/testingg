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
    execute_command("npm init --scope=@WanXcoinG")
    time.sleep(2)

    # Membuat instance subprocess untuk menangani interaksi
    p = subprocess.Popen(['npm', 'init', '--scope=@WanXcoinG'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Menangani output dari npm init
    while True:
        output = p.stdout.readline().strip()
        print(output)
        if "package name: (@WanXcoinG/my-app)" in output:
            random_package_name = "fake_package_" + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
            p.stdin.write(random_package_name + "\n")
            p.stdin.flush()
        elif "Press ^C" in output:
            # Memberikan respons sesuai dengan permintaan untuk menekan ^C untuk keluar
            p.stdin.write("\n")
            p.stdin.flush()
        elif output.startswith("Is this OK?"):
            # Menanggapi permintaan konfirmasi dari npm init
            p.stdin.write("yes\n")
            p.stdin.flush()
            break

    # Tunggu proses selesai
    p.wait()

    # Delay 5 detik
    time.sleep(5)

    # Klik enter tujuh kali (saya asumsikan ini untuk menyetujui default)
    for _ in range(7):
        execute_command("echo. | npm publish")

    # Publish dengan akses publik
    execute_command("npm publish --access public")

if __name__ == "__main__":
    main()
