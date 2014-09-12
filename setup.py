try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

INSTALL_REQUIRES = [
    'Yapsy', 'Image', 'pylint', 'thrift', 'gitpython', 'fusepy',
     'ffvideo', 'filemagic'
]

config = {
    'description': 'Digital Assets Managed Neatly: Analyzers and Transcoders',
    'author': 'sueastside',
    'url': 'https://github.com/sueastside/damn-at',
    'download_url': 'https://github.com/sueastside/damn-at',
    'author_email': 'No, thanks',
    'version': '0.1',
    'test_suite': 'tests.suite',
    'install_requires': INSTALL_REQUIRES,
    'packages': ['damn_at'],
    'scripts': [],
    'name': 'damn_at',
    'entry_points': {
        'console_scripts': [
            'damn = damn_at.run_damn:main',
            'damn_at-server = damn_at.thrift.server:main',
            'damn_at-analyze = damn_at.analyzer:main',
            'damn_at-transcode = damn_at.transcoder:main',
            'damn_fs = damn_at.damnfs.damnfs:main'
        ]
    }
}

setup(**config)
