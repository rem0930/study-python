class NameCheck:
    
    def __init__(self, text):
        self.text = text
        self.length = 0
        print("init")
        
    def text_len(self):
        for i in self.text:
            self.length = self.length+1
        return self.length
    
    def even_or_odd(self):
        if self.length % 2 == 0:
            return '偶数'
        else:
            return '奇数'

x1 = 'たろう'
print("rem")
# クラス『NameCheck』をインスタンス化
nc_ta = NameCheck(x1)
print("araki")
# 変数lengthに格納されている値を呼び出す
len1 = nc_ta.length
print(len1)
# 文字数を測る関数text_lenを実行
y1 = nc_ta.text_len()
print(y1)
len2 = nc_ta.length
print(len2)
y2 = nc_ta.even_or_odd()
print(y2)
