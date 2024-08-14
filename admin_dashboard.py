from flask import Blueprint,request
from classModules.visitorsClass import objVisitors
from classModules.adsClass import objAds
from classModules.productClickClass import objProductClick

admin_dashboard_buleprint = Blueprint(__name__,'admin_dashboard_buleprint')
@admin_dashboard_buleprint.route('/today-visitor',methods=['GET'])
def tVisitor():
    return objVisitors.todayvisitor()

@admin_dashboard_buleprint.route('/today-ad-click',methods=['GET'])
def tAdClick():
    return objAds.todayAdClick()

@admin_dashboard_buleprint.route('/today-product-clicks',methods = ['GET'])
def tPClick():
    return objProductClick.overallProductClick()

@admin_dashboard_buleprint.route('/visitor-trend',methods=['GET'])
def getVisitorTrend():
    return objVisitors.visitorsTrend()