from core.vqh_interfaces import MappingInterface
import numpy as np
import time
from pythonosc.udp_client import SimpleUDPClient
import json
from synth.sc import MusicalScale

class OSCMapping(MappingInterface):
    def __init__(self, ip:str="127.0.0.1", port:int=1450) -> None:
        self.client = SimpleUDPClient(ip, port)
        self.scale = MusicalScale()

    def publish_data(self, data, **kwargs):
        print(f'Publishing data: {data}')
        #serialized_data = json.dumps(data[0][0].tolist())
        serialized_data = [(item[0], item[1]) for i, item in enumerate(data[0][0].items())]
        print(f'Serialized data: {serialized_data}')

        self.client.send_message("/vqh/expval", data[1])
        print(f'Published expval: {data[1]}')
        print(f'Published mprob: {serialized_data}')
        for prob in serialized_data:
            self.client.send_message(f"/vqh/mprob/{prob[0]}", prob[1])
            #print(f'Published {prob[0]}: {prob[1]}')

    def update_client(self, ip:str, port:int):
        self.client = SimpleUDPClient(ip, port)

    def freeall(self):
        pass
    def free(self):
        pass
