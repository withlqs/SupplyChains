import datetime
from django.utils import timezone
from main.models import Para
# from main import models
# from models import Para


class StatusMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            request.user.last_login = timezone.now()
            request.user.save()





# class LastActivityMiddleware(object):

#     def process_request(self, request):

#         # NOTE: This could cause performance issues in the future, but considering
#         # the current traffic rates we have right now it shouldn't be a problem.
#         if request.user.is_authenticated():
#             request.user.last_activity = timezone.now()
#             request.user.save()




# class UpdateLastActivityMiddleware(object):
    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     assert hasattr(request, 'user'), 'The UpdateLastActivityMiddleware requires authentication middleware to be installed.'
    #     if request.user.is_authenticated():
    #         Para.objects.filter(Username=username) \
    #                        .update(last_activity=timezone.now())