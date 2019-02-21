from django.conf.urls import url
from app01 import views

urlpatterns = [

    # 删除功能三合一
    url(r'del_(publisher|book|author)/(\d+)/',views.delete,name='delete'),


    url(r'^publisher/', views.publisher_list, name='publisher'),

    url(r'^add_publisher/', views.add_publisher),
    # url(r'^add_publisher/', views.AddPublisher.as_view()),
    # url(r'^add_publisher/', view),

    url(r'^del_pub/(\d+)/', views.del_publisher, name='del_pub'),
    # 编辑出版社
    url(r'^edit_publisher/', views.edit_publisher),
    # 测试的url
    url(r'^test/', views.test),

    # 展示书籍
    url(r'^book_list/', views.book_list,name='book'),

    # 增加书籍
    url(r'^add_book/', views.add_book),

    # 删除书籍
    url(r'^del_book/', views.del_book),

    # 编辑书籍
    url(r'^edit_book/', views.edit_book),

    # 展示作者
    url(r'^author_list/', views.author_list,name='author'),

    # 增加作者
    url(r'^add_author/', views.add_author),

    # 删除作者
    url(r'^del_author/', views.del_author),

    # 编辑作者
    url(r'^edit_author/', views.edit_author),
]


