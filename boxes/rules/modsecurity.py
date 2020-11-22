import sys

if (len(sys.argv) != 2):
    print(f"Usage: {sys.argv[0]} <amount>")
    exit(1)

cont = 1234
amount = int(sys.argv[1]) / 2
for _ in range(int(amount)):
	print("SecRule ARGS:maliciousarg \"@contains {}test\" \"id:{},deny,log,status:403,msg:'Parametro maliciousarg com valor {}teste'\"".format(cont,cont,cont))
	cont += 1

for _ in range(int(amount)):
        print("SecRule REQUEST_HEADERS:User-Agent \"@contains {}test\" \"id:{},deny,log,status:403,msg:'User-Agent {}teste encontrado'\"".format(cont,cont,cont))
        cont += 1
