"""Views for the SCGame."""
# # Serialize Python object to JSON string. 
# task_data = TaskSerializer(task).data 
 
# # Create Python object from JSON string.
# task_data = TaskSerializer(request.data)
# task = task_data.create() 

from django.contrib.auth import get_user_model
from .models import (
    deserialize_user, GameSession, GameSessionMember, GameSessionMessage
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from notifications.signals import notify
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from django.http import JsonResponse


class CheckLogIn(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def check(self, request, *args, **kwargs):
        #check if email already matches existing account
        r_user = request.user

        if User.objects.filter(email=r_user).exists():
            return(False) #matches, throws error
        else:
            return(True)
        


class GameSessionView(APIView):
    """Manage Game sessions."""

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        """create a new game session."""
        user = request.user

        game_session = GameSession.objects.create(owner=user)

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
        owner = game_session.owner #supplier

        if owner != user:  # Only allow non owners join the room
            game_session.members.get_or_create(
                user=user, game_session=game_session
            )

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
        """return all messages in a game session."""
        # return all submissions in a game 
        uri = kwargs['uri']

        game_session = GameSession.objects.get(uri=uri)
<<<<<<< HEAD

        submissions = [game_session_submissions.to_json()
                       for game_session_submission in game_session.submissions.all()]
=======
        messages = [game_session_message.to_json() 
            for game_session_message in game_session.messages.all()]
        submissions = [game_session_submissions.to_json() for game_session_submission in game_session.submissions.all()]

>>>>>>> parent of fed72be... fuck this
        return Response({
            'id': game_session.id, 'uri': game_session.uri,
            'submissions': submissions
        })

    def post(self, request, *args, **kwargs):
        """create a new message in a game session."""
        uri = kwargs['uri']
        message = request.data['message']
        submission = request.data['submission']

        user = request.user
        game_session = GameSession.objects.get(uri=uri)

<<<<<<< HEAD
        submit=GameSessionSerializer(post).data


        game_session_submission= GameSessionSubmission.objects.create(
            user=user, game_session=game_session, forecast1=forecast1, forecast2=forecast2, forecast3=forecast3, forecast4=forecase4, order=order)
=======
        game_session_message = GameSessionMessage.objects.create(user=user, game_session=game_session, message=message)
>>>>>>> parent of fed72be... fuck this
        #submission = {1:x, 2:x, 3:x, 4:x, order:x}
        game_session_submission=GameSessionSubmission.objects.create(user=user, game_session=game_session, submission = submission)


        GameSessionMessage.objects.create(
            user=user, game_session=game_session, message=message
        )

        GameSessionSubmission.objects.create(
            user=user, game_session=game_session, submission = submission
        )

        # notif_args = {'source': user, 'source_display_name': user.get_full_name(), 'category' :'game', 'action':'Sent', 'obj': game_session_message.id, 'short_description':'You have a new message', 'silent': True, 'extra_data':{'uri': game_session.uri}}

        notif_args = {'source': user, 'source_display_name': user.get_full_name(), 'category' :'game', 'action':'Sent', 'obj': game_session_message.id, 'short_description':'New Submission', 'silent': True, 'extra_data':{'uri': game_session.uri}}

        notify.send(
            sender=self.__class__, **notif_args, channels=['websocket']
        )

        return Response({
            'status': 'SUCCESS', 'uri': game_session.uri,  'submission', submission
            'user': deserialize_user(user)
        })

class GameParameterView(APIView):
    #depends buyer, supplier, or general manager


class FinancialView(APIView):
<<<<<<< HEAD
    pass
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
=======
>>>>>>> parent of fed72be... fuck this


class GraphView(APIView):


    # //TODO: Collect data from buyer page
    # //TODO: Store data
    # //TODO: Check if all buyers have submitted, advance game state if so
    # //TODO: If period is 0, initialize WIP and inventory
    # //TODO: Otherwise compute allocations for each supplier if method is not manual.

class UserCheck(APIView):


class BuyerGame(APIView):


class SupplierGame(APIView):

class GameManager(APIView):
<<<<<<< HEAD
    serializer_class = GameManagerSerializer

    def create(self, request, *args, **kwargs):
        pass

    def get(self,request):
        pass
        #return(render(request,html,{}))
    def post(self, request):
        pass

    pass


class Comments(APIView):
    """This class defines the create behavior of our rest api."""
    queryset = CommentLog.objects.all()
    serializer_class = CommentLogSerializer

    def perform_create(self, serializer):
        serializer.save()
=======

class Comments(APIView):
>>>>>>> parent of fed72be... fuck this


class ForecastHistoryView(APIView):


class InventoryView(APIView):
<<<<<<< HEAD

    # def get(self, request, version, pk):
    #     time = generateDemoTime(version, request.GET)
    #     bar = get_object_or_404(Bar, pk=pk)
    #     opening = Bar.getOpeningTime(time is not None)
    #     closing = Bar.getUpperTime(time)
    #     if Bar.now(time) >= opening:
    #         results = []
    #         for count in range(0, ((closing-opening).seconds/60)/MINS_PER_CHUNK):
    #             startTime = opening + timedelta(minutes=MINS_PER_CHUNK*count)
    #             endTime = startTime + timedelta(minutes=MINS_PER_CHUNK)
    #             # Only add if that time is valid
    #             results.append({
    #                 "label": "%s - %s" % (startTime.strftime("%I:%M %p"), endTime.strftime("%I:%M %p")),
    #                 "x": count,
    #                 "y": bar.getTodaysTimeActivity(startTime, endTime)
    #             })
    #         return JsonResponse({"results": results})
    #     else:
    #         return JsonResponse({"errors": {"now": "Tonight's data is not yet available."}}, status=400)

=======
>>>>>>> parent of fed72be... fuck this


class GameSetting(APIView):

<<<<<<< HEAD
    def get(self, request):
        return(render(request, 'gamesetting.html', {
            'xxx':request.GET.get(''),
            }))

    def post(self, request):
        pass


class exitGame(APIView):
    session_destroy()
    Logout = True
    # some exit game API
    # URL logout=true
=======

>>>>>>> parent of fed72be... fuck this
