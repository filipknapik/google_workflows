from google.cloud import firestore
from datetime import datetime, timedelta
from flask import jsonify

collection = u'cache'

def deleteOldCache(request):
    rowsDeleted = 0
    db = firestore.Client()
    dateThreshold = datetime.today() - timedelta(days=30)
    docs = db.collection(collection).where(u'updated', u'<=', dateThreshold).stream()
    for doc in docs:
        rowsDeleted += 1
        print(doc.id)
        db.collection(collection).document(doc.id).delete()
    return jsonify({"rowsDeleted": rowsDeleted})
