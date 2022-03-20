n = input()
t = input()
ts = list(t)

now_position = [0,0]
now_houkou = [1,0]
for i in range(len(ts)):
    if ts[i] == 'S':
        now_position[0] += now_houkou[0]
        now_position[1] += now_houkou[1]
    else:
        if now_houkou[0] == 1 and now_houkou[1] == 0:
            now_houkou = [0, -1]
        elif now_houkou[0] == 0 and now_houkou[1] == -1:
            now_houkou = [-1, 0]
        elif now_houkou[0] == -1 and now_houkou[1] == 0:
            now_houkou = [0, 1]
        elif now_houkou[0] == 0 and now_houkou[1] == 1:
            now_houkou = [1, 0]
print(now_position[0], now_position[1])