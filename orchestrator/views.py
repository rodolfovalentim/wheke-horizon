from django.utils.six import BytesIO
from django.views.generic import ListView
from django_tables2 import RequestConfig
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render

from .models import Host
from .serializers import HostSerializer
from .tables import HostTable


def index(request):
    host = Host(cpu=10, hd=11, mem=12, name='nfv-001')
    host2 = Host(cpu=12, hd=13, mem=14, name='nfv-010')
    host3 = Host(cpu=12, hd=13, mem=14, name='nfv-010')

    serializer = HostSerializer([host, host2, host3], many=True)
    serializer.data
    content = JSONRenderer().render(serializer.data)
    print(content)
    stream = BytesIO(content)
    print(stream)
    data = JSONParser().parse(stream)
    serializer = HostSerializer(data=data, many=True)
    print(repr(serializer))
    print(serializer.is_valid())
    print(serializer.validated_data)
    host_data = serializer.save()
    
    table = HostTable(host_data)
    RequestConfig(request).configure(table)
    return render(request, 'orchestrator/index.html', {'table': table})
