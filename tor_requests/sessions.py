from requests.sessions import Session as OriginalSession

class Session(OriginalSession):
    
    def __init__(self):
        
        # call to super
        super(Session, self).__init__()
        
        # change default proxies
        self.proxies = {
            'http': 'socks5://localhost:9050',
            'https': 'socks5://localhost:9050'
        }
        
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