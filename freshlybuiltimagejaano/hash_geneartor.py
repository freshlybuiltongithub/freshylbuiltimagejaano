from hashlib import md5

model_checksum="models/model_r_.h5"
md5_hash=md5()
model_handler=open(model_checksum,"rb").read()
md5_hash.update(model_handler)
hash_code=md5_hash.hexdigest()
print(hash_code)