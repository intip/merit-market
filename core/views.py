from django.core.urlresolvers import reverse
from django.db.models import Q
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

    def form_valid(self, form):
        """
        Giver is logged user in request
        """
        self.object = form.save(commit=False)
        self.object.giver = self.request.user.customer
        self.object.save()
        return HttpResponseRedirect(self.get_absolute_url())

    def get_absolute_url(self):
        return reverse('transaction')

    def get_contenxt_data(self, *args, **kwargs):
        context = super(TransactionCreateView,
                        self).get_contenxt_data(*args, **kwargs)

        my_transactions = Transaction.objects.filter(
            Q(giver=self.request.user) | Q(receiver=self.request.user)
        ).order_by('-transaction_time')[:15]

        context['my_transactions'] = my_transactions

        return context
