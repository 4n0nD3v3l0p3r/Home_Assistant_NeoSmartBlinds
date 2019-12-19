import time, math, socket, logging

_LOGGER = logging.getLogger(__name__)
LOGGER = logging.getLogger(__name__)

class NeoSmartBlinds:
    commands={"up": "up", "down": "dn", "micro_up" : "mu", "micro_down" : "md", "stop" : "sp"}

    def __init__(self, host, device, close_time, port=8839):
        self._host = host
        self._port = port
        self._device = device
        self._close_time = int(close_time)
        
    def adjust(self, pos):
        if pos == 50:
            self.sendCommand('gp')
            return
        if pos >= 51:
            self.sendCommand('up')
            wait1 = (pos - 50)*2
            wait = (wait1*self._close_time)/100
            LOGGER.warning(wait)
            time.sleep(wait)
            self.sendCommand('sp')
            return            
        if pos <= 49:    
            self.sendCommand('dn')
            wait1 = (50 - pos)*2
            wait = (wait1*self._close_time)/100
            LOGGER.warning(wait)
            time.sleep(wait)
            self.sendCommand('sp') 
            return

    def sendCommand(self, code):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            newcode = self._device + code + '\r\n'
            s.connect((self._host,self._port))
            while True:
                s.send(newcode.encode())           
        except:
            return

