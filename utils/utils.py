import os
import requests
from art import tprint
from urllib.parse import urlparse
from colorama import Fore, Style

def plotBanner():
  '''
  Utiliza a lib 'art' para imprimir na tela o nome do programa
  '''

  tprint('WAFScA', font="random")
  print(f'{Fore.GREEN}Created by Felipe H Melchior{Style.RESET_ALL}', end="\n\n")

def checkRoot():
  '''
  Checa se o usuário tentando rodar o programa é um super-usuário
  '''

  if os.getuid() != 0:
    print(f'{Fore.RED}[!] User must be root to run this program!{Style.RESET_ALL}')
    exit()

def checkProtocol(url):
  if any(protocol in url for protocol in ['http://', 'https://']):
    pass
  else:
    print(f'{Fore.RED}[!] Protocol (http/https) must be provided!{Style.RESET_ALL}')
    exit()

def verifyHTTPConnection(host_list):
  '''
  Função que se conecta aos hosts usando protocolo HTTP para medir a latencia

  :returns: response_time -- Objeto com as latências obtidas 
  '''
  response_time_aux = list()
  response_time = dict()

  for host in host_list:
    try:
      for _ in range(10):
        response = requests.head(host)
        response_time_aux.append(response.elapsed.total_seconds())
      response_time[urlparse(host).netloc] = sum(response_time_aux) / len(response_time_aux)
    except:
       print(f'{Fore.RED}[!] Fail to connect to {host}{Style.RESET_ALL}')

  return response_time  
  
def printResults(response_time, internal):
  '''
  Imprime o tempo de latência em cada servidor testado
  '''
  
  if not response_time:
    print(f'{Fore.RED}[!] List of responses is empty, nothing to show{Style.RESET_ALL}')
  else:
    if internal:
      print(f'{Fore.YELLOW}Checking internal connectivity...{Style.RESET_ALL}')
    else:
      print(f'{Fore.YELLOW}Checking external connectivity...{Style.RESET_ALL}')

    for url in response_time:
      print('{} average response time => {:.2f} ms'.format(url, response_time[url]))
    print()

  