#importing needed librarys
from os import system
import time
#print options for the user
print ('MICDS Pinger Tool')
time.sleep(3)
print('Ping MICDS Related Websites to check their status :)')
time.sleep(3)
print('1. Ping MyMICDS')
print('2. Ping MICDS')
print('3. Ping Canvas')
print('4. Ping custom URL')
key = int(input('Input your choice: '))
#tell the computer what your choise means and print the output
if key == 1:
        system("ping mymicds.net")
elif key == 2:
        system("ping www.micds.org")
elif key == 3:
    system("ping micds.instructure.com")
elif key == 4:
        url = input('Enter URL: ')
        system("ping " + url)
else:
        print("Invalid Option!")
