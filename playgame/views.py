from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Game
from django.db.models import Q


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Play(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'play.html'



    def create_game(request):
        #Game.objects.all().delete() # for testing purposes
        exists = Game.objects.filter(player_1 = request.user.id, player_2 = None)
        if not exists:
            row = Game.objects.create(player_1 = request.user.id)
            row.save()
            current_game = Game.objects.latest('game_id')
            player2 = "Waiting for Second Player to Join"
            context = {'current_game':current_game, 'player2':player2}
            return render(request, 'create.html', context)
        else:
            context = {'current_game': '0', 'player2': 'Me'}
            return render(request, 'create.html', context)


def join(request):
    if request.method == 'GET':
        game_id = request.GET.get('game_id')
        join_game = Game.objects.get(game_id = game_id)
        if join_game:
            if join_game.player_2 == None:
                join_game.player_2 = request.user.id
                join_game.save()
        context = {'game_id': game_id}
        context['specs'] = join_game
    return render(request, 'joingame.html', context)


class Games(generic.CreateView):
    template_name = 'join.html'
    form_class = UserCreationForm

    def join_game_list(request):
        avail = Game.objects.filter(~Q(player_1 = request.user.id), player_2 = None) # not equal to
        involved = Game.objects.filter( ~Q(player_2 = None), Q(player_1=request.user.id)| ~Q(player_1 = None),
                                       player_2=request.user.id )
        if not avail:
            context = {'join_list':''}
            #return render(request, 'join.html', context)
        else:
            context = {'join_list': avail}
        if not involved:
            context['involved_list']=""
                # return render(request, 'join.html', context)
        else:
            context['involved_list'] = involved

        return render(request, 'join.html', context)

    def get_queryset(self):
        """Return the last five published questions."""
        return Game.objects.order_by('-pub_date')[:5]







