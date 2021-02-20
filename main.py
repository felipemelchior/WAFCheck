import argparse

from utils.run_payloads import run_payloads

from utils.utils import (
  verifyHTTPConnection, 
  checkRoot, 
  checkProtocol, 
  printResults, 
  plotBanner,
  outputAcceptedPayloads
)

from utils.constants import (
  accepted_payloads_choice, 
  host_external_list
)

def parseArguments():
  '''
  Função que retorna os argumentos recebidos

  :returns: parser -- objeto contendo os argumentos
  '''

  parser = argparse.ArgumentParser(description='Todo')
  parser.add_argument('--version', action='version', version="WAF Scenario Analyzer v1.0")
  parser.add_argument('-u', '--url', required=True, help='Define url address')
  parser.add_argument('-p', '--param', help='Define param to be tested')
  parser.add_argument('-l', '--list', choices=accepted_payloads_choice, help='Define list of payload to be used', required=True)

  return parser.parse_args()

def main():
  '''
  Função principal do programa
  '''
  args = parseArguments()
  host = args.url
  param = args.param
  payload_list = args.list
  accepted_payloads = dict()

  checkProtocol(host)

  response_http_external = verifyHTTPConnection(host_external_list)
  printResults(response_http_external, False)

  response_http_internal = verifyHTTPConnection([host])
  printResults(response_http_internal, True)

  if (payload_list == 'all'):
    for payload in accepted_payloads_choice:
      if (payload != 'all'):
        accepted_payloads[payload] = run_payloads(host, param, payload)
  else:
    accepted_payloads[payload_list] = run_payloads(host, param, payload_list)

  outputAcceptedPayloads(accepted_payloads)
  
if __name__ == '__main__':
  checkRoot()
  plotBanner()
  main()
