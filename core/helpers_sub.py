#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Ahmad Abdulnasir Shu'aib <donations@mssn.com>'
__homepage__ = https://ahmadabdulnasir.com.ng
__copyright__ = 'Copyright (c) 2019, salafi'
__version__ = "0.01t"
"""
from django.utils import timezone
from uuid import uuid4
from core.models import SiteInformation, Partner

class Egg:
    title = "Page Not Created"
    slug = "Page Not Created"
    sub_title = "Sorry This Page is Not Created Yet !!"
    body = sub_title
    img = None
    pub_date = timezone.now()
    extra_info = None

    def __str__(self):
        return self.title

def getUniqueId():
    tmp = uuid4()
    tmp_ = str(tmp).split('-')[0]
    return tmp_

def LongUniqueId():
    tmp = uuid4()
    return tmp

def siteLoginUrl():
    return 'accounts/login/'

def themeVersion():
    ''' return the current active theme/template '''
    try:
        theme = SiteInformation.objects.filter(slug__contains='default-theme').order_by('-updated').first()
        theme = theme.info
    except Exception as e:
        theme = 'v3/'
    finally:
        # print(theme)
        if theme.endswith('/'):
            return theme
        else:
            return theme+'/'

def getSitePhone(num=0):
    try:
        phones = SiteInformation.objects.filter(slug__contains='phone')
        if num>0:
            return phones[:num]
        else:
            return phones[num]
    except Exception as e:
        return '+2348035971242'

def getSiteEmail():
    try:
        email = SiteInformation.objects.filter(slug__contains='email').order_by('-updated').first()
        if not email:
            mail = 'donations@mssn.com'
        else:
            mail =  email.info
    except Exception as e:
        mail =  'donations@mssn.com'
    finally:
        return mail

def getSiteAddress():
    try:
        address = SiteInformation.objects.filter(slug__contains='address').order_by('-updated').first()
        if not address:
            address = 'donations@mssn.com'
        else:
            address =  address.info
    except Exception as e:
        address =  'donations@mssn.com'
    finally:
        return address

def getSiteSocial(social='twitter'):
    try:
        site = SiteInformation.objects.filter(slug__contains=social).order_by('-updated').first()
        if not site:
            site = 'https://ahmadabdulnasir.com.ng'
        else:
            site =  site.info
    except Exception as e:
        site =  'https://ahmadabdulnasir.com.ng'
    finally:
        return site

def getSiteTagline():
    try:
        info = SiteInformation.objects.filter(slug__contains='tagline').order_by('-updated').first()
        if not info:
            info = 'MSSN Online donation platform'
        else:
            info =  info.info
    except Exception as e:
        info =  'MSSN Online donation platform'
    finally:
        return info

def getAnalyticsId():
    try:
        info = SiteInformation.objects.filter(slug__contains='analytics').order_by('-updated').first()
        if not info:
            info = ''
        else:
            info =  info.info
    except Exception as e:
        info =  ''
    finally:
        return info

def getSiteMedia(num=0):
    try:
        media = GalleryImage.objects.all()
        if num !=0:
            print(len(media))
            return media[:num]
        else:
            print(len(media))
            return media[num]
    except Exception as e:
        return []

def getSitePartners():
    try:
        partners = Partner.objects.all().order_by('-updated')
        return partners
    except Exception as e:
        return []


def getPaymentKey(value):
    # value = value+' payment'
    try:
        info = SiteInformation.objects.get(slug=value)
        if not info:
            print('[DEBUG]: Payment Key Not Found, Using Test Key')
            info = 'pk_test_458dadb7d4acad50c5dd5226a22588ab20139778'
        else:
            info =  info.info
            print('[DEBUG]: Payment Key Found', info)
    except Exception as e:
        print('[DEBUG]: Payment Key Not Found Exception, Using Test Key')
        info =  'pk_test_458dadb7d4acad50c5dd5226a22588ab20139778'
        print(e)
    finally:
        return info




class DaboLinux:
    def __init__(self):
        self.name = "MSSN Onine Donations Platform"
        self.description = "A platform for students to make donation and non students to offer anonymous donations"
        self.sale_email = 'donations@mssn.com'
        self.contact_email = 'donations@mssn.com'
        self.phones = ['+2348012345678', '+2348187654321']
        self.title = 'MSSN Donation'
        self.website = 'https://www.mssn.com'
        self.short = 'MSSN'
        self.short_software_name = 'MSSN'
        _, q = self.info(), self.developer()

    def developer(self):
        self.dev_name = 'Ahmad Abdulnasir Shuaib'
        self.dev_p_email = 'donations@mssn.com'
        self.dev_email = 'ahmad@dabolinux.com'
        self.dev_phone = '+2348035971242'
        self.dev_website = 'https://ahmadabdulnasir.com.ng/me/'
        return self.dev_name
    def info(self):
        self.text = '''
        <p>{0} started in 2018 with a single bit of code to enhance the record management
         in primary and secondary schools in Nigeria. Since then it has grown with more 
         features that involve financial managment and tracking as well as easy data accessibility
         by users. The primary goal of building this software is to simplify the traditional methods
         of storing, managing and processing data in all e-commerce shops.</p>
        <p>Everything you see here, from the documentation to the code itself,
        was created by the team of <a href="{1}" target="_blank">{2}</a>. who still maintain the softawre. 
        All issues and bugs concerning this software are to be submitted to 
        <a href="{1}" target="_blank">{2}</a>.</p>
        <p>This software is Property of {2}</p>
        <p>This Software may be sold or marketted by a third party partner,
        but  will still maintain the licence of <a href="{1} target="_blank"">{2}</a></p>

        <p>For more Information, reach us on {3}</p>
        '''.format(self.name, self.website, self.short, self.contact_email)
        self.version = 'Version 0.1'
        self.last_update = '04<sup>th</sup> July, 2018</p>'


    def __str__(self):
        return self.name 
