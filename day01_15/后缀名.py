'''
Created on 2019年06月10日
获取文件后缀名
@author: xieziwei99
'''
def get_suffix(filename, has_dot=False):
    '''
    获取文件后缀名
    :has_dot: 后缀名是否需要带点
    '''
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos+1
        return filename[index:]
    else:
        return ""

def main():
    print(get_suffix("craps.py"))

if __name__ == '__main__':
    main()