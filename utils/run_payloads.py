import requests
import os
import time
from colorama import Fore, Style

from .constants import payloads_dir

def readPayloads(path):
  try:
    normalized_path = normalizePath(path)
    
    payload_file = open(normalized_path, 'r')
    payloads = list()

    for line in payload_file.readlines():
      payloads.append(line.strip())
   
    print(f'{Fore.GREEN}Payload file: {os.path.basename(normalized_path)} read sucessfully!{Style.RESET_ALL}')
    
    return payloads     
  except:
    print('[!] Could not open the file {}'.format(path))

def normalizePath(path):
  return os.path.join(os.getcwd(), payloads_dir, path)

def makeParam(param, payload):
  if (param):
    return {param: payload} 
  else:
    return {'test': payload}

def run_payloads(host, param, payloads_path):
  payload_list = readPayloads(payloads_path)
  accepted_payloads = dict()
  accepted_payloads['get'] = list()
  accepted_payloads['post'] = list()

  if payload_list:
    try:
      print(f'{Fore.YELLOW}Starting tests with {payloads_path}{Style.RESET_ALL}')
      start = time.time()

      # Get Requests
      for payload in payload_list:
        response = requests.get(host, params=makeParam(param, payload))
        if response.status_code == 200:
          accepted_payloads['get'].append(payload)

      # Post Requests
      for payload in payload_list:
        response = requests.post(host, data=makeParam(param, payload))

        if response.status_code == 200:
          accepted_payloads['post'].append(payload)


      end = time.time()
      print(f'Tests with {payloads_path} ended! Elapsed time {Fore.GREEN}{end - start:.2f} s{Style.RESET_ALL}')
      
      if (len(accepted_payloads["get"]) != 0):
        print(f'{Fore.RED}{len(accepted_payloads["get"])}/{len(payload_list)}{Style.RESET_ALL} payloads were accepted by the server, using GET method!')
      else: 
        print(f'{Fore.GREEN}{len(accepted_payloads["get"])}/{len(payload_list)}{Style.RESET_ALL} payloads were accepted by the server, using GET method!')

      if (len(accepted_payloads["post"]) != 0):
        print(f'{Fore.RED}{len(accepted_payloads["post"])}/{len(payload_list)}{Style.RESET_ALL} payloads were accepted by the server, using POST method!'.format(len(accepted_payloads['post']), len(payload_list)))
      else:
        print(f'{Fore.GREEN}{len(accepted_payloads["post"])}/{len(payload_list)}{Style.RESET_ALL} payloads were accepted by the server, using POST method!'.format(len(accepted_payloads['post']), len(payload_list)))
      print()
      
      return accepted_payloads
    except:
      print(f'{Fore.RED}[!] Fail to connect to {host}{Style.RESET_ALL}')
    
    