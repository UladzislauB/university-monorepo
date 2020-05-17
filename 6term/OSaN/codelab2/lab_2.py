import subprocess
import re

output = list(enumerate(str(subprocess.check_output(
    ['fatcat', 'path/FAT.img', '-l', '/'])).split('\\n')))
for i, string in output:
    print(str(i) + ' ' + string)

clusterNumber = int(input("Введите номер кластера: "))
for i, string in output:
    result = re.search("(?<=c=)(.+?)(?=\s)", string)
    number = -1
    if result:
        number = int(result.group(0))

    if number == clusterNumber:
        print(str(i) + ' ' + string)
        break
