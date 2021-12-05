from rest_framework import serializers, status
from .models import Url
from datetime import date, datetime, timedelta

class UrlSerializer(serializers.ModelSerializer):
    """
        Url serializer.
    """
    hourly_hits = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()
    class Meta:
        model = Url
        fields = ('url', 'short_code', 'created_at', 'updated_at',
                  'count','hourly_hits')
        
    def get_hourly_hits(self, obj):
        return obj.hitslog_set.filter(created_at__gte = datetime.now()-timedelta(hours=1)).count()
    
    def get_count(self, obj):
        return obj.hitslog_set.count()