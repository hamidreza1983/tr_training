from django import template
from blog.models import post

register = template.Library()
posts = post.objects.filter(status=1)



@register.simple_tag(name='post_tag')
def blog_tag(number:int= 0):
    return posts[:3]

@register.filter
def slicing(value:str, number:int):
    return value.split()[:number]

@register.inclusion_tag("popular.html")
def population():
    posts = post.objects.filter(status=1)
    return {
        "posts": posts,   
    }



