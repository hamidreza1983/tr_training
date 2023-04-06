from django import template
from blog.models import post

register = template.Library()

@register.inclusion_tag('six.html')
def six():
    posts = post.objects.filter(status=1)[:5]
    context = {
        'posts' : posts
    }
    return context