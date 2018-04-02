from .models import Host
from rest_framework import serializers

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'
        # fields = ('id', 'cpu', 'hd', 'mem', 'name')