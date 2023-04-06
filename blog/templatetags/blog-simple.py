from django import template
from blog.models import post
from blog.models import category

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
    six_latest_post = posts[:6]
    return {
        "posts": six_latest_post
    }

@register.inclusion_tag("category.html")
def ccategory():
    cat_dict = {}
    cat = category.objects.all()
    for i in cat:
        cat_dict[i] = post.objects.filter(category=i).count()
    return {
        'category':cat_dict
    }
    



