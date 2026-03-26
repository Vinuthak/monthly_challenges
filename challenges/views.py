from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat only healthy food!"
    elif month == "february":
        challenge_text = "Walk for 30 minutes!"
    elif month == "march":
        challenge_text = "learn 3 hours of django everyday!"
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)
