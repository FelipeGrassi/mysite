from django.http import HttpResponse
from django.views import generic

class PostView(generic.View):
    queryset= Post.obejct.filter(status=1).order_by("created_on")
    template_name="index.html"
    def get(self,request,*args,**kwargs):
        return HttpResponse("eai")


class PostDetail(generic.DetailView):
    model= Post
    template_name = "post_detail.html"
