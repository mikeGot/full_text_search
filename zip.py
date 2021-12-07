from zipfile import ZipFile
from datetime import datetime
password = []
with open("rockyou.txt") as file_handler:
    for line in file_handler:
        password.append(line.replace("\n","").encode('utf-8'))

start = datetime.now()
for p in password:
    try:
        with ZipFile('/Users/mike/study/zip/my_zip.zip') as zf:
            zf.extractall(pwd=p)
    except:
        # print("Bad password: " + str(p) )
        pass
    else:
        print(p)
        break

finish = datetime.now()
print(finish-start)
