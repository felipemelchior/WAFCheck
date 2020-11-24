#/usr/share/python
import sys

if (len(sys.argv) != 2):
    print(f"Usage: {sys.argv[0]} <amount>")
    exit(1)

amount = int(sys.argv[1]) / 2
cont = 0

print('[\n')
for _ in range(int(amount)):
    print("\t{\n\t\t\"path\": \"GET|"+str(cont)+"teste\",\n\t\t\"caller\": \"*\",\n\t\t\"thresold\": -1\n\t},")
    cont += 1
for i in range(int(amount)):
    if (i == amount-1):
        print("\t{\n\t\t\"path\": \"SERVER|"+str(cont)+"Referer\",\n\t\t\"caller\": \"*\",\n\t\t\"thresold\": -1\n\t}")
    else:
        print("\t{\n\t\t\"path\": \"SERVER|"+str(cont)+"Referer\",\n\t\t\"caller\": \"*\",\n\t\t\"thresold\": -1\n\t},")
    cont += 1
#{
#        "path": "POST|req_message",
#        "caller": "{BASE}edit.php",
#        "threshold": -1
#    },

print(']\n')
