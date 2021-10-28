from .models import Animal, AnimalCharacteristic
from group.models import Group
from characteristic.models import Characteristic
from group.serializers import GroupSerializer
from characteristic.serializers import CharacteristicSerializer
from .serializers import AnimalCharacteristicSerializer

def get_one_animal(animal_ID):
       
        animal = Animal.objects.get(id=animal_ID)

        response_animal = animal.__dict__

        del response_animal['_state']

        group = Group.objects.get(id=response_animal['group_id'])
        serialized_group = GroupSerializer(group)
        response_group = serialized_group.data

        response_animal['group'] = response_group

        characteristics = AnimalCharacteristic.objects.filter(animal_id_id=animal_ID)

        serialized_characteristics = AnimalCharacteristicSerializer(characteristics)

        response_characteristics = [ info.__dict__ for info in [item for item in serialized_characteristics.__dict__['_args'][0]]]
        
        for item in response_characteristics:
            del item['_state']
            
            charact = Characteristic.objects.get(id=item['characteristic_id_id'])
            serialized_charact = CharacteristicSerializer(charact)
            response_charact = serialized_charact.data['name']
            del item['animal_id_id']
            del item['characteristic_id_id']

            item['name'] = response_charact
        response_animal['characteristics'] = response_characteristics
        
        return response_animal
        