from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Animal, AnimalCharacteristic
from group.models import Group
from characteristic.models import Characteristic
from group.serializers import GroupSerializer
from characteristic.serializers import CharacteristicSerializer
from django.core.exceptions import ObjectDoesNotExist
from .controllers import get_one_animal


class AnimalView(APIView):
    def get(self, request):

        all_info = Animal.objects.all()
        all_animals_id = [item.__dict__['id'] for item in all_info]
        response  = [get_one_animal(animal) for animal in all_animals_id]       

        return Response(response, status=status.HTTP_200_OK)


    def post(self, request):

        info = request.data 
        group = info['group']
        characteristics = info['characteristics']
        animal = info

        del animal['group']
        del animal['characteristics']
  
        try:          
            group_add = Group.objects.filter(name=group['name'])
            serialized_group = GroupSerializer(group_add, many=True)
            group_id = serialized_group.data[0]['id']          
        
        except Exception:
            Group.objects.create(**group)
            group_add = Group.objects.filter(name=group['name'])
            serialized_group = GroupSerializer(group_add, many=True)
            group_id = serialized_group.data[0]['id']
     
        animal_data = {**animal}

        animal_data['group'] = Group.objects.get(id=group_id)
        
        new_animal = Animal.objects.create(**animal_data)

        for charact in characteristics: 

            try:
                charact_add = Characteristic.objects.get(name=charact['name'])

            except Exception:
            
                charact_search = Characteristic.objects.filter(name=charact['name'])
                serialized_charact = CharacteristicSerializer(charact_search, many=True)                

                if len(serialized_charact.data) == 0:
                    charact_add = Characteristic.objects.create(**charact)

            new_table = {'animal_id' : new_animal, 'characteristic_id' : charact_add}

            AnimalCharacteristic.objects.create(**new_table)

        response = get_one_animal(new_animal.id)                    

        return Response(response, status=status.HTTP_201_CREATED)


class AnimalFilterView(APIView):
    def get(self, request, animal_ID=''):
        
        try:
            Animal.objects.get(id=animal_ID)
            response = get_one_animal(animal_ID)

        except ObjectDoesNotExist:
            return Response({'error': 'ID not found'}, status=status.HTTP_404_NOT_FOUND)
       
        return Response(response, status=status.HTTP_200_OK)


    def delete(self, request, animal_ID=''):

        try:
            animal = Animal.objects.get(id=animal_ID)
            animal.delete()

        except ObjectDoesNotExist:
            return Response({'error': 'ID not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response('', status=status.HTTP_204_NO_CONTENT)
