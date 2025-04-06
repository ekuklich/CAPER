import pygame as pg, random


def upd(ris, i, j):
    raz = len(v)
    if (False):
        try:
            ris[i + 1][j] = True
        except:
            pass

        try:
            ris[i - 1][j] = True
        except:
            pass

        try:
            ris[i][j + 1] = True
        except:
            pass

        try:
            ris[i][j - 1] = True
        except:
            pass

        try:
            ris[i + 1][j + 1] = True
        except:
            pass
        try:
            ris[i - 1][j - 1] = True
        except:
            pass
        try:
            ris[i + 1][j - 1] = True
        except:
            pass
        try:
            ris[i - 1][j + 1] = True
        except:
            pass
    else:
        try:
            if (i + 1 < raz):
                ris[i + 1][j] = True
        except:
            pass

        try:
            if (i - 1 >= 0):
                ris[i - 1][j] = True
        except:
            pass

        try:
            if (j + 1 < raz):
                ris[i][j + 1] = True
        except:
            pass

        try:
            if (j - 1 >= 0):
                ris[i][j - 1] = True
        except:
            pass

        try:
            if (j + 1 < raz and i + 1 < raz):
                ris[i + 1][j + 1] = True
        except:
            pass
        try:
            if (j - 1 >= 0 and i - 1 >= 0):
                ris[i - 1][j - 1] = True
        except:
            pass
        try:
            if (j - 1 >= 0 and i + 1 < raz):
                ris[i + 1][j - 1] = True
        except:
            pass
        try:
            if (j + 1 < raz and i - 1 >= 0):
                ris[i - 1][j + 1] = True
        except:
            pass
    return ris


def findRect(v, a):
    for i in range(len(v)):
        for j in range(len(v[i])):
            if (v[i][j].colliderect(a)):
                return (i, j)


def cou_(v, i, j):
    cou1 = 0
    raz = len(v)
    try:
        if (v[i + 1][j] == -1 and i + 1 < raz):
            cou1 += 1
    except:
        pass

    try:
        if (v[i - 1][j] == -1 and i - 1 >= 0):
            cou1 += 1
    except:
        pass

    try:
        if (v[i][j + 1] == -1 and j + 1 < raz):
            cou1 += 1
    except:
        pass

    try:
        if (v[i][j - 1] == -1 and j - 1 >= 0):
            cou1 += 1
    except:
        pass

    try:
        if (v[i + 1][j + 1] == -1 and j + 1 < raz and i + 1 < raz):
            cou1 += 1
    except:
        pass
    try:
        if (v[i - 1][j - 1] == -1 and j - 1 >= 0 and i - 1 >= 0):
            cou1 += 1
    except:
        pass
    try:
        if (v[i + 1][j - 1] == -1 and j - 1 >= 0 and i + 1 < raz):
            cou1 += 1
    except:
        pass
    try:
        if (v[i - 1][j + 1] == -1 and j + 1 < raz and i - 1 >= 0):
            cou1 += 1
    except:
        pass

    return cou1


siz = 15
pg.font.init()
flag=pg.image.load("flag.png")
mina_png=pg.image.load("mina.png")
win = pg.display.set_mode((600, 600))
v = [[0 for _ in range(siz)] for _ in range(siz)]
cou = siz * siz // 10
raz = 600 / siz
kill=False

mina_png=pg.transform.scale(mina_png,(raz,raz))
flagi=[[False for _ in range(siz)] for _ in range(siz)]
ful=[[False for _ in range(siz)] for _ in range(siz)]
risi=[[True for _ in range(siz)] for _ in range(siz)]
flag=pg.transform.scale(flag,(raz,raz))
f1 = pg.font.Font(None, 1000 // siz)
vR = [[pg.Rect(i * raz + 1, j * raz + 1, raz - 2, raz - 2) for j in range(siz)] for i in range(siz)]
for i in range(cou):
    kk, mm = random.randint(0, siz - 1), random.randint(0, siz - 1)
    while(v[kk][mm]==-1):
        kk,mm=random.randint(0, siz - 1), random.randint(0, siz - 1)
    v[kk][mm] = -1
for i in range(len(v)):
    for j in range(len(v)):
        if(v[i][j]==-1):
            ful[i][j]=True
            risi[i][j]=False
First = True
print(v)
ris = [[False for _ in range(siz)] for _ in range(siz)]
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            exit()
        if (i.type == pg.MOUSEBUTTONDOWN):

            try:
                if(i.button==1):
                    pos = pg.mouse.get_pos()
                    mrect = (pos[0], pos[1], 1, 1)
                    ij = findRect(vR, mrect)
                    if not(flagi[ij[0]][ij[1]]):
                        ris[ij[0]][ij[1]] = True
                        if (First):
                            First = False
                            v[ij[0]][ij[1]] = 0
                            for i in range(siz):
                                for j in range(siz):
                                    if (v[i][j] != -1):
                                        v[i][j] = cou_(v, i, j)
                                    else:
                                        v[i][j] = -1
                        for kkk in range(siz):
                            for i in range(len(ris)):
                                for j in range(len(ris)):
                                    if (v[i][j] == 0 and ris[i][j] == True):
                                        ris = upd(ris, i, j)
                elif(i.button==3):
                    pos = pg.mouse.get_pos()
                    mrect = (pos[0], pos[1], 1, 1)
                    ij = findRect(vR, mrect)
                    if(ris[ij[0]][ij[1]]==False):
                        if(flagi[ij[0]][ij[1]]):
                            flagi[ij[0]][ij[1]]=False
                        else:
                            flagi[ij[0]][ij[1]]=True
            except:
                pass

    win.fill((0, 0, 0))
    for i in vR:
        for j in i:
            pg.draw.rect(win, (255, 255, 255), j)
    for i in range(siz):
        for j in range(siz):
            if (flagi[i][j]):
                win.blit(flag, vR[i][j])
                ris[i][j]=False
            if (ris[i][j]):
                text1 = f1.render(str(v[i][j]), True, (255, 0, 0))
                if(v[i][j]==-1):
                    win.blit(mina_png,vR[i][j])
                    kill=True
                else:
                    win.blit(text1, vR[i][j])

    pg.display.flip()
    if(kill):
        pg.time.delay(1000)

        exit()
    elif(ful==flagi and ris==risi):
        text1=f1.render("You WIN!!!", True, (255,0,0))
        win.fill((255,255,255))
        win.blit(text1,(100,300))
        pg.display.flip()
        pg.time.delay(2000)
        exit()
