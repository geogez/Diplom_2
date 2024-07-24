class APIEndpoints:

    base_url = 'https://stellarburgers.nomoreparties.site'

    register_user = f"{base_url}/api/auth/register"
    login_user = f"{base_url}/api/auth/login"
    logout_user = f"{base_url}/api/auth/logout"
    update_user_info = f"{base_url}/api/auth/user"
    create_order = f"{base_url}/api/orders"
    ingredients = f"{base_url}/api/ingredients"
    retrieve_orders = f"{base_url}/api/orders"