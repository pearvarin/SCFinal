"""Views for the chat app."""

from django.contrib.auth import get_user_model
# from django.shortcuts import render, get_object_or_404
# from django.views.generic import ListView, DetailView
# from django.http import JsonResponse

from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import BasicAuthentication

from notifications.signals import notify

# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from django.utils.six import BytesIO

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'users': reverse('users:user-list', request=request, format=format),
        # 'todos': reverse('todos:todo-list', request=request, format=format),
    })

class CheckLogIn(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def check(self, request, *args, **kwargs):
        # check if email already matches existing account
        r_user = request.user
        if User.objects.filter(email=r_user).exists():
            return(False)  # matches, throws error
        else:
            return(True)


class GameSessionView(APIView):  # a lot to fix
    """Manage Game sessions."""
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """create a new game session."""
        user = request.user
        game_session = GameSession.objects.create(Game=user)
        ##### GameSessionMember.user = user
        return Response({
            'status': 'SUCCESS', 'uri': game_session.uri,
            'message': 'New game created'
        })

    def patch(self, request, *args, **kwargs):
        """Add a user to a game session."""
        User = get_user_model()

        uri = kwargs['uri']
        username = request.data['username']
        user = User.objects.get(username=username)

        game_session = GameSession.objects.get(uri=uri)
        owner = game_session.owner  # supplier

        game_session.members.get_or_create(
            user=user, game_session=game_session)

        owner = deserialize_user(owner)
        members = [
            deserialize_user(game_session.user)
            for game_session in game_session.members.all()
        ]
        members.insert(0, owner)  # Make the owner the first member

        return Response({
            'status': 'SUCCESS', 'members': members,
            'message': '%s joined that game' % user.username,
            'user': deserialize_user(user)
        })


class GameSessionMessageView(APIView):
    """Create/Get Game session messages."""

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        # return all submissions in a game
        uri = kwargs['uri']
        game_session = GameSession.objects.get(uri=uri)
        messages = [game_session_message.to_json()
                    for game_session_message in game_session.messages.all()]
        submissions = [game_session_submissions.to_json()
                       for game_session_submission in game_session.submissions.all()]
        return Response({
            'id': game_session.id, 'uri': game_session.uri,
            'messages': messages, 'submissions': submissions
        })

    def post(self, request, *args, **kwargs):
        """create a new message in a game session."""
        uri = kwargs['uri']
        submission = request.data['submission']

        user = request.user
        game_session = GameSession.objects.get(uri=uri)

        game_session_message = GameSessionSubmission.objects.create(
            user=user, game_session=game_session, forecast1=forecast1, forecast2=forecast2, forecast3=forecast3, forecast4=forecase4, order=order)
        #submission = {1:x, 2:x, 3:x, 4:x, order:x}

        # notif_args = {'source': user, 'source_display_name': user.get_full_name(), 'category' :'game', 'action':'Sent', 'obj': game_session_message.id, 'short_description':'You have a new message', 'silent': True, 'extra_data':{'uri': game_session.uri}}

        notif_args = {'source': user, 'source_display_name': user.get_full_name(), 'category': 'game', 'action': 'Sent',
                      'obj': game_session_message.id, 'short_description': 'New Submission', 'silent': True, 'extra_data': {'uri': game_session.uri}}

        notify.send(
            sender=self.__class__, **notif_args, channels=['websocket']
        )

        return Response({
            'status': 'SUCCESS', 'uri': game_session.uri, 'submission': submission,
            'user': deserialize_user(user)
        })


class GameParameterView(APIView):
    # depends buyer, supplier, or general manager

    # get user id & user type

    if User.objects.get(username=username).user_type == 'S':  # if = supplier
        pass
    elif User.objects.get(username=username).user_type == 'GM':  # if game manager
        pass
    else:  # if buyer

        pass
    pass


class FinancialView(APIView):
    context_object_name = 'context'  # specify context variable to use for g eneric view

# class GenericView(ListView):
#     model = Publisher
#     context_object_name = 'context'

# class PublisherDetail(DetailView):

#     model = Publisher
#     queryset = Publisher.objects.all()

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(PublisherDetail, self).get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['book_list'] = Book.objects.all()
#         return context

# class PublisherBookList(ListView):

#     template_name = 'books/books_by_publisher.html'

#     def get_queryset(self):
#         self.publisher = get_object_or_404(Publisher,  name=self.args[0])
#         return Book.objects.filter(publisher=self.publisher)

#     queryset = Author.objects.all()

#     def get_object(self):
#         # Call the superclass
#         object = super(AuthorDetailView, self).get_object()

#         # Record the last accessed date
#         object.last_accessed = timezone.now()
#         object.save()
#         # Return the object
#         return object
#     # //TODO: Collect data from buyer page
#     # //TODO: Store data
#     # //TODO: Check if all buyers have submitted, advance game state if so
#     # //TODO: If period is 0, initialize WIP and inventory
#     # //TODO: Otherwise compute allocations for each supplier if method is not manual.


class UserCheck(APIView):
    pass


class BuyerGame(APIView):

    def confirmexit(self):
        if confirm('Are you sure you want to Exit? You will not be able to go back to this information') is True:
            exit_game()


class SupplierGame(APIView):
    pass


class GameManager(APIView):
    pass


class Comments(APIView):
    pass


class ForecastHistoryView(APIView):
    pass


class InventoryView(APIView):
    pass


class GameSetting(APIView):
    pass


class exitGame(APIView):
    session_destroy()
    Logout = True
    # some exit game API
    # URL logout=true


# serializers

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

        # api/urls.py

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer


class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer