from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 10.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'taskdiscretion_nl',
        'display_name': "Task Discretion Experiment - Dutch version (Administered)",
        'num_demo_participants': 4,
        'app_sequence': ['taskdiscretion_nl'],
    },
    {
        'name': 'taskdiscretion_eng',
        'display_name': "Task Discretion Experiment - English version (Translated)",
        'num_demo_participants': 4,
        'app_sequence': ['taskdiscretion_eng'],
    },
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'z6z-m0e2&@k-trf13hg^j#0&1$r3_bs*lf+u!1g0v(gw1uf*re'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
