import os
import requests
import yaml
import glob
from urllib.parse import urlparse
from colorama import Fore, Style

from .constants import ( 
  output_file,
  config_yml
)

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

def buildAcceptedPayloadsList(payloads_dir):
  accepted_payloads_lists = [os.path.splitext(os.path.basename(payload_list))[0] for payload_list in glob.glob(f'{payloads_dir}/*.txt')]
  accepted_payloads_lists.append('all')
  return accepted_payloads_lists

def loadConfigFromFile():
  '''
  Carrega as configurações do arquivo config.yml
  :returns: yaml_content -- Dicionário com configurações presentes no yml
  '''
  try:
    with open(config_yml, 'r') as stream:
      try:
        return yaml.safe_load(stream)
      except yaml.YAMLError as e:
        print(f'{Fore.RED}[!] Fail to load file content : {e}{Style.RESET_ALL}')
        exit()
  except Exception as e:
    print(f'{Fore.RED}[!] Fail to load config file : {e}{Style.RESET_ALL}')
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

def outputAcceptedPayloads(accepted_payloads, output):
  with open(output, 'w') as filehandle:
    for key, value in accepted_payloads.items():
      filehandle.writelines(f'## Lista: {key.upper()} ##\n')
      filehandle.writelines("Payload: %s\n" % payload for payload in value["get"])
      
  print(f'{Fore.GREEN}Accepted payload writed in file {output}{Style.RESET_ALL}')
  
