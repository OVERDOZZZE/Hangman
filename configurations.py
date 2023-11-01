import firebase_admin
from firebase_admin import credentials, db
cred = credentials.Certificate('firebase.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hangman-6c7f4-default-rtdb.firebaseio.com'
})

ref = db.reference('database')
WORDS = ref.child('WORDS').get()
ATTEMPTS = ref.child('ATTEMPTS').get()
HANGMAN = ref.child('HANGMAN').get()
VICTORY = ref.child('VICTORY').get()
CONGRATS = ref.child('Congratulations').get()
