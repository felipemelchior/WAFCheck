from pythonping import ping

def verifyExternalLatency():
  '''
  Função que coleta o tempo de latência de sites expostos na internet

  :returns: response_time -- Objeto com as latências obtidas 
  '''

  external_ips = ['8.8.8.8', '1.1.1.1', '8.8.4.4']
  response_time = dict()

  for url in external_ips:
    response_list = ping(url, size=40, count=50)
    response_time[url] = response_list.rtt_avg_ms

  return response_time

def printExternalLatency(response_time):
  '''
  Imprime o tempo de latência em cada servidor testado
  '''

  for url in response_time:
    print('{} average response time => {}'.format(url, response_time[url]))

