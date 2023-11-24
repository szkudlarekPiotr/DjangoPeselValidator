from django.shortcuts import render
from django.views import View
from .forms import PeselForm, TextForm


# Create your views here.
class TextView(View):
    form_class = TextForm
    template_name = "ZadaniaRekrutacyjne/text_template.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            pass
        return render(request, self.template_name, {"form": form})


class PeselView(View):
    form_class = PeselForm
    template_name = "ZadaniaRekrutacyjne/pesel_template.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            pass
        return render(request, self.template_name, {"form": form})
