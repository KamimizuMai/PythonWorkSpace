# グローバル変数とローカル変数
var_global = 100

def func():
    print(var_global)
    var_local ='A'
    print(var_local)

print(var_global)
func()
# print(var_local)



# p168

vote_box = []
label = '票'

def vote():
    print('投票します')
    vote_box.append(label)

def reset_box():
    print('箱を空にします')
    vote_box.clear()

def check_box():
    print('票の数は{}です'.format(len(vote_box)),end=" ")
    print('vote_box:',vote_box)



check_box()
for i in range(10):
    vote()
check_box()
reset_box()
vote()
vote()
check_box()