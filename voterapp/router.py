from voter.api.viewsets import Userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', Userviewsets, basename ='user_api')
