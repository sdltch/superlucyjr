# """
# ------------------------------------
# @Time : 2021/10/27 13:21
# @Auth : DALONG
# @File : pytest.PY
# @IDE  : PyCharm
# @Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
# @QQ   : 5962@qq.com
# @GROUP: 5962
# ------------------------------------
# """
# import paddlehub as hub
# import cv2
#
# # 待转换图片的绝对地址
# picture = 'D:\\testdata\\gitami\\pythonami\\superlucyjr\\test\\code.png'  # 注意代码中此处为双反斜杠
#
# # 风格图片的绝对地址
# style_image = 'D:\\testdata\\gitami\\pythonami\\superlucyjr\\test\\fangao.png'
#
# # 创建风格转移网络并加载参数
# stylepro_artistic = hub.Module(name="stylepro_artistic")
#
# # 读入图片并开始风格转换
# result = stylepro_artistic.style_transfer(
#                     images=[{'content': cv2.imread(picture),
#                              'styles': [cv2.imread(style_image)]}],
#                     visualization=True
# )