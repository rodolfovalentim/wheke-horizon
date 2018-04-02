import django_tables2 as tables
from django_tables2.utils import A
from .models import Host

class HostTable(tables.Table):
   
    class Meta:
        model = Host
        template_name = 'django_tables2/bootstrap.html'
        fields = ('id','name',
                  'cpu', 'mem', 'hd')
        # attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no host matching the search criteria..."