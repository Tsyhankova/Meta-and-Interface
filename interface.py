from abc import ABC, abstractmethod
import pickle
import json


class SerializationInterface(ABC):

    @abstractmethod
    def serialization_to_bin(self, some_data):
        file_name = 'data.bin'
        with open(file_name, "wb") as fh:
            pickle.dump(some_data, fh)

    @abstractmethod
    def serialization_to_json(self, some_data):
        file_name = 'data.json'
        with open(file_name, "w") as fh:
            json.dump(some_data, fh)

class ListSerialization(SerializationInterface):
    
    def serialization_to_bin(self, some_data):
        file_name = 'data.bin'
        with open(file_name, "wb") as fh:
            pickle.dump(some_data, fh)

    def serialization_to_json(self, some_data):
        file_name = 'data.json'
        with open(file_name, "w") as fh:
            json.dump(some_data, fh)



    



some_data = "sghjxj"
a = ListSerialization()
a.serialization_to_bin(some_data)
a.serialization_to_json(some_data)




    
