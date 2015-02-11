from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .models import Transaction
from .mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'core/index.html'


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = ('receiver', 'qtty', 'comment', )
    template_name = 'core/transaction.html'
    success_url = '/'

    def form_valid(self, form):
        """
        Giver is logged user in request
        """
        self.object = form.save(commit=False)
        self.object.giver = self.request.user.customer
        self.object.save()
        return HttpResponseRedirect(self.get_absolute_url())
