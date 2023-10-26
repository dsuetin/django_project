from .basket import Basket


def basket(request):
    """
    A context processor that provides the basket in the template.
    """
    return {'basket': Basket(request)}
