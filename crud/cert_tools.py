import sys
import os
from pyOpenSSL import crypto




try:
  PFX_Passcode = os.environ['PFX_Passcode']
except KeyError:
  sys.exit('One or more required environment variables not set, required: PFX_Passcode')

with open('server.key', "r") as f:
  privkeydata = f.read()
with open('servr.pem', 'r') as f:
  certdata = f.read()
cert = crypto.load_certificate(crypto.FILETYPE_PEM, certdata)
privkey = crypto.load_privatekey(crypto.FILETYPE_PEM, privkeydata)
p12 = crypto.PKCS12()
p12.set_privatekey(privkey)
p12.set_certificate(cert)
p12data = p12.export(PFX_Passcode)
with open('server.pfx', 'wb') as pfxfile:
  pfxfile.write(p12data)
