from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound , HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenge={

      "january":"This month is called january",
      "febuary":"this month is called febuary",
      "march":"This month is called MARCH",
      "april":"This month is called APRIL",
      "may":None,
      "june":"This month is called JUNE",
      "july":"This month is called JULY",
      "august":None,
      "september":"This month is called SEPTEMBER",
      "october":"This month is called OCTOBER",
      "november":"This month is called NOVEMBER",
      "december":None


}

# Create your views here.

def index(request):
   # list_items=""
    items_num=list(monthly_challenge.keys())
    return render(request, "laabka/index.html", {

        "bilaha":items_num

    } )


    """
    for dooro in items_num:
        
        items_capitalize=dooro.capitalize()
        item_path= reverse("saxaha", args=[dooro])
        list_items+=f"<li><a href=\"{item_path}\"> {items_capitalize}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    
    return HttpResponse(response_data)
    """

def choose_num(request, dooro):
    type_num=list(monthly_challenge.keys())
    if dooro>len(type_num):
        raise Http404()
       # jawaabta= render_to_string("404.html")
       # return HttpResponse(jawaabta)
    ubadal=type_num[dooro-1]  
    redirec_path=reverse("saxaha", args=[ubadal])
    return HttpResponseRedirect(redirec_path) 
    


def choose(request, dooro):
    try:
    
        choose_month= monthly_challenge[dooro]
        title_name=monthly_challenge.keys()
        #html_form=f"<h1>{choose_month}</h1>"
      #  html_form= render_to_string("laabka/home.html")
       # return HttpResponse(html_form)
        return render(request, "laabka/home.html", {
            "muujin": choose_month,
            "title": dooro
            
        })
    except:
        raise Http404()  
         #respons_data=render_to_string("404.html")
         #return HttpResponseNotFound(respons_data)