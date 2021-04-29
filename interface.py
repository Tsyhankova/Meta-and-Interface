from abc import ABC, abstractmethod
import pickle
import json


class SerializationInterface(ABC):

    @abstractmethod
    def serialization_to_bin(self, some_data):
        data = pickle.dumps(some_data)
        return data

    @abstractmethod
    def serialization_to_json(self, some_data):
        data = json.dumps(some_data)
        return data

class ListSerialization(SerializationInterface):
    
    def serialization_to_bin(self, some_data):
        data = pickle.dumps(some_data)
        return data

    def serialization_to_json(self, some_data):
        data = json.dumps(some_data)
        return data


if __name__ == "__main__":
    main()
    


"""
some_data = "sghjxj"
a = ListSerialization()
print(a.serialization_to_bin(some_data))
print(a.serialization_to_json(some_data))
"""



    
