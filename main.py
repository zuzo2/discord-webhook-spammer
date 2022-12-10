import requests
import os.path
import os
import time
import threading
import sys

try:
    os.system('pip install colorama >nul && cls')
    import colorama
except:
    import colorama

def set_title():
  title = "Discord Webhook Spammer by PRO JÁTÉKOS#8240"
  try:
    os.system(f"title {title}")
  except:
    os.system(f"title {title}")

threading.Thread(target=set_title).start()

print("")
print(colorama.Fore.GREEN + "█░█░█ █▀▀ █▄▄ █░█ █▀█ █▀█ █▄▀   █▀ █▀█ ▄▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀█")
print(colorama.Fore.GREEN + "▀▄▀▄▀ ██▄ █▄█ █▀█ █▄█ █▄█ █░█   ▄█ █▀▀ █▀█ █░▀░█ █░▀░█ ██▄ █▀▄")
print("")
print(colorama.Fore.RED + "█░█ ▄█ ░ ▄█")
print(colorama.Fore.RED + "▀▄▀ ░█ ▄ ░█")
print("")

def hook():
	try:
		if os.path.exists('./webhooks.txt') == True:
			if os.stat("webhooks.txt").st_size == 0:
				print(colorama.Fore.RED + "\nNincsenek webhookot. Kérlek írj be egy webhook URL-t a " + colorama.Fore.GREEN + "webhooks.txt" + colorama.Fore.RED + "-be!")
			else:
				content = input(colorama.Fore.BLUE + "[" + colorama.Fore.CYAN + ">" + colorama.Fore.BLUE + "] " + colorama.Fore.YELLOW + "Írd be a üzenetet amit a webhook spammeljen: " + colorama.Fore.RED)
				while True:
					for line in open('webhooks.txt'):
						line = line.strip()
						req = requests.post(
							line,
							json = {
								"content": content
							}
						)
						statusCode = str(req.status_code)
						if statusCode.startswith('2') == True:
							print(colorama.Fore.GREEN + '[' + str(req.status_code) + ']' + colorama.Fore.GREEN + ' Üzenet sikeresen elküldve.')
						elif statusCode.startswith('4') == True:
							if statusCode == '429':
								retry = int(req.headers['retry-after']) / int(1000)
								print(colorama.Fore.RED + '\nA discord ratelimitelt. Újrapróbálás ' + str(retry) + ' másodperc múlva.\n')
								time.sleep(retry)
							else:
								print('[' + str(req.status_code) + ']' + colorama.Fore.RED + ' A üzenet nem lett elküldve!')
		elif os.path.exists('./webhooks.txt') == False:
			print(colorama.Fore.RED + '\nNem található webhooks.tx fájl, hozd létre és írd bele a webhook url-t!')
	except KeyboardInterrupt:
		print(colorama.Fore.RED + '\nKilépés...')
		exit()

hook()