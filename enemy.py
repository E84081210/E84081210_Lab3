import pygame
import math
import os
from settings import PATH

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))


class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 5
        self.max_health = 10
        self.path = PATH
        self.path_pos = 0
        self.move_count = 0
        self.stride = 1
        self.x, self.y = self.path[0]

    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        '''
        health_bar=pygame.draw.rect(win,(255,0,0),[self.x-20,self.y-23,40,5])
        max_health=pygame.draw.rect(win,(0,255,0),[self.x-20,self.y-23,20,5]) 
        初始寫法  缺乏考量敵人width 跟 height 
        '''
        #(set Health bar and follow position of enemy image)
        health_x=self.x-self.width//2
        health_y=self.y-self.height//2
        #(draw max health bar)
        pygame.draw.rect(win,(255,0,0),[health_x,health_y,self.width,5])
        health_remain=self.width*self.health/self.max_health
        #(draw remain health bar)
        pygame.draw.rect(win,(0,255,0),[health_x,health_y,health_remain,5])
        return

    def move(self):
        '''
            while self.move_count<len(PATH):
            self.x,self.y=self.path[self.move_count]
            self.move_count+=1
            return    初始寫法（缺乏後期修改彈性）
        '''
        ax,ay=self.path[self.path_pos]
        bx,by=self.path[self.path_pos+1]
        distance_A_B_=math.sqrt((ax-bx)**2+(ay-by)**2)
        max_step=int(distance_A_B_/ self.stride) # (total footstep between A&B)
        while self.move_count < max_step:
            unit_vector_x=(bx-ax)/distance_A_B_
            unit_vector_y=(by-ay)/distance_A_B_
            delta_x = unit_vector_x * self.stride
            delta_y = unit_vector_y * self.stride
            self.x+=delta_x
            self.y+=delta_y
            self.move_count+=1
        else:
            self.move_count=0
            self.path_pos+=1


class EnemyGroup:
    def __init__(self):
        self.gen_count = 0
        self.gen_period = 120  # (unit: frame)
        self.reserved_members = [Enemy(),Enemy(),Enemy()] #(初始三個)
        self.expedition = []

    def campaign(self):
        if len(self.reserved_members) > 0:
            if self.gen_count > self.gen_period:
                self.expedition.append(self.reserved_members.pop())
                #(用append()追加敵人 再用pop()刪除敵人)
                self.gen_count =0
            else:
                self.gen_count += 10
                #(數字越小，敵人間隔越大)
        else:
            return

    def generate(self, num):
        '''想不出來怎麼寫QQ'''
        pass

    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)





