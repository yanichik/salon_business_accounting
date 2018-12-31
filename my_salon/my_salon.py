

def salon_db_setup:
    """setup database"""

def salon_add_to_db:
    """adds to DB.
    Must pass all relevant information into function.
    Return success acknowledgement"""

def salon_server_setup:
    """server setup to allow access to application on the internet"""

def salon_user_interface:
    """setup user interface"""

def salon_password_security:
    """implement username & password protection together with password recovery capability"""

def salon_main_menu:
    """menu display:
    Add Purchase
    Add Client
    Purchase History
    service type: list of services with option to add services available
    client name
    client id (running number), auto-generated
    amount payed
    payment method: check or cash
    other purchased items
    """

def salon_menu_selection:
    """returns menu selection"""

def salon_add_purchase:
    """Add purchase: Service or Product
    Service:
            choose service type
            add service type
    Product:
            choose product
            add product type"""

def salon_add_service_type:
    """Add service type in 'salon_add_purchase' menu selection"""

def salon_add_product_type:
    """Add product type in 'salon_add_purchase' menu selection"""



def add_client:
    """Add client to DB"""


# main
while True:
    print(salon_print_main_menu())