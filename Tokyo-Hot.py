#coding=utf-8
#T0kyo_1s_6ot_o_0.py
#Author:SuzukaGozen 2024.5.2 Version:1.0  

import sys
import random
import time
import webbrowser  
import argparse  
from colorama import init, Fore, Back, Style 

init(autoreset=True)  # 初始化colorama，设置autoreset为True可以在每次打印后自动重置颜色  #eg. print(Fore.GREEN + "这是一段绿色的文本")
colors = [Fore.LIGHTRED_EX,Fore.LIGHTGREEN_EX,Fore.LIGHTYELLOW_EX,Fore.LIGHTBLUE_EX,Fore.LIGHTMAGENTA_EX,Fore.LIGHTCYAN_EX,Fore.LIGHTWHITE_EX]
color = random.choice(colors)
#映射表
map = {  
    'NaYo?': '0',  # 'NaYo?' 映射到 '0'  
    'Ayo!': '1', 
    'NaYo.':'hello',
    'Ayo,':'world',  
} 
#反向映射
re_map = {v: k for k, v in map.items()}  

#加密
def Tokyo_encode(text):
    #字符转二进制（拓展了包括中文字符）
    def string_to_binary(text):  
        bytes_data = text.encode('utf-8')  
        binary_string = ''.join(format(byte, '08b') for byte in bytes_data)  
        return binary_string
    #映射表替换值，其实是反向映射
    def encrypt(encrypted_text):
        for value, key in re_map.items():  
            encrypted_text = encrypted_text.replace(value, key)  
        return encrypted_text
    #添加噪声
    def noisy(str,noise=["Ayo,","NaYo."] ):
        new_str= ""
        for char in str:
            new_str += char
            if char == "?" or char == "!":
                if random.random()>0.85:
                    new_str += random.choice(noise)  # 在问号或感叹号后加噪  
        return new_str
    return noisy(encrypt(string_to_binary(text)))
    # return encrypt(string_to_binary(text))

#解密
class DecryptionError(Exception):  
    pass  
def Tokyo_decode(text):
    #正向映射
    def decrypt(text):  
        for key in map:  
            text = text.replace(key, map[key])  
        text = ''.join(c for c in text if c in '01')    #xixi(●'◡'●)
        #为空提示解密失败
        if text=='':
            print(color+"\n"+"【Nothing!】Check your input carefully")
        return text
    #二进制转字符
    def binary_to_string(binary_text):    
        bytes_data = bytearray()  
        for i in range(0, len(binary_text), 8):  
            byte_value = int(binary_text[i:i+8], 2)  # 截取8位 
            bytes_data.append(byte_value)  
        return bytes_data.decode('utf-8',errors='ignore')   #忽略解析异常报错
    # try:
    #     Tokyo_decode(text)
    # except Exception as e:
    #     print(e)
    return binary_to_string(decrypt(text))

# str = 'Wow,你发现了Nian留下的彩蛋:...'
strs = 'NaYo?Ayo!NaYo?Ayo!Ayo,NaYo?Ayo!Ayo!Ayo,Ayo!NaYo?Ayo!Ayo!NaYo?Ayo!Ayo!Ayo!Ayo!NaYo?NaYo.Ayo!Ayo!Ayo!NaYo?Ayo,Ayo!NaYo.Ayo!Ayo!Ayo,NaYo?NaYo?Ayo!Ayo,NaYo?Ayo!Ayo!Ayo,NaYo?NaYo?Ayo!Ayo,Ayo!Ayo!NaYo?NaYo?Ayo!Ayo,NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!Ayo!Ayo!NaYo?Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?NaYo?NaYo?NaYo?Ayo!Ayo!Ayo!Ayo,NaYo?NaYo?NaYo.Ayo!NaYo?Ayo!Ayo,Ayo!NaYo?NaYo.NaYo?NaYo?Ayo!Ayo!Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!NaYo?NaYo?NaYo?Ayo!Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!Ayo!Ayo!NaYo?NaYo?Ayo,NaYo?Ayo!Ayo!Ayo,Ayo!NaYo?Ayo!NaYo?Ayo,Ayo!Ayo!NaYo?NaYo?NaYo.NaYo?NaYo?Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!Ayo!NaYo?Ayo!NaYo?Ayo!NaYo?NaYo.NaYo?NaYo?NaYo?Ayo!Ayo!NaYo?NaYo?Ayo!NaYo?NaYo?Ayo!Ayo!NaYo.Ayo!NaYo.NaYo?NaYo?Ayo!Ayo!Ayo,NaYo?Ayo!NaYo?Ayo,NaYo?Ayo!NaYo?Ayo!Ayo!Ayo,NaYo?NaYo?NaYo?NaYo?Ayo!NaYo.NaYo?Ayo!Ayo!NaYo?Ayo!Ayo!NaYo.Ayo!Ayo,NaYo?Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!NaYo.NaYo?Ayo!NaYo.Ayo!NaYo?NaYo?Ayo!Ayo!NaYo?NaYo?Ayo!NaYo.Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!NaYo?NaYo.NaYo?Ayo!NaYo?Ayo!Ayo!Ayo!NaYo?NaYo?NaYo?Ayo!NaYo?NaYo?NaYo?Ayo!NaYo?NaYo.Ayo!Ayo!Ayo!Ayo!Ayo,Ayo!NaYo?Ayo,NaYo?Ayo!Ayo!Ayo!Ayo!NaYo?NaYo?Ayo,Ayo!Ayo!NaYo?Ayo!NaYo?Ayo!NaYo?NaYo?NaYo?NaYo.NaYo?Ayo!NaYo?NaYo?Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!Ayo,NaYo?Ayo!Ayo!Ayo!Ayo!NaYo?Ayo!NaYo.Ayo!NaYo?Ayo!NaYo?NaYo.Ayo!NaYo?NaYo?Ayo,Ayo!Ayo!Ayo!Ayo!Ayo,NaYo?Ayo!NaYo?NaYo?NaYo?Ayo!Ayo,NaYo?Ayo,NaYo?Ayo!Ayo!NaYo?Ayo!Ayo!Ayo!NaYo?Ayo,NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!NaYo.Ayo!NaYo?Ayo!Ayo,NaYo?NaYo.NaYo?Ayo!NaYo?NaYo?Ayo,Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!NaYo.Ayo!Ayo,NaYo?NaYo?NaYo?NaYo?Ayo,Ayo!NaYo?Ayo!Ayo!Ayo,NaYo?Ayo!Ayo!Ayo,Ayo!NaYo.NaYo?NaYo?Ayo!Ayo!Ayo!Ayo!NaYo?Ayo!Ayo!NaYo?Ayo!NaYo?Ayo!NaYo?Ayo!Ayo,NaYo?NaYo?NaYo?NaYo?Ayo!Ayo!NaYo?NaYo?NaYo?NaYo?NaYo?Ayo,Ayo!Ayo!NaYo?Ayo!NaYo?Ayo!Ayo!NaYo?Ayo!Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!NaYo.NaYo?Ayo!Ayo!NaYo?Ayo!Ayo!Ayo!Ayo!NaYo?Ayo!NaYo?Ayo!Ayo!Ayo,Ayo!Ayo!Ayo!NaYo.NaYo?Ayo,NaYo?Ayo!Ayo!NaYo?NaYo?NaYo?NaYo.Ayo!NaYo?Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!NaYo?Ayo!NaYo?Ayo!Ayo!Ayo,Ayo!Ayo!Ayo!NaYo.NaYo?Ayo!Ayo!NaYo?NaYo.Ayo!Ayo!Ayo!NaYo.NaYo?NaYo?NaYo?Ayo!Ayo!NaYo?NaYo?Ayo,NaYo?NaYo?NaYo?Ayo!Ayo!Ayo!NaYo?Ayo!Ayo,NaYo?NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!Ayo!Ayo!Ayo!NaYo?Ayo!Ayo!Ayo!NaYo.NaYo?Ayo,Ayo!NaYo?Ayo,NaYo?NaYo?Ayo!Ayo!NaYo?Ayo!Ayo!Ayo,Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!Ayo,NaYo?NaYo?NaYo?Ayo,NaYo?NaYo?Ayo,Ayo!NaYo?Ayo,Ayo!Ayo!Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!NaYo?Ayo!Ayo!NaYo?NaYo.NaYo?Ayo!Ayo!NaYo?Ayo!NaYo.Ayo!Ayo!Ayo!NaYo?Ayo!Ayo!Ayo!NaYo?Ayo,Ayo!NaYo?NaYo?NaYo?NaYo?Ayo!NaYo?NaYo.NaYo?NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!NaYo.Ayo!Ayo!Ayo!NaYo?Ayo!Ayo,' 
# str1 = '嘻，你知道Nian的数字吗'
str1 = 'Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!NaYo.NaYo?Ayo!Ayo!NaYo?NaYo.NaYo?Ayo,Ayo!Ayo!NaYo?NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!Ayo!NaYo?Ayo!Ayo!Ayo!Ayo!Ayo!NaYo?Ayo!Ayo!Ayo!Ayo!Ayo,Ayo!NaYo?NaYo.Ayo!Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!NaYo?NaYo?NaYo?Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!NaYo?Ayo,NaYo?Ayo,Ayo!NaYo?Ayo!Ayo!Ayo!Ayo!NaYo?Ayo!Ayo!NaYo?Ayo!NaYo?NaYo.NaYo?NaYo?NaYo?NaYo?Ayo!Ayo!Ayo!NaYo?Ayo,NaYo?Ayo!Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!Ayo!Ayo!Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!Ayo!NaYo?NaYo?NaYo?Ayo,NaYo?NaYo?NaYo?Ayo!Ayo!NaYo?Ayo,NaYo?Ayo!NaYo?NaYo?Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!NaYo?NaYo?NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!NaYo?Ayo!Ayo!Ayo!NaYo?Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!Ayo,Ayo!Ayo!NaYo?NaYo?NaYo.Ayo!Ayo,Ayo!NaYo?Ayo,Ayo!NaYo?Ayo!NaYo?NaYo?NaYo.NaYo?NaYo.NaYo?Ayo!NaYo?NaYo?Ayo!Ayo,Ayo!Ayo,Ayo!NaYo?NaYo?Ayo!NaYo.Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!NaYo?Ayo!Ayo,Ayo!NaYo?Ayo!Ayo,Ayo!NaYo?Ayo,NaYo?NaYo?NaYo?Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!Ayo,NaYo?Ayo,Ayo!Ayo!NaYo?Ayo!NaYo?NaYo.Ayo!Ayo!NaYo?Ayo!Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!NaYo.Ayo!Ayo!Ayo,Ayo!Ayo!NaYo.NaYo?Ayo,NaYo?Ayo!NaYo.NaYo?Ayo!Ayo!NaYo?NaYo?Ayo!NaYo?NaYo?NaYo?NaYo.NaYo?Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!Ayo!' 
# str2 ='vivo 50 查看原文'
str2 = 'NaYo?Ayo!Ayo,Ayo!Ayo!NaYo?Ayo!Ayo!NaYo?Ayo,NaYo?NaYo.Ayo!Ayo!NaYo.NaYo?Ayo!NaYo?NaYo.NaYo?Ayo!NaYo?Ayo!Ayo!Ayo!NaYo?Ayo!Ayo!NaYo.NaYo?NaYo?NaYo.Ayo!Ayo!NaYo?Ayo!Ayo!Ayo!Ayo!NaYo.NaYo?NaYo.NaYo?Ayo!NaYo?NaYo.NaYo?NaYo?NaYo?NaYo?NaYo?NaYo?Ayo!NaYo.Ayo!Ayo,NaYo?Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!Ayo!Ayo,NaYo?Ayo,NaYo?NaYo?NaYo?Ayo,NaYo?NaYo?NaYo.Ayo!NaYo.NaYo?NaYo?NaYo?NaYo.NaYo?NaYo?Ayo!NaYo.Ayo!Ayo!NaYo?NaYo?Ayo!NaYo.Ayo!NaYo?Ayo!Ayo,NaYo?NaYo.NaYo?Ayo!Ayo!Ayo!Ayo,Ayo!Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!Ayo,Ayo!NaYo.Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!Ayo,Ayo!NaYo.Ayo!NaYo.NaYo?Ayo,NaYo?Ayo!Ayo,Ayo!Ayo!Ayo,NaYo?NaYo?Ayo,Ayo!NaYo.NaYo?NaYo?NaYo?Ayo!NaYo?Ayo!Ayo,Ayo!Ayo!Ayo!Ayo,Ayo!NaYo?NaYo?NaYo.Ayo!NaYo?Ayo!Ayo!NaYo?NaYo?NaYo?Ayo!Ayo!NaYo.Ayo!NaYo?Ayo!NaYo?NaYo.NaYo?Ayo!NaYo.Ayo!Ayo!Ayo!Ayo!Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!NaYo.Ayo!NaYo.NaYo?Ayo!NaYo?NaYo?Ayo!Ayo,NaYo?Ayo!Ayo!Ayo,NaYo?NaYo.Ayo!NaYo.NaYo?NaYo?Ayo,NaYo?NaYo?Ayo,Ayo!Ayo!Ayo!Ayo,'
# str3 = 'So.请输入^_^:'
str3 = 'NaYo?Ayo!NaYo?NaYo.Ayo!NaYo?NaYo?Ayo!Ayo!NaYo?Ayo!Ayo!NaYo?NaYo.Ayo!Ayo!Ayo!Ayo,Ayo!NaYo?NaYo.NaYo?Ayo!NaYo?Ayo,Ayo!Ayo!NaYo.Ayo!NaYo?NaYo.Ayo!Ayo!Ayo!NaYo?Ayo!NaYo?Ayo,NaYo?NaYo?NaYo.Ayo!NaYo?Ayo!Ayo,NaYo?NaYo.Ayo!Ayo!Ayo!Ayo!Ayo,Ayo!Ayo,NaYo?Ayo!Ayo!NaYo?Ayo!NaYo.Ayo!Ayo!Ayo!Ayo!Ayo!NaYo?Ayo!NaYo?NaYo.NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!Ayo,Ayo!Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!NaYo?NaYo?NaYo.Ayo!Ayo!Ayo!Ayo!Ayo!NaYo?NaYo?Ayo!NaYo?Ayo,Ayo!Ayo!NaYo?NaYo.NaYo?NaYo?NaYo?Ayo!NaYo.NaYo?Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!Ayo,NaYo?Ayo!NaYo?NaYo.Ayo!NaYo?Ayo,Ayo!Ayo!Ayo!NaYo.Ayo!NaYo?NaYo.NaYo?Ayo!NaYo?Ayo!Ayo,Ayo!Ayo!Ayo!NaYo.Ayo!NaYo.NaYo?Ayo,Ayo!NaYo?Ayo,Ayo!Ayo!Ayo!Ayo!NaYo.NaYo?NaYo.NaYo?NaYo?Ayo!Ayo!Ayo!NaYo?Ayo!NaYo.NaYo?'
# str4 = 'Wait, what the fuck is this?（。皿。メ）'
str4 = 'NaYo?Ayo!NaYo.NaYo?NaYo.Ayo!NaYo?Ayo!NaYo.Ayo!Ayo,Ayo!NaYo.NaYo?Ayo!Ayo!NaYo?NaYo?NaYo.NaYo?NaYo.NaYo?Ayo!NaYo?Ayo!Ayo!NaYo?Ayo!NaYo.NaYo?NaYo?Ayo!NaYo?Ayo!NaYo.Ayo!NaYo.Ayo!NaYo?NaYo.Ayo!NaYo?NaYo.NaYo?NaYo?NaYo.NaYo?Ayo!NaYo.NaYo?Ayo!Ayo!NaYo?Ayo,NaYo?NaYo.NaYo?NaYo.NaYo?Ayo!NaYo?NaYo?Ayo,NaYo?NaYo?NaYo?NaYo?Ayo!Ayo!Ayo!Ayo,NaYo?Ayo!Ayo!Ayo!Ayo,NaYo?Ayo!Ayo!NaYo?Ayo,Ayo!Ayo,NaYo?Ayo,NaYo?NaYo?NaYo?Ayo!Ayo!NaYo?NaYo?Ayo,NaYo?NaYo?Ayo!Ayo,NaYo?Ayo!Ayo!Ayo!NaYo?Ayo!NaYo.NaYo?Ayo,NaYo?Ayo,NaYo?NaYo?Ayo!NaYo?NaYo.NaYo?NaYo?Ayo,NaYo?NaYo?NaYo?Ayo!Ayo,Ayo!Ayo!NaYo?NaYo.Ayo!NaYo?NaYo.NaYo?NaYo?NaYo.Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?NaYo.NaYo?NaYo?Ayo!Ayo!NaYo.NaYo?Ayo,NaYo?NaYo.Ayo!NaYo?Ayo,Ayo!Ayo,NaYo?NaYo?Ayo,Ayo!NaYo?NaYo?NaYo?NaYo?NaYo.NaYo?NaYo?Ayo!Ayo,Ayo!NaYo?NaYo?Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!Ayo!NaYo.NaYo?Ayo!NaYo?Ayo!NaYo?Ayo!Ayo,Ayo!Ayo,NaYo?NaYo?NaYo?Ayo,Ayo!Ayo!NaYo?Ayo,Ayo!NaYo.Ayo!NaYo?Ayo!NaYo?Ayo!NaYo.Ayo!Ayo,NaYo?Ayo,NaYo?Ayo,Ayo!NaYo?NaYo?Ayo,NaYo?NaYo?NaYo.NaYo?NaYo?Ayo!Ayo,Ayo!NaYo?NaYo.Ayo!NaYo?NaYo?Ayo,Ayo!NaYo?Ayo!NaYo.Ayo!Ayo!NaYo.NaYo?NaYo?NaYo.Ayo!Ayo,Ayo!NaYo?NaYo?Ayo!NaYo?NaYo?NaYo?NaYo?NaYo.NaYo?NaYo?Ayo!Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?NaYo?NaYo.Ayo!Ayo!NaYo?Ayo,Ayo!NaYo?NaYo?NaYo?NaYo?Ayo!Ayo!NaYo?Ayo!Ayo,NaYo?Ayo,NaYo?Ayo!NaYo?Ayo!NaYo.Ayo!Ayo!NaYo?NaYo?NaYo.Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!Ayo,Ayo!Ayo!Ayo!Ayo!Ayo!Ayo,Ayo!Ayo!NaYo?Ayo!NaYo.Ayo!Ayo!Ayo,Ayo!Ayo!NaYo?Ayo!NaYo.Ayo!Ayo!Ayo!Ayo,NaYo?NaYo?Ayo!Ayo,NaYo?NaYo?NaYo?NaYo.Ayo!NaYo?NaYo?NaYo?NaYo.Ayo!Ayo!Ayo!NaYo?NaYo?NaYo?Ayo!Ayo!Ayo!NaYo.NaYo?NaYo.NaYo?Ayo,NaYo?NaYo?NaYo.NaYo?NaYo?NaYo?Ayo!Ayo,NaYo?Ayo,NaYo?NaYo?Ayo,NaYo?NaYo.NaYo?Ayo!Ayo,NaYo?Ayo!NaYo.Ayo!NaYo.Ayo!NaYo?NaYo?Ayo!Ayo!Ayo!Ayo,Ayo!Ayo,NaYo?Ayo,NaYo?Ayo!Ayo!Ayo,NaYo?Ayo!NaYo.NaYo?Ayo!NaYo?Ayo!Ayo!Ayo!Ayo!Ayo!Ayo!Ayo!Ayo!NaYo.Ayo!NaYo?Ayo,NaYo?NaYo.NaYo?Ayo!Ayo!NaYo.Ayo!Ayo,NaYo?NaYo?NaYo?NaYo?NaYo?NaYo?NaYo?Ayo,Ayo!NaYo?NaYo?NaYo?NaYo?Ayo,NaYo?Ayo,Ayo!NaYo?Ayo!Ayo!Ayo!NaYo?NaYo?NaYo?Ayo!Ayo!Ayo!NaYo?NaYo?NaYo?NaYo?NaYo?Ayo!Ayo!Ayo!NaYo?NaYo.Ayo!NaYo?NaYo?Ayo,NaYo?NaYo?NaYo.Ayo!Ayo!NaYo.Ayo!Ayo!NaYo?Ayo!Ayo!Ayo!Ayo,Ayo!Ayo!NaYo?NaYo.Ayo!Ayo,Ayo!Ayo!Ayo!NaYo?NaYo.NaYo?NaYo.Ayo!Ayo,NaYo?NaYo?NaYo?Ayo!NaYo?NaYo?Ayo!'
# str5 ='50'
str5 = 'NaYo?NaYo?NaYo.Ayo!Ayo!NaYo?Ayo!NaYo.NaYo?NaYo.Ayo!NaYo?NaYo.NaYo?Ayo!Ayo!NaYo?NaYo?NaYo.NaYo?NaYo?'
# str6 ='17'
str6 = 'NaYo?NaYo?Ayo,Ayo!Ayo!NaYo?NaYo?NaYo.NaYo?Ayo,Ayo!NaYo?Ayo,NaYo?Ayo!Ayo!NaYo.NaYo?Ayo!Ayo!Ayo!NaYo.'
# str7 ='hint:Double Digit'
str7 = 'NaYo?Ayo!Ayo!Ayo,NaYo?Ayo!NaYo.NaYo?NaYo?NaYo?NaYo?Ayo,Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!NaYo?Ayo,Ayo!Ayo!Ayo!NaYo.NaYo?NaYo?Ayo!Ayo!Ayo!NaYo?Ayo!NaYo?Ayo,NaYo?NaYo?NaYo?Ayo,Ayo!NaYo.Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!NaYo?NaYo?NaYo?Ayo!NaYo?NaYo?NaYo?Ayo!Ayo!NaYo?NaYo.Ayo!Ayo!Ayo,Ayo!Ayo!NaYo?Ayo!Ayo!Ayo!NaYo?Ayo!NaYo?Ayo!Ayo,NaYo?Ayo!Ayo!NaYo?NaYo.NaYo?NaYo?NaYo.Ayo!NaYo?NaYo?Ayo,Ayo!Ayo,Ayo!NaYo?Ayo!Ayo!NaYo.NaYo?NaYo?NaYo.NaYo?Ayo!NaYo.Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!NaYo?NaYo?NaYo?NaYo?NaYo.NaYo?NaYo?Ayo!NaYo?Ayo,NaYo?NaYo?Ayo!NaYo?NaYo?NaYo?Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!NaYo?NaYo?Ayo!Ayo!Ayo!NaYo?Ayo!Ayo!NaYo?Ayo!NaYo?NaYo?Ayo!NaYo?Ayo!Ayo!Ayo!NaYo.NaYo?Ayo!NaYo?NaYo?'

#闪烁
def flash(time_interval=0.4,interval=10):
    colors = [Fore.LIGHTRED_EX,Fore.LIGHTGREEN_EX,Fore.LIGHTYELLOW_EX,Fore.LIGHTBLUE_EX,Fore.LIGHTMAGENTA_EX,Fore.LIGHTCYAN_EX,Fore.LIGHTWHITE_EX]
    color = random.choice(colors)
    for i in range(50):  
            print(color+'.', end='', flush=True)  #flush=True确保立即打印  
            if (i + 1) % interval == 0:  
                time.sleep(time_interval)

#彩蛋
def cadeaux():
    print(Tokyo_encode(Tokyo_decode(strs))+"\n")
    flash(0.1,1)
    print("\n"+Tokyo_decode(str4))
    time.sleep(2)
    flash()
    print(Tokyo_decode(str2))
    time.sleep(2)
    print(Tokyo_decode(str3),end='')
    while True:
        num1 = input()
        if num1 == Tokyo_decode(str5):
            flash()
            print("Yes,you got it! ")
            time.sleep(1)
            print("原文："+Tokyo_decode(str1))
            flash(0.1,2)
            print(Tokyo_decode(str7))
            while True:
                num2 =input()
                if num2 == Tokyo_decode(str6):
                    flash(0.1,2)
                    print(Tokyo_decode(strs))
                    print('唔，你也想听听吗◑ ▽ ◐'+"\n"+color+50*'.',end='')
                    time.sleep(3)
                    print('由不得你咯')
                    time.sleep(1)
                    webbrowser.open('https://www.bilibili.com/video/BV1as411D7rn/?spm_id_from=333.337.search-card.all.click&vd_source=b54b50c65bd1969fbff055b5a7835457')
                    break
                else:
                    flash(0.1,2)
                    print("Sorry! Have a try again")
            print("That's all.Nian praises you!")
            input()
            break
        else:
            flash(0.4,8)
            print('Worong.Brokenman!もう一度')

#加解密模块
def magic():
    mitsuha = """
    __  __ _ _             _           
    |  \/  (_) |_ ___ _   _| |__   __ _ 
    | |\/| | | __/ __| | | | '_ \ / _` |
    | |  | | | |_\__ \ |_| | | | | (_| |
    |_|  |_|_|\__|___/\__,_|_| |_|\__,_|    """
    print(mitsuha,end=""+Fore.RED+"Author:SuzukaGozen Version:1.0")
    print("                                        ")
    print("                                        ")
    print("\n"+"东京不太热加解密")
    flash()
    print("NaYo语和人语的切换器")
    while(True):
        print("1:加密模式"+"\n"+"2:解密模式"+"\n"+"3:退出")
        mode = input()
        if mode=='1':
            print("输入想转NaYo语的文本：",end='')
            strs = input()
            print("\n"+"NaYo密文："+Fore.YELLOW+Tokyo_encode(strs)+"\n"+50*'.')
        elif mode=='2':
            print("输入想解密的NaYo语：",end='')
            strs = input()
            #空字符串异常抛出
            print("\n"+"原文："+Fore.LIGHTRED_EX+Tokyo_decode(strs)+"\n"+50*'.')
        elif mode=='3':
            sys.exit()
        else:print(color+"\n"+"Are you Sure o_O?"+"\n"+50*'.')
        time.sleep(0.5)
  
def main():  
    parser = argparse.ArgumentParser(description='Process some integers.')  
    parser.add_argument('-magic', '--magic-option', action='store_true', help='Encoding and decoding') 
    parser.add_argument('-cadeaux','--cadeaux-option',action='store_true',help='Go find that Easter egg') 
    # parser.add_argument('','',action='',help='')
    args = parser.parse_args()  
    if args.magic_option:  
        magic()  
    elif args.cadeaux_option:
        cadeaux() 
    else:
        magic()
  
if __name__ == "__main__":  
    main()