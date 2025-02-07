import firebase_admin
from firebase_admin import credentials

# Configuração do Firebase (com as quebras de linha escapadas)
firebase_config_json = {
    "type": "service_account",
    "project_id": "bottelegram-6937f",
    "private_key_id": "ee7f95164c6075803eb5ce61ba43b964cfc57e4e",
    "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC7X83GQR1OChBv\\nXV/EZeUmZaFvOESVFel23q++J9hiQ/9N1OXhRz6yfOzcYk6hiiZ9B09LEgdckvVq\\n0p+ouQjm/1j/XrBfR3dS9/XexLaOYBR7gTAXSsdUxiOkXcMzHUFkmZD+xYj7Aw7/\\nxAHLgWvrt5yJRsXr6g8Jx6UX8IOP+Av0phdGOo20iLZQDEWGll6bDoVD9VH/yctu\\nT/rQtvujatRc7wWLFfQImIDytZywUCXXes3Beq+fn9FNZD0rWA9wimNadIorTd8O\\nJP7x2KbQHTVdDOE0eHeIxhd+efS2EUA4ntoyZNV2LzXXUb0gnWULoLBMQG1E7ebq\\nT+CAkck1AgMBAAECggEABg1Z+Kw0FZ1hRYTsacwUGDw9Is9cS70kSC4jhWQFFbt2\\nMh3iekx8+8fpi1QeOmfbcWYR4MNe0ICArn10zGmESO3OLUVyM0mm0tu71IEMbScw\\n/NeXOuaz7zWNLiscec4D8DYTnF8QsHGQrks29vX3C0CS16OdE08r7YLGKYf1FT/S\\nue9vDVM/f/Aegy5ZFQE8E/g5mfU3TlQc/DJ+CyqI4Wp+x1NSFltYMr0Cb9+ZwZy8\\nx8aozZWU2zxy16B4IkAuDjza35j6eJ/n37+JeBaQriif2dsDKQx2Ffy5n6gY70dp\\n9t8kwmDiqkEKY7zN0C7X6OphLr5+OuSZk2aBC7phsQKBgQD4N8E28Qe4ItAUdO0g\\ns7wmyJN5uY+3AwjgdbdRPNS09Tv1RBvZEu7EnHcPjt9xHb2duDOxFGM277f3PsUy\\nVG2jqPwSK8qjTtWPGge1JdZW1SIrIep3CklaSVBvVrjMg9fe4QW8x7Ejgptu6+Ua\\nUogSJqAx/VO/C7Yce/QRpAcDPQKBgQDBP7Ti+3LKOBf+63HU8Ygc8ygyHfXJ9x6l\\nJ2GBxVEbkqpIWkJS58O1kesANWm8aD7q/Da8YdLJjfJIdkP3dpfTT2W1r2/8UJUy\\nJQDScFDT1VU3XMqIeMwnFxcNRYSoe7XvNIOIQrH02ifs9eHLyJT64fvdpp8qA76o\\nWPGDKw7dWQKBgQCbwjjvph6G8OmL/LeUjtThrXnFp6jEWhYm7BeF1dtQVpcyWHP1\\nKslD/T9FNw2FqPkE0MM3Oqjrn0/cybnq1EocqfzL1kkJY33ll5sAlGbFBGe1k0nT\\nO1Q+YMUlqNC8HXvH84KrLNA+jUXGPCb+9o1GfpCF7gawWsQDadEFhN2VrQKBgDyO\\nsyeB9lnKNDLNIzHAso+n3wu9eb1ddDv62EJrS9xhHH1p02jZeenXHRZGpqjE3hqT\\nCLAF06EXmzn73ZaZkkBEnDHQFT6zHd3F3LkVOy72piqgKFOVzxvcz3t4Mnb9tWiN\\nQz6a79sz1dkawDQ02gK4eE3gHfZzj/Z/UMdy4ciZAoGBANUbRcANBeQuIbsAfTSm\\nZSCgSLDFVQ5x61KysUo3SzOv2lOqs7sXaVFup1UKCYuJRVvyB/9Q5cO5hk0CfRxZ\\noRnqwcdEFjw3JtC/lu1OJmKF4JgyTR286ijTUOtQw4oeuH2+jbySk3FFraCJ/xpG\\nIo4ZNO5U1BVQo0BuOIwEfzLu\\n-----END PRIVATE KEY-----\\n",
    "client_email": "firebase-adminsdk-fbsvc@bottelegram-6937f.iam.gserviceaccount.com",
    "client_id": "108397135342027414658",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40bottelegram-6937f.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# Inicializando o Firebase com as credenciais
cred = credentials.Certificate(firebase_config_json)
firebase_admin.initialize_app(cred)
