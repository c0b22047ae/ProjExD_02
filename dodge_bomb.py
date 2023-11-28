import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900

delta = {  #練習3　押したキーと移動量の辞書
    pg.K_UP:(0,-5),   #キー：移動量／値:(横方向移動量、縦方向移動量)
    pg.K_DOWN:(0,+5),  
    pg.K_LEFT:(-5,0),  
    pg.K_RIGHT:(+5,0)  
}  

direction = {
    (+5,+5):0,
    (+5,-5):45,
    (0,-5):90,
    (-5,-5):135,
    (-5,0):180,
    (-5,+5):-135,
    (0,+5):-90,
    (+5,+5):-45
}

def check_bound(rct:pg.Rect) -> tuple[bool,bool]:

    yoko,tate = True,True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
    return yoko,tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()  #練習3 こうかとんのSurfaceRectを抽出する
    kk_rct.center = 900,400  #こうかとんの初期座標
    bom_img = pg.Surface((20,20))  #練習1　透明のSurfaceを作る
    pg.draw.circle(bom_img,(255,0,0),(10,10),10)  #練習１　赤い半径10の円を描く
    bom_img.set_colorkey((0,0,0)) #S練習１　黒い部分を透明にする
    bom_rct = bom_img.get_rect()  #練習1　爆弾SurfaceのRectを抽出する
    bom_rct.centerx = random.randint(0,WIDTH)
    bom_rct.centery = random.randint(0,HEIGHT)
    vx,vy = +5,+5  #練習2　爆弾の速度
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        if kk_rct.colliderect(bom_rct):
            print("game over")
            return
            
        key_lst = pg.key.get_pressed()
        sum_mv = [0,0]
        for k,tpl in delta.items():
            if key_lst[k]:  #練習3　キーが押されたら
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]
        screen.blit(bg_img, [0, 0])
        #screen.blit(kk_img, [900, 400])         
        kk_rct.move_ip(sum_mv[0],sum_mv[1]) 
        if check_bound(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])
        screen.blit(kk_img,kk_rct) #練習３　こうかとんを移動させる
        bom_rct.move_ip(vx,vy)  #練習2　爆弾を移動させる
        yoko,tate = check_bound(bom_rct)  
        if not yoko:  #横方向にはみ出たら
            vx *= -1
        if not tate:  #縦方向にはみ出たら
            vy *= -1         
        screen.blit(bom_img,bom_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()