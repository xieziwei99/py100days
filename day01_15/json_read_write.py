'''
Created on 2019年6月12日
用Python中的json模块就可以将字典或列表以JSON格式保存到文件中
@author: xieziwei99
'''
import json
def main():
    mydict = {
        'name': 'Jack',
        'age': 20,
        'qq': 123456789,
        'friends': ['Kangkang', 'Lucy'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    with open('data.json', 'w', encoding='utf-8') as fp:
        json.dump(mydict, fp)
    print('Save complete')
    
if __name__ == '__main__':
    main()