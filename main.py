import random
cards = [2,3,4,5,6,7,8,9,10,"j","q","k","a",2,3,4,5,6,7,8,9,10,"j","q","k","a",2,3,4,5,6,7,8,9,10,"j","q","k","a",2,3,4,5,6,7,8,9,10,"j","q","k","a"]
p1=[]
p2=[]
p1num=[]
p2num=[]
p1War=[]
p2War=[]
while len(cards)>0:
    addCard=cards[random.randint(0,len(cards)-1)]
    p1.append(addCard)
    cards.pop(cards.index(addCard))

    addCard=cards[random.randint(0,len(cards)-1)]
    p2.append(addCard)
    cards.pop(cards.index(addCard))
print(f"p1H: {p1}\np2H:{p2}")


def faceConvert(player:list, outputList:list):
    for card in player:
        if type(card) is str:
            match card:
                case "j":
                    cardVal=11
                case "q":
                    cardVal=12
                case "k":
                    cardVal=13
                case "a":
                    cardVal=14
            outputList.append(cardVal)
        else:
            outputList.append(card)
    print(f"OutputList: {outputList}")

def warDraw(p1:list, p2:list):
    global p1War,p2War
    print(f"original:\np1:{p1}\np2:{p2}")
    try:
        for i in range(3):
            p1War.append(p1[-1])
            p1.pop()
        for j in range(3):
            p2War.append(p2[-1])
            p2.pop()
        print(f"p1war: {p1War}\np2war:{p2War}")
        if p1War[1] == p2War[1]:
            warDraw(p1,p2)
        elif p1War[1] > p2War[1]: #Face down card check to see if one greater than other 
            p1[0:0]=p2War+p1War
            print(f"Player one won the war!\n\np1:{p1}\np2:{p2}")
        else:
            p2[0:0]=p1War+p2War
            print(f"Player two won the war!\n\np1:{p1}\np2:{p2}")

    except IndexError:
        print(f"Index oor: lenof lists: p1:{len(p1)}, p2:{len(p2)}")
        if len(p1) < 3:
            p2.extend(p1)
            p1.clear()
        else:
            p1.extend(p2)
            p2.clear()
    p1War=[]
    p2War=[]

def faceOff(p1:list, p2:list):
   while len(p1) > 0 or len(p2)> 0:
        p1Card=p1[-1]
        p2Card=p2[-1]
        if p1Card == p2Card:
            warDraw(p1,p2)
        elif p1Card > p2Card:
            p1.insert(0,p2Card)
            p2.pop()
            print(f"success")
        else:
            p2.insert(0,p1Card)
            p1.pop()
            print(f"success")


faceConvert(p1, p1num)
faceConvert(p2, p2num)
faceOff(p1num, p2num)