import requests
import os
from colorama import Fore, Style

def readPayloads(path):
  try:
    payload_file = open(path, 'r')
    payloads = list()

    for line in payload_file.readlines():
      payloads.append(line.strip())
   
    print(f'{Fore.GREEN}Payload file: {path} read sucessfully!{Style.RESET_ALL}')
    
    return payloads     
  except:
    print('[!] Could not open the file {}'.format(path))

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

      print(f'{Fore.RED}{len(accepted_payloads["get"])}/{len(payload_list)}{Style.RESET_ALL} payloads were accepted by the server, using GET method!')
      print(f'{Fore.RED}{len(accepted_payloads["post"])}/{len(payload_list)}{Style.RESET_ALL} payloads were accepted by the server, using POST method!'.format(len(accepted_payloads['post']), len(payload_list)))

      return accepted_payloads
    except:
      print(f'{Fore.RED}[!] Fail to connect to {host}{Style.RESET_ALL}')
    
    