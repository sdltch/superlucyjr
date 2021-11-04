# /usr/bin/python
# encoding: utf-8
import datetime
import random

import rsa
from Crypto import Random
from Crypto.PublicKey import RSA
import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from rsa import encrypt


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
    def myencrypt(self, message, publickey):
        # 加密1
        # crypto = rsa.encrypt(message.encode(), publickey)
        # print(crypto)
        # b64str = base64.b64encode(crypto).decode('utf-8')
        # print("字符串【{}】加密后【{}】".format(message,b64str))
        print("字符串【{}】".format(publickey))
        # 公钥加密2
        key = '-----BEGIN PUBLIC KEY-----\n' + publickey + '\n-----END PUBLIC KEY-----'
        print("字符串【{}】".format(key))
        # 导入公钥
        public_key = RSA.importKey(key)
        # public_pem = key.exportKey()  # 将公钥输出成pem格式
        cipher = Cipher_pkcs1_v1_5.new(public_key)
        cipher_text = base64.b64encode(cipher.encrypt(message.encode()))
        cipher_str = cipher_text.decode()
        print("加密：{};类型{}".format(cipher_str,type(cipher_str)))
        return cipher_text


    # 解密
    def mydecrypt(self, strone, privatekeyone):
        print("解密【{}】;类型{}".format(strone, type(strone)))
        print("私钥1【{}】;类型{}".format(privatekeyone,type(privatekeyone)))
        keyone = '-----BEGIN RSA PRIVATE KEY-----\n' + privatekeyone + '\n-----END RSA PRIVATE KEY-----'
        # 导入私钥
        print('私钥2:{}'.format(keyone))
        private_key = RSA.importKey(keyone)
        cipher = Cipher_pkcs1_v1_5.new(private_key)
        # rsatext = cipher.decrypt(base64.b64decode(strone.decode()), '')
        rsatext = cipher.decrypt(base64.b64decode(strone), '')
        print("解密类型：{}".format(type(rsatext)))
        print(rsatext)
        # 解密出来的是字节码格式，decodee转换为字符串
        print("解密：{}".format(rsatext))
        return rsatext

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
    strone = "123456"
    # 私钥
    privateKey = 'MIICXAIBAAKBgQCkNNm6P72DN30Gy9ChfSAeI3CTRUb3V/S7pttl4d3Boi2yLDOnbpnlMgPpWa+h82nXErq6D66hq3DudmMA3QYaGkKsdVzAnQ++KxJEHea4hIKN0S9OF1PYC8cpiEFY8B2TdBdh8KZUP7Fx/BiShOs3IXCWvHYSSR/QEw7pknM9AwIDAQABAoGASuUOH5x98DDpViW1CUr8ULLCYHF7HkqgRcyjihMcZXp2lCsD/kx8ZeTLku3EpT3UGvQgdce8U2HSNvmJS3YEFzy82ogwNfRtiOEvYpobpMnJk1EkPEz+9wpvciFGXlQFM6jYm/RHG3BE1dn7mUl8pDQ3VuG+NytXctq8zVWrEtkCQQC5JVnZIL1dUv2Wbng3+h6dLpTy4Sll8eI6XLMb0f9AOexXnXcp2jhKY6stA6YTdrZFzLI/vEx0Fk7/RusFrDxrAkEA4wwSZicsrGAqSbm+jPxu5gcEQ/9UrlcNot+NoYZuJe00aLe6N8gKEGy0n8koOtmEiZ18T22fve8Tzb2w2+qnyQJALYo6Z2XeLi5TocTaXSpwjUj/6h3oCONOOfzDMXydxDZ7I7HftbOvVNzfJdtX5kG048ZNsc+nHoa+N5xCAssysQJBAI7OeAAiobmmHtMSbmT1Hbe3MBqozZV+kcgg/k9bY4qdYPqAnTMasiHUjeN2vcQOLov0L00yMWhgqL8ekdAxDukCQAjdkQAFSPXwBI3Tm/OLIOII7MQ/38m//OwkJpeXht4NMQIENkUtnLkF1nXqZ02eRaP7hRUIlNR7GsPISeTNTVQ='
    # 公钥
    publicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCVNH7WzQiB3fzfOvBYpiDMdfkm7SK/eSH9xgfDzmSYeHhAcZBjqYynZNK2mAl+g/0sKnA7tuIMzqR/S+ctaIGKtQ3oC7s6ECYxhZ7jbR7FHHQu8EY/lou1FNnlVp7HhuDVf4asaCHOSF8MALCEBhqQI8uYU4nDXu5TLMUJ3XB1KwIDAQAB"
    rsaencrypt = ss.myencrypt(strone, publicKey)
    rsanew = rsaencrypt.decode()
    print("加密后数据:【{}】；类型：【{}】".format(rsanew,type(rsanew)))

    # sss = 'random.randint(0,9)'
    # aas = random.randint(0,9)
    # # now_time = datetime.datetime.now()
    # now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # # 判断成功
    # ss= random.__call__
    # if (hasattr(random, '__call__')):
    #     print("sss")
    # print(now_time)
    # print("sss："+sss)
    # print(aas)
    # dd=eval(sss)
    # dddd = str(dd)
    # print(dddd)
