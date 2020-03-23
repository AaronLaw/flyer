#
# 下载的文件名总是「乱码」？这里有各平台的解决方法 - 少数派. https://sspai.com/post/44360
#  乱码  python gbk to unicode  -> bulk big5 to unicode -> big5轉utf8工具-> python iconv -> https://www.letiantian.me/2014-10-14-python-convert-file-encoding/
# !/usr/bin/python
# 亂碼 1/2 更新記錄 https://openhome.cc/Gossip/EncodingUpdate.html
# -*- encoding:utf-8 -*-

import chardet, codecs, os

import sys
#reload(sys)
#sys.setdefaultencoding('UTF-8')

def detect_file_encoding(file_path):
    ''' 返回文件的编码 '''
    f = open(file_path, 'r')
    data = f.read()
    predict =  chardet.detect(data)
    f.close()
    return predict['encoding']

def get_file_content(file_path):
    ''' 获取文件内容，最终为utf-8 '''
    file_encoding = detect_file_encoding(file_path)
    if file_encoding is None:
        return ''
    f = codecs.open(file_path, 'r', file_encoding, errors="ignore")
    data = f.read()
    f.close()
    return data

def get_all_file(dir_path):
    ''' 获取 dir_path下的所有文件的路径 '''
    dir_list = [dir_path]
    file_list = []

    while len(dir_list) != 0:
        # print dir_list
        curr_dir = dir_list.pop(0)
        for path_name in os.listdir(curr_dir):
            full_path = os.path.join(curr_dir, path_name)
            if os.path.isdir(full_path):
                dir_list.append(full_path)
            else:
                file_list.append(full_path)
    return file_list

def write2file(content, file_path):
    ''' 将utf-8编码的content写入文件file_path '''

    with codecs.open(file_path, 'w', 'utf-8', errors='ignore') as f:
        f.write(content)

def del_file(file_path):
    ''' 删除文件 '''
    os.remove(file_path)


def translate_dir(dir_path):
    ''' 将整个目录下的所有文件转换为utf-8编码 '''
    for file_path in get_all_file(dir_path):
        # print file_path
        content = get_file_content(file_path)
        del_file(file_path)
        write2file(content, file_path)

def count_encoding_none(dir_path):
    ''' 看看哪些文件的编码为None '''
    all_num = 0
    none_num = 0
    none_files = []
    for file_path in get_all_file(dir_path):
        print(file_path)
        encoding = detect_file_encoding(file_path)
        all_num += 1
        if encoding is None:
            none_num += 1
            none_files.append(file_path)
    return all_num, none_num, none_files


if __name__ == '__main__':
    dir_path = './'
    translate_dir(dir_path)