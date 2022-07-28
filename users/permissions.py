from rest_framework.permissions import BasePermission
from rest_framework.views import Request

# O arquivo permissions.py conterá a lógica
  
# Classe UserPermission herda de BasePermission
# classe que contem toda a lógica de permissões do DRF  
class UserPermission(BasePermission): 
    # Funão has_permission verifica os métodos de admin 
    # setados na variável staff_methods (métodos de funcionários)
    def has_permission(self, request: Request, _):
        staff_methods = {
            "GET",
        }

        # Caso o método da requisição esteja setado
        # em staff_methods ele retornara True ou False
        # de acordo com o staff do usuário. Sendo false, a permissão é negada
        if request.method in staff_methods:
            return request.user.is_superuser

        # Caso o método requisitado não esteja restrito
        # a requisição será permitida
        return True