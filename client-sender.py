import time
import secp256k1
import json
import asyncio
import websockets
from hashlib import sha256
from nostr.key import PrivateKey
import argparse

async def send_message(host,messages):
  uri = "wss://{}".format(host) #wss for https
  pk = PrivateKey()
  pub_key = pk.public_key
  event = {
      'id': None,
      'sig': None,
      'content':messages,
      'created_at':int(time.time()),
      'kind':1, #fixed for 1 in this proj
      'pubkey':pub_key.hex(),
      'tag':[]
  }
  data = [0,pub_key.hex(),event['created_at'],event['kind'],event['tag'],event['content']]
  serialzed = json.dumps(data,separators=(',',':'),ensure_ascii=False).encode()
  event['id'] = sha256(serialzed).hexdigest()
  sk = secp256k1.PrivateKey(pk.raw_secret)
  event['sig'] = sk.schnorr_sign(bytes.fromhex(event['id']),None,raw=True).hex()

  async with websockets.connect(uri) as websocket:
    payload = [
        'EVENT',
        event
    ]
    await websocket.send(json.dumps(payload))


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--host',default='localhost:8080')
  parser.add_argument('--message',default="Hello World")
  args = parser.parse_args()
  asyncio.run(send_message(args.host,args.message))