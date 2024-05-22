from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'livros',LivrosView)
router.register(r'emprestimo',EmprestimoView)
router.register(r'emprestimo-livros',EmprestimoLivrosView)
router.register(r'usuarios',UsuarioCustomizadoView)

urlpatterns = router.urls
