from django.shortcuts import render
from django.views import View
from .forms import PeselForm, TextForm


class TextView(View):
    form_class = TextForm
    template_name = "ShuffleValidate/text_template.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            data = form.save()
            return render(
                request, self.template_name, {"shuffled_text": data.shuffled_text}
            )
        return render(request, self.template_name, {"form": form})


class PeselView(View):
    form_class = PeselForm
    template_name = "ShuffleValidate/pesel_template.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            pesel = form.save()
            return render(
                request,
                self.template_name,
                {
                    "validated": True,
                    "pesel": pesel,
                },
            )
        return render(request, self.template_name, {"form": form})
