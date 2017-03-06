from django.views.generic import FormView
from django.contrib import messages

from .forms import UploadForm
from .helpers import CreditCard


class Index(FormView):
    template_name = 'index.html'
    form_class = UploadForm
    success_url = '/'
    success_messages = []

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.calculated_field,
        )

    def form_valid(self, form):
        if form.cleaned_data['text'] != '':
            lines = form.cleaned_data['text'].splitlines()
            for line in lines:
                card = CreditCard(line)
                messages.info(self.request, card.check_valid())

        if form.cleaned_data['file']:
            lines = form.cleaned_data['file'].read().decode('utf-8')

            for line in lines.splitlines():
                card = CreditCard(line)
                messages.info(self.request, card.check_valid())

        return super(Index, self).form_valid(form)
