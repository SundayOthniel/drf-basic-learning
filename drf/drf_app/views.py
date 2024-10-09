# from rest_framework.response import Response
# from .serializers import PersonSerializer
# from .models import Person
# from rest_framework.decorators import api_view
# from rest_framework import status
# from rest_framework.views import APIView
# from django.shortcuts import get_list_or_404, get_object_or_404
# from rest_framework import generics, mixins


# ###Class based view###
# class PersonRequest(APIView):
#     def get(self, request, format=None):
#         persons = Person.objects.all()
#         person_serializer = PersonSerializer(persons, many=True)
#         return Response(person_serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, format=None): 
#         person_data = PersonSerializer(data=request.data)
#         if person_data.is_valid():
#             person_data.save()
#             return Response(person_data.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(person_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Functionbased view
'''@api_view(['GET', 'POST'])
def personRequest(request, format=None):
    if request.method == 'GET':
        person = Person.objects.all()
        person_serializer = PersonSerializer(person, many=True)
        return Response(person_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        person_data = PersonSerializer(data=request.data)
        if person_data.is_valid():
            person_data.save()
            return Response(person_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(person_data.errors, status=status.HTTP_400_BAD_REQUEST )'''
    
# ###Class based view###
# class PersonUpdate(APIView):
#     def get(self, request, id, format=None):
#         person = get_object_or_404(Person, id=id)
#         person_serializer = PersonSerializer(person)
#         return Response(person_serializer.data, status=status.HTTP_200_OK)
    
#     def delete(self, request, id, format=None):
#         person = get_object_or_404(Person, id=id)
#         person.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, id, format=None):
#         person = get_object_or_404(Person, id=id)
#         person_serializer = PersonSerializer(person, data=request.data)
#         if person_serializer.is_valid():
#             person_serializer.save()
#             return Response(person_serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def  patch(self, request, id, format=None):
#         person = get_object_or_404(Person, id=id)
#         person_serializer = PersonSerializer(person, data=request.data, partial=True)
#         if person_serializer.is_valid():
#             person_serializer.save()
#             return Response(person_serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Function based view
'''@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def personUpdate(request, id, format=None):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        person_serializer = PersonSerializer(person)
        return Response(person_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        person_serializer = PersonSerializer(person, data=request.data)
        if person_serializer.is_valid():
            person_serializer.save()
            return Response(person_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        person_serializer = PersonSerializer(person, data=request.data, partial=True)
        if person_serializer.is_valid():
            person_serializer.save()
            return Response(person_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''

# class PersonRequest(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Snippet
from rest_framework import viewsets, renderers
from rest_framework.decorators import action


class userList(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class userList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('userList', request=request, format=format),
#         # 'snippets': reverse('UserDetail', request=request, format=format)
#     })

# from rest_framework import renderers

# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)