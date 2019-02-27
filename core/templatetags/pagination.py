from django.template import Library

register = Library()

@register.inclusion_tag('pagination.html')
def pagination(request, paginator, page_obj):
    context = {}
    context['request'] = request
    context['paginator'] = paginator
    context['page_obj'] = page_obj

    getvars = request.GET.copy()
    if 'page' in getvars:
        del getvars['page']
    elif len(getvars) > 0:
        context['getvars'] = f'&{getvars.urlencode()}'
    else:
        context['getvars'] = ''

    return context