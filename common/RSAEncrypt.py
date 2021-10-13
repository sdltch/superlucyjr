# /usr/bin/python
# encoding: utf-8
import datetime
import random

import rsa
from Crypto import Random
from Crypto.PublicKey import RSA
import base64
from Crypto.Cipher import PKCS1_v1_5


class RSAEncrypt():

    def _gen_modulus_exponent(self, s) ->int:
        # p.debug("Now base64 decode pub key,return modulus and exponent")
        # 对字符串解码, 解码成功返回 模数和指数
        b_str = base64.b64decode(s)
        if len(b_str) < 162:
            return False
        hex_str = b_str.hex()
        # 找到模数和指数的开头结束位置
        m_start = 29 * 2
        e_start = 159 * 2
        m_len = 128 * 2
        e_len = 3 * 2
        self._modulus = int(hex_str[m_start:m_start + m_len], 16)
        self._exponent = int(hex_str[e_start:e_start + e_len], 16)


    def _gen_rsa_pubkey(self):
        # 将pub key string 转换为 pub rsa key
        # p.debug("Now turn key string to rsa key")
        try:
            rsa_pubkey = rsa.PublicKey(self._modulus, self._exponent)
            # 赋值到_pub_rsa_key
            self._pub_rsa_key = rsa_pubkey.save_pkcs1()
            # p.debug("self._pub_rsa_key：{}".format(self._pub_rsa_key))
        except Exception as e:
            # p.error(e)
            # p.error("Invalid public_key")
            raise e

    # 随机生成密钥对
    def genKeyPair(self):
        # 伪随机数生成器
        random_generator = Random.new().read
        # rsa算法生成实例
        rsa = RSA.generate(1024, random_generator)
        # 私钥的生成
        private_pem = rsa.exportKey()
        with open("private.pem", "wb") as f:
            f.write(private_pem)
        # 公钥的生成
        public_pem = rsa.publickey().exportKey()
        with open("public.pem", "wb") as f:
            f.write(public_pem)


    # 加密
    def encrypt(self, message, publickey):
        # 加密
        crypto = rsa.encrypt(message.encode(), publickey)
        print(crypto)
        b64str = base64.b64encode(crypto).decode('utf-8')
        print("字符串【{}】加密后【{}】".format(message,b64str))
        print(b64str)
        # 公钥加密
        # cipher = Cipher_pkcs1_v1_5.new(publickey)  # 创建用于执行pkcs1_v1_5加密或解密的密码
        # sss = cipher.encrypt(message.encode('utf-8'))
        # cipher_text = base64.b64encode(sss)
        # print(cipher_text.decode('utf-8'))


    # 解密
    def decrypt(self, str, privateKey):
        # 密文
        msg = 'bAlnUNEJeDLnWikQs1ejwqPTo4qZ7RWxgFwoO4Bfg3C7EY+1HN5UvJYJ2h6047K6vNjG+TiIxc0udTR7a12MivSA+DwoGjwFIb25u3zc+M8KTCaCT5GdSumDOto2tsKYaVDKCPZpdwYdzYwlVijr6cPcchQTlD1yfKk2khhNchU='
        # base64解码
        msg = base64.b64decode(msg)
        # 获取私钥
        privatekey = open('private.pem').read()
        rsakey = RSA.importKey(privatekey)
        # 进行解密
        cipher = PKCS1_v1_5.new(rsakey)
        text = cipher.decrypt(msg, 'DecryptError')
        # 解密出来的是字节码格式，decodee转换为字符串
        print(text.decode())
        return text.decode()

    def strkey(self,s):
        # 对字符串解码
        b_str = base64.b64decode(s.encode("utf-8"))

        if len(b_str) < 162:
            return False

        hex_str = ''
        # 按位转换成16进制
        hex_str = b_str.hex()
        # for x in b_str:
        #     h = hex(ord(x))[2:]
        #     h = h.rjust(2, '0')
        #     hex_str += h

        # 找到模数和指数的开头结束位置
        m_start = 29 * 2
        e_start = 159 * 2
        m_len = 128 * 2
        e_len = 3 * 2

        modulus = hex_str[m_start:m_start + m_len]
        exponent = hex_str[e_start:e_start + e_len]
        return modulus, exponent

    # 对String的公钥转成成key
    def mykey(self, publicKey):

        key = ss.strkey(publicKey)
        print(key)
        modulus = int(key[0], 16)
        exponent = int(key[1], 16)
        rsa_pubkey = rsa.PublicKey(modulus, exponent)
        return rsa_pubkey

if __name__ == '__main__':
    ss = RSAEncrypt()
    # # ss.genKeyPair()
    # str = "123456"
    # publicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCVNH7WzQiB3fzfOvBYpiDMdfkm7SK/eSH9xgfDzmSYeHhAcZBjqYynZNK2mAl+g/0sKnA7tuIMzqR/S+ctaIGKtQ3oC7s6ECYxhZ7jbR7FHHQu8EY/lou1FNnlVp7HhuDVf4asaCHOSF8MALCEBhqQI8uYU4nDXu5TLMUJ3XB1KwIDAQAB"
    # mypublicKey = ss.mykey(publicKey)
    # ss.encrypt(str,mypublicKey)
    sss = 'random.randint(0,9)'
    aas = random.randint(0,9)
    # now_time = datetime.datetime.now()
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 判断成功
    ss= random.__call__
    if (hasattr(random, '__call__')):
        print("sss")
    print(now_time)
    print("sss："+sss)
    print(aas)
    dd=eval(sss)
    dddd = str(dd)
    print(dddd)
