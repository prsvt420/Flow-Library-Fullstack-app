
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from book.views import BookViewSet, BookCountView, TagViewSet

router: routers.DefaultRouter = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/count/', BookCountView.as_view(), name='book-count'),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
