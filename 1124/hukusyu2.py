import math
kakudo = float(input("角度を入力してください(度):"))
angle = kakudo * math.pi/180
print(f"{kakudo}度->{angle}ラジアン")
print(f'sin({kakudo})=>{math.sin(angle)}')