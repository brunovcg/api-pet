from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Animal
from group.models import Group
from characteristic.models import Characteristic
from .serializers import AnimalSerializer
from django.core.exceptions import ObjectDoesNotExist

class AnimalView(APIView):
    def get(self, request):

        all_info = Animal.objects.all()

        serialized = AnimalSerializer(all_info, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)

    def post(self, request):

        name = request.data['name']
        age = request.data['age']
        weight = request.data['weight']
        sex = request.data['sex']
        group = request.data['group']
        characteristics = request.data['characteristics']

        add_group = Group.objects.get_or_create(**group)
        
        new_animal = Animal.objects.create(name=name, age= age, weight = weight, sex=sex, group=add_group[0])

        for charact in characteristics:    

            add_charact = Characteristic.objects.get_or_create(name=charact['name'])
            new_animal.characteristics.add(add_charact[0])

        serialized = AnimalSerializer(new_animal)               

        return Response(serialized.data, status=status.HTTP_201_CREATED)


class AnimalFilterView(APIView):
    def get(self, request, animal_ID=''):
        
        try:
            animal = Animal.objects.get(id=animal_ID)
            serialized = AnimalSerializer(animal)

        except ObjectDoesNotExist:
            return Response({'error': 'ID not found'}, status=status.HTTP_404_NOT_FOUND)
       
        return Response(serialized.data, status=status.HTTP_200_OK)


    def delete(self, request, animal_ID=''):

        try:
            animal = Animal.objects.get(id=animal_ID)
            animal.delete()

        except ObjectDoesNotExist:
            return Response({'error': 'ID not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response('', status=status.HTTP_204_NO_CONTENT)
