from goods.serializers import GoodsSerializer
from .models import Goods
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics


class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
    '商品列表页'
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)