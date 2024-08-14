from flask import Blueprint,request
from classModules.productClass import objProducts
from classModules.adsClass import objAds
from classModules.visitorsClass import objVisitors
from classModules.contactClass import objContact
from classModules.productClickClass import objProductClick
from classModules.cartClass import objCart
from classModules.ordersClass import objOrders

product_blueprint = Blueprint('product_blueprint',__name__)
@product_blueprint.route('/products',methods=['GET'])
def product():
    return objProducts.displayAllProducts()

@product_blueprint.route('/products/<product_id>',methods=['GET'])
def singleProduct(product_id):
    return objProducts.getSingleProduct(productId=product_id)

@product_blueprint.route('/track-ad-click',methods=['GET'])
def logAdsClick():
    return objAds.saveAdClick()

@product_blueprint.route('/track-visitors',methods=['GET'])
def logVisitors():
    return objVisitors.saveVisitor()

@product_blueprint.route('/save-contact',methods=['POST'])
def logcontact():
    
    #Receving the date from client / front end
    customerName = request.form['customerName']
    customerEmail = request.form['customerEmail']
    customerMobile = request.form['customerMobile']
    customerQuery = request.form['customerQuery']
    
    #check if name ,email ,mobile is empty
    if not customerName and not customerEmail and not customerMobile:
        return'[{"errFlag":1,"message":"some fields are empty"}]'
    return objContact.saveContact(customerName,customerEmail,customerMobile,customerQuery) 

@product_blueprint.route('/cart-items',methods=['GET'])
def cartAll():
    return objCart.getCartItems()

@product_blueprint.route('/cart-count',methods=['GET'])
def cartCount():
    return objCart.getCartCount()

@product_blueprint.route('/save-cart/<product_id>',methods=['GET'])
def logcart(product_id):
    return objCart.saveCart(product_id)

@product_blueprint.route('/remove-cart/<product_id>',methods=['GET'])
def removeCartItem(product_id):
    return objCart.removeItem(product_id)

@product_blueprint.route('/delete-cart/<product_id>',methods=['GET'])
def deleteCartItem(product_id):
    print("delete carts")
    return objCart.deleteCartItem(product_id)

@product_blueprint.route('/track-product-click/<product_id>')
def trackproductclick(product_id):
    return objProductClick.saveProductClick(product_id)

@product_blueprint.route('/orders-add',methods = ["POST"])
def addOrder():
    data = request.get_json()
    product_id = data.get('product_id')
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')
    return objOrders.insertOrder(product_id,name,email,phone,address)


@product_blueprint.route('/orders-count',methods=['GET'])
def ordersCount():
    print('loda')
    return objOrders.todaysOrdersCount()