import os
import argparse

from utils.external import verifyExternalLatency, printExternalLatency


def parseArguments():
  '''
  Função que retorna os argumentos recebidos

  :returns: parser -- objetos contendo os argumentos
  '''

  parser = argparse.ArgumentParser(description='Todo')
  parser.add_argument('--version', action='version', version="WAF Scenario Analyzer v1.0")
  parser.add_argument('-v', '--verbose', action="store_true", help="Set verbose true or false")
  parser.add_argument('-u', '--url', required=True, help='Define host address')

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

  response_time = verifyExternalLatency()
  if args.verbose: printExternalLatency(response_time)

if __name__ == '__main__':
  check_root()
  main()