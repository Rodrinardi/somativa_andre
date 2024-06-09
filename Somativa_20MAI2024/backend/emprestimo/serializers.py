from rest_framework import serializers
from .models import *

class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['id','email','telefone','cpf','endereco','is_active','groups','user_permissions']
        many = True

class GeneroLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroLivro
        fields = '__all__'
        many = True

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Foto
        fields = '__all__'
        many = True

class LivrosSerializer(serializers.ModelSerializer):
    Foto = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    )
    GeneroLivroFK = GeneroLivroSerializer(read_only=True)
    class Meta:
        models = Livros
        fields = '__all__'
        many = True

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Emprestimo
        fields = '__all__'
        many = True

class EmprestimoLivrosSerializer(serializers.ModelSerializer):
    class Meta:
        models = EmprestimoLivros
        fields = '__all__'

        
