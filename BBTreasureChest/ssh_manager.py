
'''
requirements: sshtunnel
'''

from sshtunnel import SSHTunnelForwarder


class SSHTunnelManager:
    '''
    unsafe imp with the status of the connection unknown.
    the user should guarantee the validity of the server status.
    '''
    server_roster: dict[str, SSHTunnelForwarder]

    def __init__(self):
        self.server_roster = {}

    def add_server(self, server_card: dict, ifConnect:bool = True) -> bool:
        assert self.check_server_card(server_card) is True, "Server card is invalid!"
        # check redundancy

        # add server
        server = SSHTunnelForwarder(
            ssh_address_or_host=(server_card['ssh_address_or_host'], server_card['ssh_port']),
            ssh_username=server_card['ssh_username'],
            ssh_password=server_card['ssh_password'],
            remote_bind_address=(server_card['remote_bind_address'], server_card['remote_port']),
            local_bind_address=(server_card['local_bind_address'], server_card['local_port'])
        )

        self.server_roster[server_card['name']] = server

        if ifConnect:
            server.start()

        return True
    
    def stop_server(self, server_name: str) -> bool:
        '''
        literally stop the connection to the server.
        would return false if the server is not registed in the roster.
        '''
        if server_name not in self.server_roster:
            return False
        self.server_roster[server_name].stop()
        return True
    
    def start_server(self, server_name: str) -> bool:
        if server_name not in self.server_roster:
            return False
        self.server_roster[server_name].start()
        return True
    
    def remove_server(self, server_name: str) -> bool:
        if server_name not in self.server_roster:
            return False
        self.server_roster[server_name].stop()
        del self.server_roster[server_name]
        return True

    def check_server_card(self, server_card: dict) -> bool:
        # TODO add server card validity check
        return True


