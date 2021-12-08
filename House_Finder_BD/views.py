from django.views.generic import TemplateView


# Homepage
class HomePage(TemplateView):
    template_name = 'index.html'
