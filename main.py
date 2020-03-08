import os
import argparse

from utils.external import verifyExternalLatency, printExternalLatency
from utils.internal import checkProtocol
from utils.banner import plotBanner

def parseArguments():
  '''
  Função que retorna os argumentos recebidos

  :returns: parser -- objetos contendo os argumentos
  '''

  parser = argparse.ArgumentParser(description='Todo')
  parser.add_argument('--version', action='version', version="WAF Scenario Analyzer v1.0")
  parser.add_argument('-v', '--verbose', action="store_true", help="Set verbose true or false")
  parser.add_argument('-u', '--url', required=True, help='Define url address')

  return parser.parse_args()

def check_root():
  '''
  Checa se o usuário tentando rodar o programa é um super-usuário
  '''

  if os.getuid() != 0:
    print('User must be root to run this program!')
    exit()

def main():
  '''
  Função principal do programa
  '''
  args = parseArguments()

  if not checkProtocol(args.url):
    print('[!] Protocol (http/https) must be provided')
    exit()

  response_external_time = verifyExternalLatency()
  if args.verbose: printExternalLatency(response_external_time)

  

if __name__ == '__main__':
  check_root()
  plotBanner()
  main()