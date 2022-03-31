#! python3
# pw.py - An insecure password locker program.
# import pyperclip
import sys
import winsound

print("This is the name of the program", sys.argv[0]

      )


PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}


password = input("What's the lucky number? ")
if password == "gipcode":
    account = input("Ihon My guy, which password do you need? ")
    if account in PASSWORDS:
      #   pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print("No password for " + account + " .")


winsound.Beep(440, 500)
winsound.PlaySound("beep.wav", winsound.SND_ALIAS)
