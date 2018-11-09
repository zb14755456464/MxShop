from django.conf.urls import url,include
import xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet,CategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from users.views import SmsCodeViewset,UserViewset
from user_operation.views import *


router = DefaultRouter()

#配置goods的url
router.register(r'goods', GoodsListViewSet)
router.register(r'categorys', CategoryViewSet, base_name="categorys")

# 用户
router.register(r'code', SmsCodeViewset, base_name="code")
router.register(r'users', UserViewset, base_name="users")
router.register(r'userfavs', UserFavViewset, base_name="userfavs")
router.register(r'messages', LeavingMessageViewset, base_name="messages")
router.register(r'address',AddressViewset , base_name="address")

# 购物车
from trade.views import ShoppingCartViewset,OrderViewset
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")
router.register(r'orders', OrderViewset, base_name="orders")

from goods.views import BannerViewset,IndexCategoryViewset
router.register(r'banners', BannerViewset, base_name="banners")
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")




from django.views.generic import TemplateView
from trade.views import AlipayView
urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'docs/', include_docs_urls(title="慕学生鲜")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^', include(router.urls)),
    url(r'^login/$', obtain_jwt_token),
    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^alipay/return/', AlipayView.as_view(), name="alipay"),
    url('', include('social_django.urls', namespace='social'))
]
