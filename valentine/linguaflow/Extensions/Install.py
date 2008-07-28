import transaction
from Products.CMFCore.utils import getToolByName
PRODUCT_DEPENDENCIES = ('PloneLanguageTool','LinguaPlone', )
EXTENSION_PROFILES = ('valentine.linguaflow:default', )

def install(self, reinstall=False):

    qi = getToolByName(self, 'portal_quickinstaller')
    portal_setup = getToolByName(self, 'portal_setup')
    for product in PRODUCT_DEPENDENCIES:
        if reinstall and qi.isProductInstalled(product):
            qi.reinstallProducts( [product])
            transaction.savepoint()
        elif not qi.isProductInstalled(product):
            qi.installProduct(product)
            transaction.savepoint()

    for extension_id in EXTENSION_PROFILES:
        portal_setup.setImportContext('profile-%s' % extension_id)
        portal_setup.runAllImportSteps()
        product_name = extension_id.split(':')[0]
        qi.notifyInstalled(product_name)
        transaction.savepoint()