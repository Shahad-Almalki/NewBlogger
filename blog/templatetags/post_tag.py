from django import template
from blog.models import Post, Comments

register = template.Library()
@register.inclusion_tag('blog/latests_posts.html')

def latest_posts ():
    context = {
        'l_posts': Post.objects.all()[0:5],
    }
    return context


@register.inclusion_tag('blog/latest_comments.html')

def latest_comments ():
    context = {
        'l_comments': Comments.objects.filter(active= True)[:5],
    }
    return context
