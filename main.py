import argparse

from utils.run_payloads import run_payloads

from utils.utils import (
  verifyHTTPConnection, 
  checkRoot, 
  checkProtocol, 
  printResults, 
  plotBanner
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

  return parser.parse_args()

def main():
  '''
  Função principal do programa
  '''
  args = parseArguments()
  host = args.url
  param = args.param

  checkProtocol(host)

  host_external_list = ['https://google.com', 'https://facebook.com', 'https://cloudflare.com'] 

  response_http_external = verifyHTTPConnection(host_external_list)
  printResults(response_http_external, False)

  response_http_internal = verifyHTTPConnection([host])
  printResults(response_http_internal, True)

  accepted_payloads = run_payloads(host, param, 'payloads/xss_payloads.txt')
  
if __name__ == '__main__':
  checkRoot()
  plotBanner()
  main()