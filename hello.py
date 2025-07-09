print("hello world")
a = 3
b = 156
c = 7
print(a*b+c)
print("my name is juwon. what is your name?")
import pygame
import sys
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. 할일추가")
    print("2. 할일보기")
    print("3. 완료표시하기")
    print("4. 할일지우기")
    print("5. 나가기")
    print("번호를 입력하여 사용할 수 있습니다.")
print("안녕하세요. 저는 주원이라고 합니다.")

def add_task(tasks):
    task = input("할일을 쓰시오: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")
#사람이 자기 닉네임을 입력할 수 있게하는 코드

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("시뮬레이션")
def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "Completed" if task["완료됨"] else "완료되지 않았습니다"
            print(f"{idx}. {task['task']} - {status}")
nick_name = input("당신의 이름은 무엇인가요?")
print("안녕하세요", nick_name ,"님!")

# 색 정의
BG_COLOR = (30, 30, 30)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER = (100, 160, 210)
TEXT_COLOR = (255, 255, 255)
def mark_completed(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("완료처리할 할일의 번호를쓰십시오: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print(f"Task '{tasks[task_num - 1]['task']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("지울할일의 번호를 쓰십시오: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"할일 '{removed_task['task']}' (이)가 추가되었습니다.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    clock = pygame.time.Clock()

    tasks = []
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
        display_menu()
        choice = input("번호를 선택하십시오: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("To-Do List가 종료됩니다...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
print("쉬기,이름변경,3,4,5,중에")

cho = input("무엇을 하시겠습니까?")
print("네!", cho , "를 시작하겠습니다!")
if cho == '쉬기':
        print("네, 쉬기를 실행하겠습니다.")
        
elif cho == '이름변경':
        name = input("이름을 변경하시겠습니까? 네/아니오")
        if name == '네':
            na = input("이름을 입력하십시오")
            print("안녕하세요", na ,"님!")
        elif name == '아니오':
               print("네, 이름을 변경하지 않겠습니다. 여전히 당신의 이름은", nick_name , "입니다.")