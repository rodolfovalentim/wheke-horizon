from django.db import models

class Host(models.Model):
    __tablename__ = 'hosts'

    # id = models.PositiveIntegerField(primary_key=True)
    cpu = models.IntegerField()
    hd = models.IntegerField()
    mem = models.IntegerField()
    name = models.CharField(max_length=100)
    # host_ip = models.CharField(max_length=100)
    # availability_zone = models.CharField(max_length=100)
    # opf_dpip_brint = models.CharField(max_length=100)
    # opf_dpip_breth = models.CharField(max_length=100)
    # keyflow_switch_id = models.IntegerField()
    # port_map = models.CharField(max_length=100)
    # int_br_eth = models.IntegerField()