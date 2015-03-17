from collective.grok import gs
from wcc.pilgrimagepolicy import MessageFactory as _

@gs.importstep(
    name=u'wcc.pilgrimagepolicy', 
    title=_('wcc.pilgrimagepolicy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.pilgrimagepolicy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
