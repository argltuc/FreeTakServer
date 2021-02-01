#######################################################
# 
# FederationServiceAbstract.py
# Python implementation of the Class FederationServiceAbstract
# Generated by Enterprise Architect
# Created on:      12-Sep-2020 10:32:32 PM
# Original author: natha
# 
#######################################################
from FreeTAKServer.model.ServiceObjects.FederateClients import FederateClients
from FreeTAKServer.model.ServiceObjects.Federate import Federate


class FederationServiceAbstract:
    """FederationServiceAbstract.py Python implementation of the Class
    FederationServiceAbstract Generated by Enterprise Architect Created on:      12-
    Sep-2020 10:32:32 PM Original author: natha
    """
    def __init__(self, pipe):
        self.federateClients = FederateClients()
        self.pipe = pipe


    def recv_data_from_clients(self, clients):
        """this function receives data from all connected client
        """
        try:
            if isinstance(clients, list):
                for client in clients:
                    if isinstance(client, Federate):
                        try:
                            for CoT in client.federationController.receive_data_from_federates():
                                self.pipe.send(CoT)
                        except TypeError:
                            self.federateClients.remove_client(client)
                    else:
                        raise TypeError('the list should only contain instances of the Federate class')
                return 1
            else:
                raise TypeError('this function should only be supplied a list object')
        except Exception as e:
            return -1
    def send_data_to_clients(self, data, clients):
        """this function will send the data of a CoT object to all connected client
        """
        try:
            if isinstance(clients, list):
                for client in clients:
                    if isinstance(client, Federate):
                        client.federationController.send_data_to_federates(data)
                    else:
                        raise TypeError('the list should only contain instances of the Federate class')
                return 1
            else:
                raise TypeError('this function should only be supplied a list object')
        except Exception as e:
            return -1

    def check_if_data_is_available(self, clients):
        """
        this function serves a purpose similar to poll
        within a pipe by iterating over clients and
        in the event any data is received the function
        returns this data
        :param clients:
        :return:
        """
        data = []
        try:
            if isinstance(clients, list):
                client = clients[0]
                if isinstance(client, Federate):
                    for CoT in client.federationController.receive_data_from_federates():
                        data.append(CoT)

                else:
                    raise TypeError('the list should only contain instances of the Federate class')
                return data
            else:
                raise TypeError('this function should only be supplied a list object')
        except Exception as e:
            return -1
