# -*- coding: utf-8 -*-
import pygame
import math
from pygame.locals import *

pygame.init()
color = pygame.Color

try:
    file = open('Memory.txt', 'r')
    num = file.readline()
    file.close()
except FileNotFoundError:
    file = open('Memory.txt', 'w')
    file.write('')
    file.close()


def write_text(surface, text, text_color, length, height, x, y):
    m = ['mc', 'm+', 'm-', 'mr', '(', ')', '!x', 'e', 'π', '1/x']
    m2 = ['(', ')', '√']
    f = 'Calibri'
    if text in m:
        f = 'Oral'
    font_size = int(length // len(text) + 10)
    if len(text) == 1 and text != '=':
        font_size = int(length // len(text) - (length+height)/3)
    elif text == '=':
        font_size = int(length // len(text) - (length+height)/5)
    elif len(text) == 2 and text != '!x':
        font_size = int(length // len(text) - (length+height)*0.13)
    elif text == 'y√x':
        font_size = int(length // len(text) - (length+height)*0.001)
    elif text == '!x':
        font_size = int(length // len(text) - (length + height)*0.09)
    elif text == '1/x':
        font_size = int(length // len(text) - (length + height)*0.012)
    if text in m2:
        font_size = int(length // len(text) - (length+height)*0.43)
    font = pygame.font.SysFont(f, font_size)
    text = font.render(text, 1, text_color)
    surface.blit(text, ((x + length / 2) - text.get_width() / 2, (y + height / 2) - text.get_height() / 2 + 2))
    return surface


def draw_button(surface, color, length, height, x, y):
    pygame.draw.rect(surface, color, (x, y, length, height), 0)
    pygame.draw.rect(surface, (190, 190, 190), (x, y, length, height), 1)
    return surface


class Button:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.buttons = []

    def create_button(self, surface, color, x, y, length, height, text, text_color, button_id):
        surface = draw_button(surface, color, length, height, x, y)
        surface = write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x, y, length, height)
        a = 0
        for button in self.buttons:
            if button_id == button['id']:
                i = self.buttons.index(button)
                del self.buttons[i]
                self.buttons.append({'id': button_id, 'button': self.rect})
                a = 1
        if a == 0:
            self.buttons.append({'id': button_id, 'button': self.rect})
        return surface

    def pressed(self, mouse):
        for button in self.buttons:
            if mouse[0] > button['button'].topleft[0]:
                if mouse[1] > button['button'].topleft[1]:
                    if mouse[0] < button['button'].bottomright[0]:
                        if mouse[1] < button['button'].bottomright[1]:
                            return button['id']


class Window:
    def __init__(self):
        self.Button = Button()
        self.d = True
        self.m_label_text = ''
        self.label_text = ''
        self.p_label_text = ''
        self.screen = pygame.display.set_mode((316, 560))
        self.vertical = int(str(self.screen).split('x')[1])
        self.horizontal = int(str(self.screen).split('(')[1].split('x')[0])
        self.length = int(self.horizontal) / 4
        self.height = self.length
        self.label_font = int((self.vertical - (self.height * 6)) / 4 + 5)
        self.p_label_font = int((self.vertical - (self.height * 6)) / 4 + 5) // 2
        self.level_label_font = [1, 0, 0, 0, 0, 0, 0]
        self.pol = 'vertical'
        if self.vertical == 560:
            self.user = 'pc'
        else:
            self.user = 'android'

        self.color_op = (0, 191, 255)
        self.color0 = color('White')
        self.color1 = color('White')
        self.color2 = color('White')
        self.color3 = (0, 191, 255)
        self.color4 = color('White')
        self.color5 = color('White')
        self.color6 = color('White')
        self.color7 = color('White')
        self.color8 = color('White')
        self.color9 = color('White')
        self.color10 = (245, 245, 245)
        self.color11 = color('White')
        self.color12 = color('White')
        self.color13 = color('White')
        self.color14 = (245, 245, 245)
        self.color15 = (245, 245, 245)
        self.color16 = (245, 245, 245)
        self.color17 = (245, 245, 245)
        self.color18 = (245, 245, 245)
        self.color19 = (245, 245, 245)
        self.color20 = (245, 245, 245)
        self.color21 = (245, 245, 245)
        self.color22 = (245, 245, 245)
        self.color23 = (245, 245, 245)
        self.color24 = (245, 245, 245)
        self.color25 = (245, 245, 245)
        self.color26 = (245, 245, 245)
        self.color27 = (220, 220, 220)
        self.color28 = (220, 220, 220)
        self.color29 = (220, 220, 220)
        self.color30 = (220, 220, 220)
        self.color31 = (220, 220, 220)
        self.color32 = (220, 220, 220)
        self.color33 = (220, 220, 220)

        self.main()

    def update_display(self):
        file = open('Memory.txt', 'r')
        num = file.readline()
        if len(num) != 0:
            self.m_label_text = 'M'
        else:
            self.m_label_text = ''
        self.screen.fill(color('White'))
        if self.pol == 'vertical':
            self.create_buttons()
        else:
            self.create_buttons_1()
        self.draw_label()
        self.draw_p_label()
        self.draw_m_label()
        pygame.display.flip()

    def back_color(self):
        self.color0 = color('White')
        self.color1 = color('White')
        self.color2 = color('White')
        self.color3 = (0, 191, 255)
        self.color4 = color('White')
        self.color5 = color('White')
        self.color6 = color('White')
        self.color7 = color('White')
        self.color8 = color('White')
        self.color9 = color('White')
        self.color10 = (245, 245, 245)
        self.color11 = color('White')
        self.color12 = color('White')
        self.color13 = color('White')
        self.color14 = (245, 245, 245)
        self.color15 = (245, 245, 245)
        self.color16 = (245, 245, 245)
        self.color17 = (245, 245, 245)
        self.color18 = (245, 245, 245)
        self.color19 = (245, 245, 245)
        self.color20 = (245, 245, 245)
        self.color21 = (245, 245, 245)
        self.color22 = (245, 245, 245)
        self.color23 = (245, 245, 245)
        self.color24 = (245, 245, 245)
        self.color25 = (245, 245, 245)
        self.color26 = (245, 245, 245)
        self.color27 = (220, 220, 220)
        self.color28 = (220, 220, 220)
        self.color29 = (220, 220, 220)
        self.color30 = (220, 220, 220)
        self.color31 = (220, 220, 220)
        self.color32 = (220, 220, 220)
        self.color33 = (220, 220, 220)

    def create_buttons(self):
        self.Button.create_button(self.screen, self.color0, 0, self.vertical - self.height, self.length, self.height, 'Close', color('Black'), button_id=0)
        self.Button.create_button(self.screen, self.color1, 0 + self.length, self.vertical - self.height, self.length, self.height, '0', color('Black'), button_id=1)
        self.Button.create_button(self.screen, self.color2, 0 + self.length * 2, self.vertical - self.height, self.length, self.height, '.', color('Black'), button_id=2)
        self.Button.create_button(self.screen, self.color3, 0 + self.length * 3, self.vertical - self.height * 2, self.length, self.height * 2, '=', color('White'), button_id=3)

        self.Button.create_button(self.screen, self.color4, 0, self.vertical - self.height * 2, self.length, self.height, '1', color('Black'), button_id=4)
        self.Button.create_button(self.screen, self.color5, 0 + self.length, self.vertical - self.height * 2, self.length, self.height, '2', color('Black'), button_id=5)
        self.Button.create_button(self.screen, self.color6, 0 + self.length * 2, self.vertical - self.height * 2, self.length, self.height, '3', color('Black'), button_id=6)

        self.Button.create_button(self.screen, self.color7, 0, self.vertical - self.height * 3, self.length, self.height, '4', color('Black'), button_id=7)
        self.Button.create_button(self.screen, self.color8, 0 + self.length, self.vertical - self.height * 3, self.length, self.height, '5', color('Black'), button_id=8)
        self.Button.create_button(self.screen, self.color9, 0 + self.length * 2, self.vertical - self.height * 3, self.length, self.height, '6', color('Black'), button_id=9)
        self.Button.create_button(self.screen, self.color10, 0 + self.length * 3, self.vertical - self.height * 3, self.length, self.height, '+', self.color_op, button_id=10)

        self.Button.create_button(self.screen, self.color11, 0, self.vertical - self.height * 4, self.length, self.height, '7', color('Black'), button_id=11)
        self.Button.create_button(self.screen, self.color12, 0 + self.length, self.vertical - self.height * 4, self.length, self.height, '8', color('Black'), button_id=12)
        self.Button.create_button(self.screen, self.color13, 0 + self.length * 2, self.vertical - self.height * 4, self.length, self.height, '9', color('Black'), button_id=13)
        self.Button.create_button(self.screen, self.color14, 0 + self.length * 3, self.vertical - self.height * 4, self.length, self.height, '–', self.color_op, button_id=14)

        self.Button.create_button(self.screen, self.color15, 0, self.vertical - self.height * 5, self.length, self.height, 'c', self.color_op, button_id=15)
        self.Button.create_button(self.screen, self.color16, 0 + self.length, self.vertical - self.height * 5, self.length, self.height, '÷', self.color_op, button_id=16)
        self.Button.create_button(self.screen, self.color17, 0 + self.length * 2, self.vertical - self.height * 5, self.length, self.height, '×', self.color_op, button_id=17)
        self.Button.create_button(self.screen, self.color18, 0 + self.length * 3, self.vertical - self.height * 5, self.length, self.height, '<–', self.color_op, button_id=18)

        self.Button.create_button(self.screen, self.color19, 0, self.vertical - self.height * 6+1, self.length, self.height/2, 'mc', (120, 120, 120), button_id=19)
        self.Button.create_button(self.screen, self.color20, 0 + self.length, self.vertical - self.height * 6+1, self.length, self.height/2, 'm+', (120, 120, 120), button_id=20)
        self.Button.create_button(self.screen, self.color21, 0 + self.length * 2, self.vertical - self.height * 6+1, self.length, self.height/2, 'm-', (120, 120, 120), button_id=21)
        self.Button.create_button(self.screen, self.color22, 0 + self.length * 3, self.vertical - self.height * 6+1, self.length, self.height/2, 'mr', (120, 120, 120), button_id=22)

        self.Button.create_button(self.screen, self.color23, 0, self.vertical - self.height * 6 + self.height/2+1, self.length, self.height/2, '(', (120, 120, 120), button_id=23)
        self.Button.create_button(self.screen, self.color24, 0 + self.length, self.vertical - self.height * 6 + self.height/2+1, self.length, self.height/2, ')', (120, 120, 120), button_id=24)
        self.Button.create_button(self.screen, self.color25, 0 + self.length * 2, self.vertical - self.height * 6 + self.height/2+1, self.length, self.height/2, '√', (120, 120, 120), button_id=25)
        self.Button.create_button(self.screen, self.color26, 0 + self.length * 3, self.vertical - self.height * 6 + self.height/2+1,  self.length, self.height/2, 'y√x', (120, 120, 120), button_id=26)

    def create_buttons_1(self):
        self.Button.create_button(self.screen, self.color0, self.length*1, self.vertical - self.height, self.length, self.height, 'Close', color('Black'), button_id=0)
        self.Button.create_button(self.screen, self.color1, self.length*2, self.vertical - self.height, self.length, self.height, '0', color('Black'), button_id=1)
        self.Button.create_button(self.screen, self.color2, self.length*3, self.vertical - self.height, self.length, self.height, '.', color('Black'), button_id=2)
        self.Button.create_button(self.screen, self.color3, self.length*4, self.vertical - self.height * 2, self.length, self.height * 2, '=', color('White'), button_id=3)

        self.Button.create_button(self.screen, self.color4, self.length*1, self.vertical - self.height * 2, self.length, self.height, '1', color('Black'), button_id=4)
        self.Button.create_button(self.screen, self.color5, self.length*2, self.vertical - self.height * 2, self.length, self.height, '2', color('Black'), button_id=5)
        self.Button.create_button(self.screen, self.color6, self.length*3, self.vertical - self.height * 2, self.length, self.height, '3', color('Black'), button_id=6)

        self.Button.create_button(self.screen, self.color7, self.length*1, self.vertical - self.height * 3, self.length, self.height, '4', color('Black'), button_id=7)
        self.Button.create_button(self.screen, self.color8, self.length*2, self.vertical - self.height * 3, self.length, self.height, '5', color('Black'), button_id=8)
        self.Button.create_button(self.screen, self.color9, self.length*3, self.vertical - self.height * 3, self.length, self.height, '6', color('Black'), button_id=9)
        self.Button.create_button(self.screen, self.color10, self.length*4, self.vertical - self.height * 3, self.length, self.height, '+', self.color_op, button_id=10)

        self.Button.create_button(self.screen, self.color11, self.length*1, self.vertical - self.height * 4, self.length, self.height, '7', color('Black'), button_id=11)
        self.Button.create_button(self.screen, self.color12, self.length*2, self.vertical - self.height * 4, self.length, self.height, '8', color('Black'), button_id=12)
        self.Button.create_button(self.screen, self.color13, self.length*3, self.vertical - self.height * 4, self.length, self.height, '9', color('Black'), button_id=13)
        self.Button.create_button(self.screen, self.color14, self.length*4, self.vertical - self.height * 4, self.length, self.height, '–', self.color_op, button_id=14)

        self.Button.create_button(self.screen, self.color15, self.length*1, self.vertical - self.height * 5, self.length, self.height, 'c', self.color_op, button_id=15)
        self.Button.create_button(self.screen, self.color16, self.length*2, self.vertical - self.height * 5, self.length, self.height, '÷', self.color_op, button_id=16)
        self.Button.create_button(self.screen, self.color17, self.length*3, self.vertical - self.height * 5, self.length, self.height, '×', self.color_op, button_id=17)
        self.Button.create_button(self.screen, self.color18, self.length*4, self.vertical - self.height * 5, self.length, self.height, '<–', self.color_op, button_id=18)

        self.Button.create_button(self.screen, self.color19, self.length*1, self.vertical - self.height * 6+1, self.length, self.height/2, 'mc', (120, 120, 120), button_id=19)
        self.Button.create_button(self.screen, self.color20, self.length*2, self.vertical - self.height * 6+1, self.length, self.height/2, 'm+', (120, 120, 120), button_id=20)
        self.Button.create_button(self.screen, self.color21, self.length*3, self.vertical - self.height * 6+1, self.length, self.height/2, 'm-', (120, 120, 120), button_id=21)
        self.Button.create_button(self.screen, self.color22, self.length*4, self.vertical - self.height * 6+1, self.length, self.height/2, 'mr', (120, 120, 120), button_id=22)

        self.Button.create_button(self.screen, self.color23, self.length*1, self.vertical - self.height * 6 + self.height/2+1, self.length, self.height/2, '(', (120, 120, 120), button_id=23)
        self.Button.create_button(self.screen, self.color24, self.length*2, self.vertical - self.height * 6 + self.height/2+1, self.length, self.height/2, ')', (120, 120, 120), button_id=24)
        self.Button.create_button(self.screen, self.color25, self.length*3, self.vertical - self.height * 6 + self.height/2+1, self.length, self.height/2, '√', (120, 120, 120), button_id=25)
        self.Button.create_button(self.screen, self.color26, self.length*4, self.vertical - self.height * 6 + self.height/2+1,  self.length, self.height/2, 'y√x', (120, 120, 120), button_id=26)

        self.Button.create_button(self.screen, self.color27, 0, self.vertical - self.height, self.length, self.height, 'e', (120, 120, 120), button_id=27)
        self.Button.create_button(self.screen, self.color28, 0, self.vertical - self.height * 2, self.length, self.height, 'π', (120, 120, 120), button_id=28)
        self.Button.create_button(self.screen, self.color29, 0, self.vertical - self.height * 3, self.length, self.height, '!x', (120, 120, 120), button_id=29)
        self.Button.create_button(self.screen, self.color30, 0, self.vertical - self.height * 4, self.length, self.height, '1/x', (120, 120, 120), button_id=30)
        self.Button.create_button(self.screen, self.color31, 0, self.vertical - self.height * 5, self.length, self.height, '±', (120, 120, 120), button_id=31)
        self.Button.create_button(self.screen, self.color32, 0, self.vertical - self.height * 6+self.height/2+1, self.length, self.height/2, 'xⁿ', (120, 120, 120), button_id=32)
        self.Button.create_button(self.screen, self.color33, 0, self.vertical - self.height * 6+1, self.length, self.height/2, ' ', (120, 120, 120), button_id=33)

    def draw_label(self):
        font = pygame.font.SysFont("Calibri", int(self.label_font))
        text = font.render(self.label_text, 1, color('Black'))
        if self.horizontal - text.get_width() - 10 < self.length/2 and self.level_label_font[0] == 1:
            self.level_label_font[0] = 2
            self.level_label_font[1] = len(self.label_text)-1
            self.level_label_font[2] = len(self.label_text)
        elif self.horizontal - text.get_width() - 10 < self.length/2 and self.level_label_font[0] == 2:
            self.level_label_font[0] = 3
            self.level_label_font[3] = len(self.label_text)
        elif self.horizontal - text.get_width() - 10 < self.length / 2 and self.level_label_font[0] == 3:
            self.level_label_font[0] = 4
            self.level_label_font[4] = len(self.label_text)
        elif self.horizontal - text.get_width() - 10 < self.length / 2 and self.level_label_font[0] == 4:
            self.level_label_font[0] = 5
            self.level_label_font[5] = len(self.label_text)
        elif self.horizontal - text.get_width() - 10 < self.length / 2 and self.level_label_font[0] == 5:
            self.level_label_font[0] = 6
            self.level_label_font[6] = len(self.label_text)
        if self.level_label_font[0] == 1:
            self.label_font = int((self.vertical - (self.height * 6)) / 4 + 5)
            self.p_label_font = int((self.vertical - (self.height * 6)) / 4 + 5) // 2
        elif self.level_label_font[0] == 2:
            self.label_font = int((self.vertical - (self.height * 6)) / 4 + 5)*0.7
        elif self.level_label_font[0] == 3:
            self.label_font = int((self.vertical - (self.height * 6)) / 4 + 5)*(0.7**2)
        elif self.level_label_font[0] == 4:
            self.label_font = int((self.vertical - (self.height * 6)) / 4 + 5)*(0.7**3)
        elif self.level_label_font[0] == 5:
            self.label_font = int((self.vertical - (self.height * 6)) / 4 + 5)*(0.7**4)
        elif self.level_label_font[0] == 6:
            self.label_font = int((self.vertical - (self.height * 6)) / 4 + 5)*(0.7**5)
        font = pygame.font.SysFont("Calibri", int(self.label_font))
        text = font.render(self.label_text, 1, color('Black'))
        if self.pol == 'vertical' or self.user == 'android':
            self.screen.blit(text, (self.horizontal-text.get_width()-10, (self.vertical-(self.height*6))/2-text.get_height()))
        else:
            self.screen.blit(text, (self.horizontal-text.get_width()-10+self.length, (self.vertical-(self.height*6))/2-text.get_height()))

    def draw_p_label(self):
        if self.label_text == '':
            self.p_label_text = ''
        font = pygame.font.SysFont("Calibri", int(self.p_label_font))
        text = font.render(self.p_label_text, 1, color('Gray'))
        if self.horizontal - text.get_width() - 10 < self.length/2:
            if self.p_label_font == int((self.vertical - (self.height * 6)) / 4 + 5) // 2:
                self.p_label_font *= 0.7
            elif self.p_label_font == int((self.vertical - (self.height * 6)) / 4 + 5) // 2 * 0.7:
                self.p_label_font *= 0.7
            elif self.p_label_font == int((self.vertical - (self.height * 6)) / 4 + 5) // 2 * 0.7*0.7:
                self.p_label_font *= 0.7
            elif self.p_label_font == int((self.vertical - (self.height * 6)) / 4 + 5) // 2 * 0.7*0.7*0.7:
                self.p_label_font *= 0.7
            font = pygame.font.SysFont("Calibri", int(self.p_label_font))
            text = font.render(self.label_text, 1, color('Gray'))
        if self.pol == 'vertical' or self.user == 'android':
            self.screen.blit(text, (self.horizontal-text.get_width()-10, (self.vertical-(self.height*6))/2-text.get_height()+text.get_height()*1.5))
        else:
            self.screen.blit(text, (self.horizontal-text.get_width()-10+self.length, (self.vertical-(self.height*6))/2-text.get_height()+text.get_height()*1.5))

    def draw_m_label(self):
        font = pygame.font.SysFont("Calibri", int((self.vertical-(self.height*6))/4+5)//3 + 3)
        text = font.render(self.m_label_text, 1, color('Gray'))
        self.screen.blit(text, (self.horizontal * 0.01, self.vertical * 0.01))

    def add_s(self, s):
        self.label_text = self.label_text.replace(' ', '')
        self.label_text = self.label_text.lstrip()
        self.label_text += s
        self.p_result()

    def check_add_s(self, s):
        op = ['+', '/', '.', '', '*', '-', '(', '√', '!', '^']
        if self.label_text == '':
            self.label_text = ' '
        if s in op:
            if s == '-':
                if self.label_text == ' ':
                    self.add_s(s)
                elif self.label_text[len(self.label_text) - 1] == '/':
                    self.add_s(s)
                elif self.label_text[len(self.label_text) - 1] == '*':
                    self.add_s(s)
                elif self.label_text[len(self.label_text) - 1] in op:
                    pass
                else:
                    self.add_s(s)
            elif s == '√':
                if self.label_text == ' ':
                    self.add_s(s)
                elif self.label_text[len(self.label_text) - 1] == '√':
                    pass
                else:
                    self.add_s(s)
            elif s == '!':
                if self.label_text == ' ':
                    self.add_s('!(')
                elif self.label_text[len(self.label_text) - 1] not in op:
                    pass
                else:
                    self.add_s('!(')
            elif s == '^':
                if self.label_text == ' ':
                    pass
                elif self.label_text[len(self.label_text) - 1] in op:
                    pass
                else:
                    self.add_s(s)
            else:
                if s == '(':
                    if self.label_text[len(self.label_text) - 1] not in op and self.label_text != ' ':
                        self.add_s('*(')
                    else:
                        self.add_s(s)
                elif self.label_text != ' ' and self.label_text[len(self.label_text) - 1] not in op:
                    self.add_s(s)
        else:
            if s == 'e':
                if self.label_text == ' ':
                    self.add_s('e')
                elif self.label_text[len(self.label_text) - 1] in op:
                    if self.label_text[len(self.label_text) - 1] != '.':
                        self.add_s('e')
                elif self.label_text[len(self.label_text) - 1] not in op:
                    self.add_s('*e')
            elif s == 'p':
                if self.label_text == ' ':
                    self.add_s('π')
                elif self.label_text[len(self.label_text) - 1] in op:
                    if self.label_text[len(self.label_text) - 1] != '.':
                        self.add_s('π')
                elif self.label_text[len(self.label_text) - 1] not in op:
                    self.add_s('*π')
            else:
                self.add_s(s)

    def visual_func(self, button_id):
        if button_id is not None:
            if button_id == 0:
                self.color0 = (180, 180, 180)
            elif button_id == 1:
                self.color1 = (220, 220, 220)
            elif button_id == 2:
                self.color2 = (220, 220, 220)
            elif button_id == 3:
                self.color3 = (0, 161, 225)
            elif button_id == 4:
                self.color4 = (220, 220, 220)
            elif button_id == 5:
                self.color5 = (220, 220, 220)
            elif button_id == 6:
                self.color6 = (220, 220, 220)
            elif button_id == 7:
                self.color7 = (220, 220, 220)
            elif button_id == 8:
                self.color8 = (220, 220, 220)
            elif button_id == 9:
                self.color9 = (220, 220, 220)
            elif button_id == 10:
                self.color10 = (220, 220, 220)
            elif button_id == 11:
                self.color11 = (220, 220, 220)
            elif button_id == 12:
                self.color12 = (220, 220, 220)
            elif button_id == 13:
                self.color13 = (220, 220, 220)
            elif button_id == 14:
                self.color14 = (220, 220, 220)
            elif button_id == 15:
                self.color15 = (220, 220, 220)
            elif button_id == 16:
                self.color16 = (220, 220, 220)
            elif button_id == 17:
                self.color17 = (220, 220, 220)
            elif button_id == 18:
                self.color18 = (220, 220, 220)
            elif button_id == 19:
                self.color19 = (220, 220, 220)
            elif button_id == 20:
                self.color20 = (220, 220, 220)
            elif button_id == 21:
                self.color21 = (220, 220, 220)
            elif button_id == 22:
                self.color22 = (220, 220, 220)
            elif button_id == 23:
                self.color23 = (220, 220, 220)
            elif button_id == 24:
                self.color24 = (220, 220, 220)
            elif button_id == 25:
                self.color25 = (220, 220, 220)
            elif button_id == 26:
                self.color26 = (220, 220, 220)
            elif button_id == 27:
                self.color27 = (200, 200, 200)
            elif button_id == 28:
                self.color28 = (200, 200, 200)
            elif button_id == 29:
                self.color29 = (200, 200, 200)
            elif button_id == 30:
                self.color30 = (200, 200, 200)
            elif button_id == 31:
                self.color31 = (200, 200, 200)
            elif button_id == 32:
                self.color32 = (200, 200, 200)
            elif button_id == 33:
                self.color33 = (200, 200, 200)

    def func(self, button_id):
        if button_id is not None:
            if button_id == 0:
                if self.label_text == '505':
                    if self.pol == 'vertical':
                        self.screen = pygame.display.set_mode((int(self.horizontal+self.length), self.vertical))
                        self.pol = 'horizontal'
                        if self.user == 'android':
                            self.length = int(self.horizontal) / 5
                    else:
                        self.screen = pygame.display.set_mode((self.horizontal, self.vertical))
                        self.pol = 'vertical'
                        if self.user == 'android':
                            self.length = int(self.horizontal) / 4
                        self.Button.buttons.clear()
                else:
                    self.d = False
            elif button_id == 1:
                self.check_add_s('0')
            elif button_id == 2:
                self.check_add_s('.')
            elif button_id == 3:
                self.result()
            elif button_id == 4:
                self.check_add_s('1')
            elif button_id == 5:
                self.check_add_s('2')
            elif button_id == 6:
                self.check_add_s('3')
            elif button_id == 7:
                self.check_add_s('4')
            elif button_id == 8:
                self.check_add_s('5')
            elif button_id == 9:
                self.check_add_s('6')
            elif button_id == 10:
                self.check_add_s('+')
            elif button_id == 11:
                self.check_add_s('7')
            elif button_id == 12:
                self.check_add_s('8')
            elif button_id == 13:
                self.check_add_s('9')
            elif button_id == 14:
                self.check_add_s('-')
            elif button_id == 15:
                self.label_text = ''
                self.p_label_text = ''
                self.level_label_font[0] = 1
            elif button_id == 16:
                self.check_add_s('/')
            elif button_id == 17:
                self.check_add_s('*')
            elif button_id == 18:
                if self.label_text != '':
                    i = len(self.label_text)
                    self.label_text = self.label_text[0:i - 1]
                    self.p_result()
                    if self.label_text == '':
                        self.p_label_text = ''
                    if len(self.label_text) < self.level_label_font[1]:
                        self.level_label_font[0] = 1
                    elif len(self.label_text) < self.level_label_font[2]:
                        self.level_label_font[0] = 1
                    elif len(self.label_text) < self.level_label_font[3]:
                        self.level_label_font[0] = 2
                    elif len(self.label_text) < self.level_label_font[4]:
                        self.level_label_font[0] = 3
                    elif len(self.label_text) < self.level_label_font[5]:
                        self.level_label_font[0] = 4
                    elif len(self.label_text) < self.level_label_font[6]:
                        self.level_label_font[0] = 5
            elif button_id == 19:
                self.m(self.label_text, 'mc')
            elif button_id == 20:
                self.m(self.label_text, 'm+')
            elif button_id == 21:
                self.m(self.label_text, 'm-')
            elif button_id == 22:
                self.m(self.label_text, 'mr')
            elif button_id == 23:
                self.check_add_s('(')
            elif button_id == 24:
                self.check_add_s(')')
            elif button_id == 25:
                self.check_add_s('√')
            elif button_id == 26:
                self.check_add_s('^(1/')
            elif button_id == 27:
                self.check_add_s('e')
            elif button_id == 28:
                self.check_add_s('p')
            elif button_id == 29:
                self.check_add_s('!')
            elif button_id == 30:
                self.check_add_s('^(-1)')
            elif button_id == 31:
                if self.label_text != '':
                    if self.label_text[0] == '-':
                        self.label_text = self.label_text[1:]
                    else:
                        self.label_text = '-{}'.format(self.label_text)
            elif button_id == 32:
                self.check_add_s('^')

    def result(self):
        try:
            t = self.label_text
            t = t.replace('e', '2.718281')
            t = t.replace('π', '3.141592')
            t = t.replace('^', '**')
            for i in range(0, self.label_text.count('√')):
                try:
                    a = t.replace('-', ' ')
                    a = a.replace('+', '     ')
                    a = a.replace('*', ' ')
                    a = a.replace('/', ' ')
                    a = a.replace('**', ' ')
                    b = math.sqrt(int(a.split('√')[1].split(' ')[0]))
                    t = t.replace('√{}'.format(a.split('√')[1].split(' ')[0]), str(b))
                except (IndexError, ValueError):
                    pass
            for i in range(0, self.label_text.count('!')):
                try:
                    a = math.factorial(int(self.label_text.split('!(')[1].split(')')[0]))
                    t = t.replace('!({})'.format(self.label_text.split('!(')[1].split(')')[0]), str(a))
                except Exception as e:
                    print(e)
            self.label_text = str(eval(t))
            self.label_text = self.p_label_text
        except Exception as e:
            print(e)
            self.p_label_text = 'ERROR'

    def p_result(self):
        try:
            t = self.label_text
            t = t.replace('e', '2.718281')
            t = t.replace('π', '3.141592')
            t = t.replace('^', '**')
            if t.count('(') != t.count(')'):
                for i in range(0, t.count('(')-t.count(')')):
                    t += ')'
            for i in range(0, self.label_text.count('√')):
                try:
                    a = t.replace('-', ' ')
                    a = a.replace('+', '     ')
                    a = a.replace('*', ' ')
                    a = a.replace('/', ' ')
                    a = a.replace('**', ' ')
                    b = math.sqrt(float(a.split('√')[1].split(' ')[0]))
                    t = t.replace('√{}'.format(a.split('√')[1].split(' ')[0]), str(b))
                except (IndexError, ValueError):
                    pass
            for i in range(0, self.label_text.count('!')):
                try:
                    a = math.factorial(int(t.split('!(')[1].split(')')[0]))
                    t = t.replace('!({})'.format(t.split('!(')[1].split(')')[0]), str(a))
                except (IndexError, ValueError):
                    pass
            self.p_label_text = str(eval(t))
            if len(self.p_label_text) > 50:
                self.p_label_text = 'ERROR'
                self.label_text = ' '
                self.level_label_font[0] = 1
            else:
                result = self.p_label_text.split('.')[0]
                result_l = []
                i_l = []
                a = 3
                for s in result:
                    result_l.append(s)
                for i1 in range(len(result_l) // 3):
                    i_l.append(a)
                    a = a + 4
                for i in i_l:
                    result_l.insert(len(result_l) - i, ' ')
                result = ''
                for s in result_l:
                    result = result + s
                if '.' in self.p_label_text:
                    if self.p_label_text.split('.')[1] == '0':
                        result = result.split('.')[0]
                    else:
                        result = result + '.' + self.p_label_text.split('.')[1]
                self.p_label_text = result.lstrip()
                if self.p_label_text == '()':
                    self.p_label_text = ''
        except (TypeError, SyntaxError, IndexError):
            pass

    def m(self, s, d):
            if d == 'm-':
                if self.label_text != '':
                    file = open('Memory.txt', 'w')
                    a = s
                    if '-' not in s:
                        a = '-' + s
                    file.write(a)
                    file.close()
            elif d == 'm+':
                if self.label_text != '':
                    sa = s
                    if '-' in s:
                        sa = s.split('-')[1]
                    file = open('Memory.txt', 'w')
                    file.write(sa)
                    file.close()
            elif d == 'mr':
                file = open('Memory.txt', 'r')
                num = file.readline()
                if len(num) == 0:
                    pass
                else:
                    self.label_text = str(num)
                file.close()
            elif d == 'mc':
                file = open('Memory.txt', 'w')
                file.write('')
                file.close()

    def main(self):
        print(str(self.horizontal) + 'x' + str(self.vertical))
        pygame.display.set_caption('калькулятор')
        while self.d:
            self.update_display()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.d = False
                elif event.type == MOUSEBUTTONUP:
                    self.back_color()
                    buton_id = self.Button.pressed(pygame.mouse.get_pos())
                    self.func(buton_id)
                elif event.type == MOUSEBUTTONDOWN:
                    buton_id = self.Button.pressed(pygame.mouse.get_pos())
                    self.visual_func(buton_id)


Window()
