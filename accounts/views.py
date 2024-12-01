from django.views import generic

from accounts.models import Cook


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes")
