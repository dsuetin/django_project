from .models import Category

def categories(request):
    """ return categories list

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return {
        'categories': Category.objects.all()
    }