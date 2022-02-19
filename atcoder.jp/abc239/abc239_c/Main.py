x1, y1, x2, y2= map(int, input().split())

one_cans = [[x1+1, y1+2], [x1+1, y1-2], [x1-1, y1+2], [x1-1, y1-2], [x1+2, y1+1], [x1+2, y1-1], [x1-2, y1+1], [x1-2, y1-1]]
two_cans = [[x2+1, y2+2], [x2+1, y2-2], [x2-1, y2+2], [x2-1, y2-2], [x2+2, y2+1], [x2+2, y2-1], [x2-2, y2+1], [x2-2, y2-1]]

hantei = 'No'

for one_item in one_cans:
    for two_item in two_cans:
        if one_item[0] == two_item[0] and one_item[1] == two_item[1]:
            hantei = 'Yes'
print(hantei)