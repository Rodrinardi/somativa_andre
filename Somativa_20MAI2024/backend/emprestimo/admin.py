from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class AdminUsuarioCustomizado(UserAdmin):
    models=UsuarioCustomizado
    list_display = ['id', 'email', 'cpf']
    list_display_links = ('id', 'email', 'cpf',)
    fieldsets = (
        (None,{'fields': ('email','password')}),
        ('Permissions', {'fields': ('is_staff','is_active','groups','user_permissions',)}),
        ('Management', {'fields': ('last_login',)}),
        ('Custom fields', {'fields': ('cpf','telefone','endereco',)}),
    )
    filter_horizontal = ('groups','user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1','password2', 'is_staff','is_active','groups','user_permissions',)
        }),
    )    
    search_fields = ['email',]
    ordering = ['email']

admin.site.register(UsuarioCustomizado,AdminUsuarioCustomizado)

class AdminFoto(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 10
    
admin.site.register(Foto,AdminFoto)

class AdminGeneroLivro(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 10

admin.site.register(GeneroLivro)

class AdminLivros(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'autor']
    list_display_links = ['id', 'titulo', 'autor']
    search_fields = ('titulo',)
    list_per_page = 10

admin.site.register(Livros, AdminLivros)

class AdminEmprestimo(admin.ModelAdmin):
    list_display = ['id', 'usuarioFK', 'dataEmprestimo', 'devolucaoPrevista']
    list_display_links = ['id','usuarioFK', 'dataEmprestimo', 'devolucaoPrevista']
    search_fields = ('usuarioFK',)
    list_per_page = 10

admin.site.register(Emprestimo,AdminEmprestimo)

class AdminEmprestimoLivros(admin.ModelAdmin):
    list_display = ['id','livroFK', 'emprestimoFK']
    list_display_links = ['id','livroFK', 'emprestimoFK']
    search_fields = ('livroFK',)
    list_per_page = 10

admin.site.register(EmprestimoLivros,AdminEmprestimoLivros)