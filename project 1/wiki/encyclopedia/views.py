from django.shortcuts import render, redirect
import random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry_title):
    content = util.get_entry(entry_title)
    



