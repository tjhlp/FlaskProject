from . import cart_bp


@cart_bp.route('/info')
def get_cart():
    return 'cart/info'
