from collective.grok import gs
from wccpilgrimageblog.policy import MessageFactory as _

@gs.importstep(
    name=u'wccpilgrimageblog.policy', 
    title=_('wccpilgrimageblog.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wccpilgrimageblog.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
