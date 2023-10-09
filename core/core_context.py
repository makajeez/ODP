from .helpers_sub import ( getSitePhone, getSiteEmail, getSiteAddress, 
                            getSiteSocial, getSiteTagline, DaboLinux, 
                            getSitePartners, getAnalyticsId,
                        )


def UniversalContext(request):
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    # web services or social APIs
    context = {}
    context['phone'] = getSitePhone()
    context['site_email'] = getSiteEmail()
    context['address'] = getSiteAddress()
    context['phones'] = getSitePhone(3)
    context['facebook'] = getSiteSocial('facebook')
    context['twitter'] = getSiteSocial('twitter')
    context['linkedin'] = getSiteSocial('linkedin')
    context['instagram'] = getSiteSocial('instagram')
    context['pinterest'] = getSiteSocial('pinterest')
    context['youtube'] = getSiteSocial('youtube')
    context['site_tags'] = getSiteSocial('site_tags')
    context['site_keywords'] = getSiteSocial('site_keywords')
    context['site_geo_placename'] = getSiteSocial('site_geo_placename')
    context['site_geo_position'] = getSiteSocial('site_geo_position')
    context['google_meta'] = getSiteSocial('google_meta')
    context['yandex_meta'] = getSiteSocial('yandex_meta')
    context['bing_meta'] = getSiteSocial('bing_meta')
    context['propeller_meta'] = getSiteSocial('propeller_meta')
    context['tagline'] = getSiteTagline()
    context['provider'] = DaboLinux()
    context['google_analytics_id'] = getAnalyticsId()
    context['partners'] = getSitePartners()
    egg = True if request.user.is_superuser else False
    print('[DEBUG]: User is admin: ', egg)
    context['is_admin'] = egg
    return context

