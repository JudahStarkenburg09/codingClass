import pygsheets
import json

# add credentials to the account
creds = json.dumps({
    "type": "service_account",
    "project_id": "linus-co",
    "private_key_id": "5f8ac6ad7e2535d14626e3eeeca3aec93ce19614",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCvBNFv/7FitDdt\nbTpLaDjmuDTQSOHqjwAk98zQCktx3CXh+n0DXXtYMN1+PdsvkwiCPdhtcwaguStV\naQucji5L0C9stgpKPSUcuEJAdwEgHj9mbbb1NgM4s+meKFJFOG69F17LOE3scRiA\nqif79pR4Omtx6gmLai/1Z3hhAD6k9YKmicBY2h/Dl7sk12LHHSifLEHaWmCLxdkl\n9p3KNUjvY8+0BYd7SxTe6bk7Lf8vbCTDBg3jn5/hRgTbmF7coSk9fX5KLE6klFDJ\n3FmHSV5BnNn0Czffr71X5miYeSI2EHStp23azNLKU6JYMnQWwwyaRkR9q5N026ic\nNH1xlsPvAgMBAAECggEADP6slkZD43JCE0vi4ipw3yCaO0TOEV5gwl3rxR6ej2ur\nHGY+1fsg52FpcLAjEBs4rILvCOFbgp99CjBsfklIQrTIcKfrh6uWj9VWhfbQDJRy\nXKaUyQwjnRgupmGUCjOwdTXBAhHCJ2YWTadUpK6gQ3UC+UhJQSK3QN9X3svn2tOI\nWaTLdwR0zQYkwO5UaKm/kx5gYh8/uSI+l100fSC3osX5vFfB16LzGwX9LGVd15Bi\nnqmptj5/OHaSCDkU6mZfHNHyZtpNeA0QIK1CDxIw99r3/+7HPk7mCAUM3kriCbsx\n4NAo0dOhpgL8pUTFeX3APJ/2uvVvdySVOEKhpTH40QKBgQDXoRTuPC21HT298d1K\n+Iw7TR1u1a8+iYNM4ud/2t2bal/bDb4en5a8wHXZut7BGohgVq3VF+zs1d9Y1C4X\nK+bbmRe8FOb9rwbGeGyysJtdXQsuRmWVOzomfV5PPMJXJg9RosbuIVukEgdoFmT8\nh9bIHfYBDTGYWUykD1wrqx6WVQKBgQDPyVDG9/S2VIvFD3X4tv0UoI30xIDyo8Yx\nRHAIPfvH2fLHLYNgDTir+wqJnxxNtd075dvVDVgiGzHuRpf9pI9LQ7/5Fz78cvJv\n0P62SeHf9OGlNmRWTQOeRqQKc5yuaQ+Skz1tarbCrYgrF4juBabWMgSJ/k3fFrdM\nRApouOqNMwKBgGzgLdRY2G9hs2IsNKN9OjlbJ6hmBtVZ081HqMJa/ZhSrtHJb5zA\n0fi+aQMmIwF35zJVsfIt4Xh4SQzuHdOfXDK3a0+RckzXSmF+Psw+9kO/Dj0wWGxw\nel0i4jK6KBqe4g9DVJS6jS4b2FeLLzR/Vki3MBa51bfqJxOTmeOGxKv9AoGAZ1y0\nsxV7hQvPr4p+W+fjQ1SO6TirEIiJuc5akK8MxaDUlWI9nRVWoK6z0jv1H28di4NP\ndM87jVPL5cT2LLWkloMwRx/aNEiV8yua2WEtXHP7n2zMQuXyq9RmG9DhGx2mInre\nLsTL/1HFj/IYKpdjI+Ajw+VeJWCuc+DQ8MEz5GMCgYBDMluUqOcRxpHMnXK4g2Ln\nmuyfeih/KhOBQxRWWNvsF7JQ2g+cY+g6yAYt9cRVFXItfkVONSJn58JfBozimEmI\nYffEPg+BVccOS4bf5TqD+bBcAX5GXpq5avat9CZqNbgOKtj2QmlNb7/dGXBZEo2v\noV5xDw7qLdmxY/K+A9mZCg==\n-----END PRIVATE KEY-----\n",
    "client_email": "linus-co-op@linus-co.iam.gserviceaccount.com",
    "client_id": "110264289236205928194",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/linus-co-op%40linus-co.iam.gserviceaccount.com"
    })

# set up credentials
gc = pygsheets.authorize(service_account_json=creds)

# open the Google Sheets document by its URL
sheet_url = 'https://docs.google.com/spreadsheets/d/1nWb4ZTeLfldXi_7kQ--qB65GLoX7JB_k5YzAIKiPocA/edit#gid=0'
sh = gc.open_by_url(sheet_url)

# select a worksheet by its index (starting from 0)
worksheet = sh[0]

#--------------------------------------------------------------------
#TODO #TODO #TODO #TODO #TODO #TODO #TODO #TODO #TODO #TODO
Score = 103 #ERASE THIS LINE
user = 'Judah' #ERASE THIS LINE


# update the high score if necessary
newHighScore = None

if int(worksheet.cell('H3').value) < Score:
    newHighScore = Score

if newHighScore:
    ScoreCell = worksheet.cell('H3')
    ScoreCell.value = str(newHighScore)
    ScoreCell.color = (0.929, 0.490, 0.490) # Red color
    ScoreCell.update()
    
    UserCell = worksheet.cell('J3')
    UserCell.value = str(user)
    UserCell.color = (0.929, 0.694, 0.490) # Orange color
    UserCell.update()