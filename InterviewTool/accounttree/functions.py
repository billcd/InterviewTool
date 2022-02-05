from django.template.defaultfilters import slugify
from django.db.models import Q
import string
import random
from .forms import AccountFormBasicOrg
from .models import Account
from .permissions import check_permission, PermissionType


def get_child_accounts(parent, get_siblings=False, active=True):
    if get_siblings:
        children = Q(parent=parent, active=active)
        siblings = Q(parent=parent.parent, active=active)
        return Account.objects.filter(children | siblings).order_by('name')

    else:
        return Account.objects.filter(parent=parent, active=active).order_by('name')


def get_account_by_slug(slug):
    return Account.objects.get(slug=slug)


def slug_unique(slug):
    if slug is None or slug == "":
        slug = random.choice(string.ascii_letters)
    slug = slug.replace(" ", "")
    slug = slugify(slug)

    if not Account.objects.filter(slug=slug).exists():
        return slug
    else:
        return slug_unique(slug + random.choice(string.ascii_letters))


"""
 Rewrite this garbage so it's testable and document it!
def get_client_breadcrumb(me, account):
    parents = []

    try:
        while account != me.parent:
            parents.append(account)
            account = account.parent
    except AttributeError as e:
        print(e.with_traceback() + " get_client_breadcrumb")
    try:
        parents.reverse()
    except IndexError:
        return None
    return parents
"""


def new_client_short(request, me, current_account=None):
    # method is too specific at this level, it assumes that persons must belong to an organization
    # this method needs to check that me has permissions to add accounts under the requested parent.

    if request.POST:
        account_form = AccountFormBasicOrg(data=request.POST)
        if account_form.is_valid():
            account = account_form.save(commit=False)
            account.slug = slugify(account.slug)
            account.owner = me.user
            account.active = True
            if check_permission(me, account, PermissionType.WRITE):
                account.save()
        else:
            return account_form

    if current_account and current_account.account_type == Account.ORGANIZATION_TYPE:
        account_type = Account.PERSON_TYPE
    else:
        account_type = Account.ORGANIZATION_TYPE

    return AccountFormBasicOrg(initial={'parent': me.parent, 'account_type': account_type, 'owner': me.user, 'active': True})
