from pythonping import ping

def checkProtocol(url):
  if any(protocol in url for protocol in ['http://', 'https://']):
    return True
  return False

def verifyInternalLatency(host):
  # todo
  pass
