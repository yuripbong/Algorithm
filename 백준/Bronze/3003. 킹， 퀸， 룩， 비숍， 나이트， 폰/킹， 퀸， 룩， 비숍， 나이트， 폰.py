king, queen, look, beshop, night, phone = map(int, input().split())

if king != 1:
    king -= 1
    king = -king
elif king == 1:
    king = 0
    
if queen != 1:
    queen -= 1
    queen = -queen
elif queen == 1:
    queen = 0
    
if look != 2:
    look -= 2
    look = -look
elif look == 2:
    look = 0
    
if beshop != 2:
    beshop -= 2
    beshop = -beshop
elif beshop == 2:
    beshop = 0
    
if night != 2:
    night -= 2
    night = -night
elif night == 2:
    night = 0
    
if phone != 8:
    phone -= 8
    phone = -phone
elif phone == 8:
    phone = 0
    
print(king, queen, look, beshop, night, phone)