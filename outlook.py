from selenium import webdriver
import time
import imaplib
import datetime

global driver
driver = webdriver.Firefox(executable_path="C:\\Users\\username\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\geckodriver-v0.26.0-win64\\geckodriver.exe")
hotmailacc='mail1 mail2 mail3'
hotmailacc=hotmailacc.split()
passwordacc='pwd1,pwd2,pwd3'
passwordacc=passwordacc.split(',')
finaldic=dict(zip(hotmailacc,passwordacc))
count=["[b'']"]

class StyleCode:
    def LOGIN(self,account):
        driver.get("login url for hotmail sign in page")
        elem = driver.find_element_by_id("i0116")
        pwd=finaldic[account]
        elem.send_keys(account)
        nextButton = driver.find_element_by_id('idSIButton9')
        nextButton.click()
        time.sleep(1)
        #locating password field and entering my pasalexsword
        elem2 = driver.find_element_by_id("i0118")
        elem2.send_keys(pwd)
        signinButton = driver.find_element_by_id('idSIButton9')
        signinButton.click()
        
        
    def mail2asign(self, uname="mail-id", passwd="password", imapsw="imap-mail.outlook.com", imapprt="993"):
        for j in range(len(hotmailacc)):
            self.username = hotmailacc[j]
            self.password = passwordacc[j]
            self.imap_server = imapsw
            self.imap_port = imapprt
            server = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            try:
                server = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
                server.login(self.username, self.password)
                server.select('INBOX')
                typ, data = server.search(None,'UNSEEN','SINCE','23-Mar-2020')
                data=str(data).split()
                if (count==data):
                    print("The Unread mails for",hotmailacc[j],"------->0")
                    driver.get("https://login.live.com/logout.srf")
                    server.logout()
                else:
                    print("The Unread mails for",hotmailacc[j],"------->",len(data))
                    obj.LOGIN(hotmailacc[j])
                    print("Enter q to quit")
                    q=input()
                    if(q=='q'):
                        driver.get("https://login.live.com/logout.srf")
                        server.logout()
                        
            except:
                print("[!] Cannot connect imap server. Probably poor internet connection problem.")
                return -1

obj=StyleCode()
n=int(input("enter 1 to notify 2 to open\n"))
if n==1:
    obj.mail2asign()
    
else:
    print("Choose an account from the following")
    account=input()
    obj.LOGIN(account)
