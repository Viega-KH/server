from conlink.models import contactlink
def contactlink_context(request):
    contacts = contactlink.objects.first()
    return {'contactlink': contacts}