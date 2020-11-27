import urllib.parse
from google.cloud import firestore

db = firestore.Client()

def processEntry(request):
    if request.args and 'runID' in request.args and 'step' in request.args :
        runID = request.args.get('runID')
        step = request.args.get('step')
        value = None

        doc = db.collection(u'workflow_callbacks').document(runID+'_'+step)
        
        if 'value' in request.args:
            value_urlcoded = request.args.get('value')
            value = urllib.parse.unquote(value_urlcoded)
        
        doc.set({u'responded': True, u'value': value})
        
        return "OK", 200

    return "Missing runID or step query paramater", 400