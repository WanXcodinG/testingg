import subprocess
import time
import random

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e}")

def interact_with_process(process, inputs):
    for input_line in inputs:
        process.stdin.write(input_line.encode('utf-8') + b'\n')
        process.stdin.flush()
        time.sleep(1)

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
    
    # Publish npm
    execute_command("npm publish")

    # Tunggu 10 detik
    time.sleep(10)

    # Inisialisasi npm dengan scope
    npm_init_process = subprocess.Popen(['npm', 'init', '--scope=@WanXcoinG'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Menanggapi prompt dari npm init
    inputs = [
        "fake_package_" + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5)) + "\n",
        "\n",  # version
        "\n",  # description
        "\n",  # entry point
        "\n",  # git repository
        "\n",  # keywords
        "\n",  # author
        "\n",  # license
        "yes\n"  # Is this OK?
    ]
    interact_with_process(npm_init_process, inputs)

    # Tunggu proses selesai
    npm_init_process.wait()

    # Delay 5 detik
    time.sleep(5)

    # Publish dengan akses publik
    execute_command("npm publish --access public")

if __name__ == "__main__":
    main()
