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
  return f"{os.path.join(os.getcwd(), payloads_dir, path)}.txt"

def printResults(payloads_path, payload_list, time, accepted_payloads):
  print(f'Tests with {payloads_path} ended! Elapsed time {Fore.GREEN}{time:.2f} s{Style.RESET_ALL}')
  
  if (len(accepted_payloads["get"]) != 0):
    print(f'{Fore.RED}{len(accepted_payloads["get"])}/{len(payload_list)}{Style.RESET_ALL} payloads were accepted by the server, using GET method!')
  else: 
    print(f'{Fore.GREEN}{len(accepted_payloads["get"])}/{len(payload_list)}{Style.RESET_ALL} payloads were accepted by the server, using GET method!')
  print()

def run_payloads(host, payloads_path, blocked_requests):
  payload_list = readPayloads(payloads_path)
  accepted_payloads = dict()
  accepted_payloads['get'] = list()
  blocked_request = False

  if payload_list:
    try:
      print(f'{Fore.YELLOW}Starting tests with {payloads_path} list{Style.RESET_ALL}')
      start = time.time()

      for payload in payload_list:
        response = requests.get(host, params={'test': payload})
        if (response.status_code == 200):
          for blocked_template in blocked_requests:
            if blocked_template in response.text: 
              blocked_request = True
          
          if not blocked_request:
            accepted_payloads['get'].append(payload)

      end = time.time()
      printResults(payloads_path, payload_list, end - start, accepted_payloads)
      
      return accepted_payloads
    except:
      print(f'{Fore.RED}[!] Fail to connect to {host}{Style.RESET_ALL}')
    