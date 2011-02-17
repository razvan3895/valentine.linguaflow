from Products.Five import BrowserView
from zope.component import getUtility
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFPlone.utils import getToolByName
import logging
logger = logging.getLogger('Plone')

class ReminderMail(BrowserView):
    """
    View to update all feeds
    """
    
    def send(self):
        """
        Send reminder mail
        """
        portal = getUtility(IPloneSiteRoot)
        ct = getToolByName(portal, 'portal_catalog')
        wf = getToolByName(portal, 'portal_workflow')
        doActionFor = wf.doActionFor
        invalidTranslations = [b.getObject() for b in ct(Language='all', lingua_state='invalid')]
        print 'len:', len(invalidTranslations)
        for translation in invalidTranslations:
            doActionFor(translation, 'notify_editors')
        logger.info('valentine.linguaflow: Notified editors about %d invalidated translations', len(invalidTranslations))
