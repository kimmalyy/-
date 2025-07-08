print("hello world")
a = 3
b = 156
c = 7
print(a*b+c)
print("my name is juwon. what is your name?")
import pygame
import sys

pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("게임 프론트엔드")

# 색 정의
BG_COLOR = (30, 30, 30)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER = (100, 160, 210)
TEXT_COLOR = (255, 255, 255)

# 폰트 설정
title_font = pygame.font.SysFont(None, 72)
button_font = pygame.font.SysFont(None, 48)

# 텍스트 렌더링
title_surf = title_font.render("시뮬레이션", True, TEXT_COLOR)
title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 4))

# 버튼들(rectangles)
buttons = {
    "start": {
        "rect": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 60),
        "text": "시작"
    },
    "desc": {
        "rect": pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 60),
        "text": "설명"
    }
}

def draw_buttons(mouse_pos):
    for info in buttons.values():
        rect = info["rect"]
        # hover 상태
        color = BUTTON_HOVER if rect.collidepoint(mouse_pos) else BUTTON_COLOR
        pygame.draw.rect(screen, color, rect)
        # 텍스트
        txt_s = button_font.render(info["text"], True, TEXT_COLOR)
        txt_r = txt_s.get_rect(center=rect.center)
        screen.blit(txt_s, txt_r)

def main():
    clock = pygame.time.Clock()

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                for key, info in buttons.items():
                    if info["rect"].collidepoint(ev.pos):
                        print(f"{info['text']} 버튼 클릭됨")

        # 화면 그리기
        screen.fill(BG_COLOR)
        screen.blit(title_surf, title_rect)
        draw_buttons(mouse_pos)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

