import math

# ラジアンについて
# https://juken-mikata.net/how-to/mathematics/radian.html
input_angle = float(input('角度を入力してください（度）：'))
rad = input_angle*math.pi/180
print("{}度->{} ラジアン".format(input_angle,rad))
print(f"sin({input_angle})=>{math.sin(rad)}")