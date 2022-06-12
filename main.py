# Exploit Founded at Sunday, 12 June 2022 by KIPASGTS aka KIPAS
# Some Idea from: Geruays & Revan-ar
# Script created by PhynX

import requests, threading, datetime, sys, os

os.system('cls' if os.name == 'nt' else 'clear')
print(f"\t   Simple Crown/Trophy Duplicators for Stumble Guys")
print(f"\t\t\tBy: KIPASGTS & PhynX")
print("="*64)
auth = str(input("Auth Key: "))
thr = int(input("Threads: "))
#auth = '{"DeviceId":"9ba3294fea4bb181df5fbfecbf6be796","GoogleId":"","FacebookId":"","Token":"9xOLpZaGxFUvrE6i94R1Fz29qd-uAz6V","Timestamp":1655031269,"Hash":"21ed9d97278c2d8e164c9a6e38159d276c523865"}'

def serang():
        while True:
                dt = datetime.datetime.now()
                try:
                        headers = {
                            'authorization': auth,
                            'use_response_compression': 'true',
                            'Accept-Encoding': 'gzip',
                            'Host': 'kitkabackend.eastus.cloudapp.azure.com:5010',
                        }
                        response = requests.get('http://kitkabackend.eastus.cloudapp.azure.com:5010/round/finishv2/3', headers=headers)
                        if response.status_code == 200:
                                trof = response.text.split('"SkillRating":')[1].split(',')[0]
                                cro = response.text.split('"Crowns":')[1].split(',')[0]
                                sys.stdout.write(f"\r[{dt.year}-{dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}] SUCCESS!! | Trophy: {trof} | Crowns: {cro}")
                                sys.stdout.flush()
                        else:
                                print(f"[{response.status_code}] Failed")
                except Exception as e:
                        print(e)
                        sys.exit(0)

for _ in range(thr):
        threading.Thread(target=serang).start()
