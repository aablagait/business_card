from django.views.generic import TemplateView


class NewMe(TemplateView):
    template_name = 'chat.html'
