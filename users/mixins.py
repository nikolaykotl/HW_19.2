from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class UserRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.is_authenticated:
            if request.user != self.get_object().owner or request.user.is_staff:
                messages.info(request, 'Изменение доступно только авторизованому пользователю (владельцу)')
                return redirect('catalog:home')
        return super().dispatch(request,*args, **kwargs)