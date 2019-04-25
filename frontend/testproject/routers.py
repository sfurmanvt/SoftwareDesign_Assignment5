from rest_framework import routers
from comment.viewsets import CommentViewSet

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)
