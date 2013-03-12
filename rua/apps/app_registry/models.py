from __future__ import absolute_import

import logging
import imp
import sys

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.importlib import import_module

from project_setup.api import register_setup
from project_tools.api import register_tool
from navigation.api import register_top_menu

logger = logging.getLogger(__name__)


class App(object):
    @classmethod
    def register(cls, app_name):
        logger.debug('Trying to import: %s' % app_name)
        try:
            app_module = import_module(app_name)
        except ImportError:
            logger.debug('Unable to import app: %s' % app_name)
        else:
            logger.debug('Trying to import registry from: %s' % app_name)
            try:
                registration = import_module('%s.registry' % app_name)
            except ImportError:
                logger.debug('Unable to import registry for app: %s' % app_name)
            else:
                if not getattr(registration, 'disabled', False):
                    app = App()
                    app.name=app_name
                    # If there are not error go ahead with the stored app instance
                    app.label = getattr(registration, 'label', app_name)
                    app.description = getattr(registration, 'description', u'')
                          
                    for link in getattr(registration, 'setup_links', []):
                        logger.debug('setup link: %s' % link)
                        register_setup(link) 

                    for link in getattr(registration, 'tool_links', []):
                        logger.debug('tool link: %s' % link)
                        register_tool(link)
                        
                    for index, link in enumerate(getattr(registration, 'menu_links', [])):
                        logger.debug('menu_link: %s' % link)
                        register_top_menu(name='%s.%s' % (app_name, index), link=link)

    def __unicode__(self):
        return unicode(self.label)
