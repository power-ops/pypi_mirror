INSTALLED_APPS += [
    'admin_reorder',
]
ADMIN_REORDER = [
    {'app': 'auth', 'models': ('auth.User', 'auth.Group', 'authtoken.Token')},
    {'app': 'registry', 'models': (
        'registry.Package', 'registry.Path',
         )},
]
