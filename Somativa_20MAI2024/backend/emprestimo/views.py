from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status  

class UsuarioCustomizadoView(ModelViewSet):
    queryset = UsuarioCustomizado.objects.all()
    serializer_class = UsuarioCustomizadoSerializer
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = UsuarioCustomizado.objects.filter(id=user.id) 
    #     return queryset

class GeneroLivroView(ModelViewSet):
    queryset = GeneroLivro.objects.all()
    serializer_class = GeneroLivroSerializer

class LivrosView(ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
    
class EmprestimoView(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class EmprestimoLivrosView(ModelViewSet):
    queryset = EmprestimoLivros.objects.all()
    serializer_class = EmprestimoLivrosSerializer

# teste