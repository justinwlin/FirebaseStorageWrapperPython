# Summary

This project is using:
https://github.com/AsifArmanRahman/firebase-rest-api

Firebase-rest-api to manage file uploading / downloading from FileStorage.

# Setup

Firebase Project > Users and Permissions

## Under General

1) Add a new app for Web

You'll get an object like this:
```python
 firebaseConfig = {
  apiKey: "x",
  authDomain: "x.firebaseapp.com",
  projectId: "x",
  storageBucket: "x.appspot.com",
  messagingSenderId: "x",
  appId: "1:x:web:x",
  measurementId: "G-x"
};
```

## Under Service Accounts
2) Generate a new private key

You will get a JSON file to download and put to your project.

```python

dir_path = os.path.dirname(os.path.realpath(__file__))
credentials_path = os.path.join(dir_path, "firebase_credentials.json")

if not os.path.exists(credentials_path):
    raise FileNotFoundError(
        f"Firebase credentials file not found at {credentials_path}"
    )

config={
        # initialized this through creating a "web app"
        apiKey: "x",
        authDomain: "x.firebaseapp.com",
        projectId: "x",
        storageBucket: "x.appspot.com",
        messagingSenderId: "x",
        appId: "1:x:web:x",
        measurementId: "G-x"
        # This is for real time database url so can leave empty.
        "databaseURL": "",
        # This is specifically the admin level
        "serviceAccount": credentials_path,  # Initialized this through: https://firebase.google.com/docs/admin/setup#initialize-sdk
    }

firebaseSimpleManager = SimpleFirebaseManager(config)
firebaseSimpleManager.upload_file("mock.mp3", "media/output.mp3")
firebaseSimpleManager.download_file("media/output.mp3", "test_download.mp3")
```