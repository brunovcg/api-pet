from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AnimalView(APIView):
    def get(self, request):


        return Response({'message': 'hello Kenzie'}, status=status.HTTP_200_OK)


    def post(self, request):

        anwser = request.data['teste']

        return Response({'message': f'{anwser}'}, status=status.HTTP_201_CREATED)


class AnimalFilterView(APIView):
    def get(self, request, animal_id=''):
        return Response({'message': f'{animal_id}'}, status=status.HTTP_200_OK)


    def delete(self, request, animal_id=''):
        return Response({'message': 'hello Kenzie'}, status=status.HTTP_204_NO_CONTENT)


