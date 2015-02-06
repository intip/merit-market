from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Transaction, Customer


class IndexView(TemplateView):
    template_name = 'index.html'


class TransactionCreateView(CreateView):
    model = Transaction
    fields = ('receiver', 'qtty', 'comment', )
    template_name = 'transaction.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TransactionCreateView,
                        self).get_context_data(*args, **kwargs)
        context['customer'] = Customer.objects.get(pk=self.request.user.id)
        return context

    def save_form(self, *args, **kwargs):
        print 666
