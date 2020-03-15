import datetime
import json

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action

from .models import Superhero
from django.shortcuts import get_object_or_404
from .serializers import SuperheroSerializer
from .serializers import MemberSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT,
                                   HTTP_400_BAD_REQUEST)
from django.core.serializers.json import DjangoJSONEncoder


class SuperheroViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving superheros.
    """
    serializer_class = SuperheroSerializer
    serializer_member = MemberSerializer

    def list(self, request):
        """list superhero object"""
        try:
            queryset = Superhero.objects.filter()
            serializer = SuperheroSerializer(queryset, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return HTTP_204_NO_CONTENT

    def retrieve(self, request, pk=None):
        try:
            queryset = Superhero.objects.filter()
            superhero = get_object_or_404(queryset, pk=pk)
            serializer = SuperheroSerializer(superhero)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response.status_code('There is not any entry for this key')

    def create(self, request):
        post_data = request.data
        squad_name = post_data['squad_name']
        hometown = post_data['hometown']
        active = post_data['active']
        formed = post_data['formed']
        members = {'squad_name': squad_name, 'hometown': hometown, 'active': active, 'formed': formed}
        data = {'squad_name': squad_name, 'hometown': hometown, 'active': active, 'formed': formed, "members": members}
        return Response(data=data, status=HTTP_201_CREATED)

    # @action(methods=['PUT'], url_path='superhero')
    # def partial_update(self, request, pk=None):
    #     json.JSONEncoder.default = lambda self, objt: (objt.isoformat() if isinstance(objt, datetime.date)else None)
    #     req_obj= Superhero.objects.get(pk=pk)
    #     obj = vars(req_obj)
    #     squad_name = obj['squad_name']
    #     hometown = obj['hometown']
    #     active = obj['active']
    #     formed = json.loads(json.dumps(obj['formed']))
    #     member_data = {'squad_name': squad_name, 'hometown': hometown, 'active': active, 'formed': formed}
    #
    #     update_data = Superhero()
    #     update_data.squad_name = squad_name
    #     update_data.hometown = hometown
    #     update_data.active = active
    #     update_data.formed = formed
    #     update_data.members = member_data
    #     update_data.save()
    #     return Response("Update Complete")

    def destroy(self, request, pk=None):
        obj = Superhero.objects.get(pk=pk)
        obj.delete()
        return Response("Entry Deleted Successfully.")

    @action(detail=True, methods=['GET'], url_path='members')
    def get_superhero_members(self, request, pk=None):
        superhero = get_object_or_404(Superhero, pk=pk)
        members1 = superhero.members
        return Response(members1)

    @action(detail=True, methods=['POST'], url_path='members')
    def post_values(self, request, pk=None):
        obj = get_object_or_404(Superhero, pk=pk)
        serializer = SuperheroSerializer(data=obj.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'items posted'})
        else:
            return Response(serializer.errors,
                            status=HTTP_400_BAD_REQUEST)


class MemberViewset(viewsets.ViewSet):
    serializer_class = MemberSerializer

    def list(self, request):
        """list superhero object"""
        queryset = Superhero.objects.filter('members')
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if request.method == 'GET':
            queryset = Superhero.objects.filter()
            member = get_object_or_404(queryset, pk=pk)
            serializer = MemberSerializer(member)
            response_data = serializer.data['members']
            return Response(response_data)

        # elif request.method == 'PUT' or request.method == 'PATCH':
        #     update_data = request.data
        #     return Response(vars(update_data))



    def create(self, request):
        post_data = request.data
        squad_name = post_data['squad_name']
        hometown = post_data['hometown']
        active = post_data['active']
        formed = post_data['formed']
        members = {'squad_name': squad_name, 'hometown': hometown, 'active': active, 'formed': formed}

        # data = {'squad_name': squad_name, 'hometown': hometown, 'active': active, 'formed': formed, "members": members}
        s = Superhero()
        s.squad_name = squad_name
        s.hometown = hometown
        s.active = active
        s.formed = formed
        s.members = members
        s.save()
        return Response('Success')

    def destroy(self, request, pk=None):
        obj = Superhero.objects.get(pk=pk)
        obj.delete()
        return Response("Member Entry Deleted Successfully.")

