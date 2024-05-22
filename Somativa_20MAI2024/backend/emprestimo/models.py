from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .gerenciador import Gerenciador

class UsuarioCustomizado(AbstractBaseUser,PermissionsMixin):
     email = models.EmailField("endereço de email", unique=True)
     is_staff = models.BooleanField(default=False)
     is_active = models.BooleanField(default=True)
     telefone = models.CharField(max_length=15, null=True, blank=True)
     endereco = models.CharField(max_length=200)
     cpf = models.CharField(max_length=20)
     is_email_verified = models.BooleanField(default=False)

     objects = Gerenciador() 

     USERNAME_FIELD = "email"
     REQUIRED_FIELDS = []

     def __str__(self):
          return self.email
     

class Foto(models.Model):
    url = models.CharField(max_length=3000)

    def __str__(self):
        return self.url
    


CLASSIFICACAO_INDICATIVA = [

    ('L','LIVRE'),
    ('10','10 anos'),
    ('12','12 anos'),
    ('14','14 anos'),
    ('16','16 anos'),
    ('18','18 anos')
   
]



CATEGORIA_LIVRO = [
    ("T", "TERROR"),
    ("R", "ROMANCE"),
    ("A", "AVENTURA"),
    ("M", "MISTÉRIO"),
    ("FC", "FICÇÃO CIENTÍFICA"),
    ("D", "DRAMA"),
    ("C", "CRIME"),
    ("H", "HISTÓRIA"),
    ("B", "BIOGRAFIA"),
    ("E", "ENSINO"),
    ("P", "POESIA"),
    ("AA", "AUTOAJUDA"),
    ("F", "FANTASIA"),
    ("LIJ", "LITERATURA INFANTO-JUVENIL")
    
]


FORMATO_LIVRO = [
 
    ("E", "EBOOK"),
    ("F", "FÍSICO")
    
   


]

APROVACAO_LIVRO = [
    ("P", "PENDENTE"),
    ("C", "CANCELADO"),
    ("A","APROVADO")
]

class Livros(models.Model):
    titulo = models.CharField(max_length=45)
    nota = models.IntegerField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    autor = models.ForeignKey(UsuarioCustomizado, related_name='autorLivro', on_delete=models.CASCADE)
    descricao = models.TextField()
    editora = models.CharField(max_length=30)
    idade = models.CharField(choices=CLASSIFICACAO_INDICATIVA, max_length=35)
    dataLancamento = models.DateField(auto_now_add=True)
    publicacao = models.DateField()
    categoria = models.CharField(choices=CATEGORIA_LIVRO, max_length=30)
    fotoFK = models.ForeignKey(Foto, related_name='fotoLivro', on_delete=models.CASCADE)
    numeroPaginas = models.IntegerField()
    formato = models.CharField(choices=FORMATO_LIVRO, max_length=30)
    codEdicao = models.CharField(max_length=25)
    aprovado = models.CharField(choices=APROVACAO_LIVRO, max_length=25)

    def __str__(self):
        return self.titulo


STATUS_EMPRESTIMO = [
    ("P","PENDENTE"),
    ("A","APROVADO"),
    ("R","RECUSADO"),
    ("C","CANCELADO"),
]


class Emprestimo(models.Model):
    usuarioFK = models.ForeignKey(UsuarioCustomizado, related_name='usuarioEmprestimo', on_delete=models.CASCADE)
    dataEmprestimo = models.DateField(auto_now_add=True)
    devolucaoPrevista = models.DateField() #duas semanas depois da data emprestimo
    dataDevolucao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_EMPRESTIMO)

    def __str__(self):
            return self.status

class EmprestimoLivros(models.Model):
     livroFK = models.ForeignKey(Livros, related_name='Emprestimo_livro', on_delete=models.CASCADE)
     quantidade = models.IntegerField()
     emprestimoFK = models.ForeignKey(Emprestimo, related_name='livro_Emprestimo', on_delete=models.CASCADE)

     def __str__(self):
            return self.livroFK.titulo
    


# chatbot??????