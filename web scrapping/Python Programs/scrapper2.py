import requests
import time
file = open("newdoc.txt","a")

for i in range(10000,300000):
    result = requests.get(f"https://www.ratemyprofessors.com/professor/{i}")
    # print(f"https://www.ratemyprofessors.com/professor/{i}")
    if(result.status_code == requests.codes.ok):
        file.write(f"https://www.ratemyprofessors.com/professor/{i}\n")
        print(f"Ok{i}")
    time.sleep(1)

print("Over")
    
file.close()
