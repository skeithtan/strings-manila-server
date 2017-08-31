from django.conf.urls import url

from .shared_views import CancelOrderView
from .admin_views import OrderList, OrderDetail, VerifyOrderPayment
from .customer_views import OrdersView, OrderDetailView, SubmitPaymentView

order_api_urls = [
    url(r'^api/orders/$', OrderList.as_view()),
    url(r'^api/orders/(?P<order_id>(\d+))/$', OrderDetail.as_view()),
    url(r'^api/orders/(?P<order_id>(\d+))/cancel/$', CancelOrderView.as_view()),
    url(r'^api/orders/(?P<order_id>(\d+))/verify/$', VerifyOrderPayment.as_view()),
]

order_pages_urls = [
    url(r'^orders/$', OrdersView.as_view()),
    url(r'^orders/(?P<order_id>(\d+))/$', OrderDetailView.as_view()),
    url(r'^orders/(?P<order_id>(\d+))/submit-payment/$', SubmitPaymentView.as_view())
]

