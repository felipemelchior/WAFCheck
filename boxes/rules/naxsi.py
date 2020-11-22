import sys

if(len(sys.argv) != 2):
    print(f"Usage: {sys.argv[0]} <amount")
    exit(1);

cont = 2000
amount = int(sys.argv[1])/2
for _ in range(int(amount)):
    print("MainRule \"str:{}teste\" \"msg: {}teste\" \"mz:ARGS|URL|BODY|$HEADERS_VAR:Cookie\" \"s:$XSS:8\" id:{};".format(cont,cont,cont))
    cont += 1

for _ in range(int(amount)):
    print("MainRule \"str:{}teste\" \"msg: DN SCAN {}teste User Agent\" \"mz:$HEADERS_VAR:User-Agent\" \"s:$UWA:8\" id:{};".format(cont,cont,cont,cont))
    cont += 1

