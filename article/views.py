import json
from datetime import date

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST

# Create your views here.
from article.models import Article

def home(request):
    art = Article.objects.get_random().first()  #Used for preview article
    top_10 = Article.objects.filter(publication_date__lte=date.today()).order_by("publication_date")[:10]
    today = date.today()
    return render(request, "list.html", {"page3_article": art,
                                         "top_10": top_10,
                                         "today": today,})

def article_details(request, **kwargs):
    art = get_object_or_404(Article, id = kwargs.get("art_id"))
    
    #To Use jQuery lets put it in session and receive in ajax.
    #Though there is no need to use jQuery in the requirment, but as this is a test assignment,
    # lets use jQuery for evalution.
    request.session["art_id"] = art.id

    return render(request, "details.html", {})


@require_POST
def article_details_ajax(request):
    art = Article.objects.get(id = request.session.get("art_id"))
    try:
        article_img = art.article_img.url
    except ValueError:
        # can be raised when there is no image
        article_img = ""

    response_data = {
        "title": art.title,
        "author" : art.author.username,
        "publication_date" : str(art.publication_date),
        "category" : art.category.name,
        "hero" : art.hero.url,
        'article_img' : article_img,
        'text' : art.text,
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")
