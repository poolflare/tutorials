#!/usr/bin/env python

# Python code
import codecs

nonce1 = '0123'
nonce2 = '456789abcdef'
header_hex = '00000000000000004f7b074e53a70500b0992ffb0afbe928f6be055a262e36c85fa9a6bb7430661195fad6579a2bf651030002000000f9debd3ce3f6cae504e320000b1024511d17489e6c7638c89b096aea747d1de0060000009f12eda2e2a982bff541446e0f54846d0b23de59b6a7f133f71c007d8bca13b80800000092a2101fe3a7cbcf5d556608acaeda812c3a447d99ad1cc429917f8ed0694f04932ae464bbc1c0a3ed720934c502c88cc79af5ba100ff4d0e743000000000000b54307fd6d674efe27e75e077d96385b4bd4180ffdc89820c0df0c351852de5c07000000ff232862a00f21ee0900000000000000000000000000000000000000000000008ba60900000000000500000023884ae452a705000000000000000000'

# 456789abcdef0123 (big endian)
nonce_hex = nonce2 + nonce1
# decode and reverse
nonce = codecs.decode(nonce_hex, 'hex')[::-1]
print(codecs.encode(nonce, 'hex'))

header = codecs.decode(header_hex, 'hex')
pow_header = header[0:278] + nonce

# 286
print(len(pow_header))
print(codecs.encode(pow_header, 'hex'))
# blake2s it and reverse
# pow_hash = blake2s(pow_header)[::-1]
