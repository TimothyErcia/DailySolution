"""
Good morning! Here's your coding interview problem for today.
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C,
replace the color of the given pixel and all adjacent same colored pixels with C.
For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:
B B W
W W W
W W W
B B B
Becomes
B B G
G G G
G G G
B B B
"""

def changeColorCode(items, OldcolorCharacter, NewcolorCharacter):
    position_X = 0
    position_Y = 0
    max_X = len(items[0])
    max_Y = len(items)
    newItems = []
    c1 = ""
    try:
        while position_Y is not max_Y:
            while position_X is not max_X:
                if items[position_Y][position_X] == OldcolorCharacter:
                    c1 = items[position_Y][position_X].replace(OldcolorCharacter, NewcolorCharacter)
                    newItems.append(c1)
                elif items[position_Y][position_X] is not OldcolorCharacter:
                    newItems.append(items[position_Y][position_X])
                position_X+=1
            position_X = 0
            print(newItems)
            newItems.clear()
            position_Y+=1
    except:
        pass
    return newItems

item2 = [['B' ,'B' ,'W'],
        ['W', 'W' ,'W'],
        ['W', 'W' ,'W'],
        ['B', 'B' ,'B']]


cc = changeColorCode(item2, 'W', 'G')
print(cc)


