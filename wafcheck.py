#!/usr/bin/env python

import argparse

from utils.run_payloads import run_payloads

from utils.utils import (
  verifyHTTPConnection, 
  checkRoot, 
  checkProtocol,
  loadConfigFromFile, 
  printResults,
  outputAcceptedPayloads,
  buildAcceptedPayloadsList
)

from utils.constants import (
  accepted_payloads_choice, 
  host_external_list,
  payloads_dir,
  output_file
)

def parseArguments(payload_dir):
  '''
  Função que retorna os argumentos recebidos

  :returns: parser -- objeto contendo os argumentos   
  '''

  parser = argparse.ArgumentParser(description='Todo')
  parser.add_argument('--version', action='version', version="WAFCheck v1.0")
  parser.add_argument('-u', '--url', required=True, help='Define url address')
  parser.add_argument('-o', '--output', help='Name of output file')
  parser.add_argument('-l', '--list', choices=buildAcceptedPayloadsList(payload_dir), help='Define list of payload to be used', required=True)

  return parser.parse_args()

def main(configs):
  '''
  Função principal do programa
  '''
  args = parseArguments(configs['payloadsDir'] if configs['payloadsDir'] != '' else payloads_dir)
  output = (args.output if args.output != None else output_file) 
  host = args.url
  
  payload_list = args.list
  accepted_payloads = dict()

  checkProtocol(host)

  response_http_external = verifyHTTPConnection(configs['hostExternalList'] if configs['hostExternalList'] != '' else host_external_list)
  printResults(response_http_external, False)

  response_http_internal = verifyHTTPConnection([host])
  printResults(response_http_internal, True)

  if (payload_list == 'all'):
    for payload in accepted_payloads_choice:
      if (payload != 'all'):
        accepted_payloads[payload] = run_payloads(host, payload, configs['blockedRequest'])
  else:
    accepted_payloads[payload_list] = run_payloads(host, payload_list, configs['blockedRequest'])

  outputAcceptedPayloads(accepted_payloads, output)
  
if __name__ == '__main__':
  checkRoot()
  main(loadConfigFromFile())
