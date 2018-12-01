from requests.sessions import Session as OriginalSession
from stem import Signal
from stem.control import Controller
from time import sleep
import json

PORT0 = 9050
PORT1 = 9051
PASS = 'vanzan'

class TorConnection:
    
    def __init__(self):
        pass
    
    def renew(self):
        with Controller.from_port(port = PORT1) as controller:
            controller.authenticate(password = PASS)
            controller.signal(Signal.NEWNYM)


class Session(OriginalSession):
    
    def __init__(self):
        super(Session, self).__init__()
        
        # change default proxies
        self.proxies = {
            'http': 'socks5://localhost:{0}'.format(PORT0),
            'https': 'socks5://localhost:{0}'.format(PORT0)
        }
        
    def ip(self):
        r = self.get('https://api.ipify.org?format=json')
        return json.loads(r.text)['ip']
    
    def renew(self):
        current_ip = self.ip()
        
        # renew tor
        with Controller.from_port(port = PORT1) as controller:
            controller.authenticate(password = PASS)
            controller.signal(Signal.NEWNYM)
        
        # reinit
        self.__init__()
        
        # wait for ip to change
        # count = 60
        # while current_ip == self.ip():
        #     sleep(5)
        #     count -= 1
        #     if count == 0:
        #         raise Exception('TimeoutException at self.renew()')

def session():
    """
    Returns a :class:`Session` for context-management.

    .. deprecated:: 1.0.0

        This method has been deprecated since version 1.0.0 and is only kept for
        backwards compatibility. New code should use :class:`~requests.sessions.Session`
        to create a session. This may be removed at a future date.

    :rtype: Session
    """
    return Session()
    
class SessionPool:
    
    def __init__(self, n):
        self.tor = TorConnection()
        self.session_pool = []
        self.current = 0
        self.n = n
        
        tries = 0
        while len(self.session_pool) < n:
            session = Session()
            
            if session.ip() not in self.ips():
                self.session_pool.append(session)
            else:
                self.tor.renew()
                tries += 1
        
        self.tries = tries
        
    def next(self):
        rv = self.session_pool[self.current % self.n]
        self.current += 1
        return rv
                
    def sessions(self):
        return self.session_pool
        
    def ips(self):
        return [s.ip() for s in self.session_pool]