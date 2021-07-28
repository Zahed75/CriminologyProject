from .models import HeaderAndFooter

def headerfooter(request):
    header_footer = HeaderAndFooter.objects.all()
    return {'header_footer': header_footer}