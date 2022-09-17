from proxy_checker import ProxyChecker
import requests
import threading

files = input("Название файла с прокси: ")
thr = int(input("Кол-во потоков: "))

checker = ProxyChecker()

file = open(files).read().split('\n')

def thread():
    while file:
        to_check = file[0]
        file.remove(to_check)
        try:
            check(to_check)
        except Exception as e:
            print("Ошибка:", e)

def check(proxys):
    try:
        req = requests.get("http://google.com", proxies={'http':f'http://{proxys}'})
        print(f"[LIVE] - {proxys}")
        my_file = open("good.txt", "at")
        my_file.write(f"{proxys}\n")
        my_file.close()
    except IOError:
        print(f"[DEAD] - {proxys}")

for _ in range(thr):
    t = threading.Thread(target=thread)
    t.start()