# _*_ coding:utf8 _*_

#   调用c语言模块
#   c语言动态连接库生成命令 gcc -o lib(这里是c语言文件名).so -shared -fPIC c语言文件名.c
#   c++语言动态连接库生成命令 g++ -o lib(这里是c++语言文件名).so -shared -fPIC c++语言文件名.c
import ctypes

ll = ctypes.cdll.LoadLibrary
lib_c = ll("./libtest.so")
lib_c.foo(1,3)
lib_cc = ll("./libfoo_cpp.so")
lib_cc.display_int()