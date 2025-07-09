import tkinter as tk
from tkinter import simpledialog, messagebox

messagebox.showinfo("안녕하세요. 저는 주원이라고 합니다.")

def start_program():
    # 이름 입력
    nick_name = simpledialog.askstring("이름입력", "당신의 이름은 무엇인가요?")
    if not nick_name:
        return  
    # 취소하면 종료

    messagebox.showinfo("환영합니다!", f"안녕하세요, {nick_name}님!")

    # 메뉴 선택
    choice = simpledialog.askstring(
        "메뉴 선택",
        "무엇을 하시겠습니까?\n(쉬기, 이름변경, 주원에게 말걸기, 4, 5 중에서 입력)"
    )
    
    if choice == "쉬기":
        messagebox.showinfo("쉬기", "네, 쉬기를 실행하겠습니다.")
    
    elif choice == "이름변경":
        confirm = simpledialog.askstring("확인", "이름을 변경하시겠습니까? (네/아니오)")
        if confirm == "네":
            new_name = simpledialog.askstring("새 이름", "새 이름을 입력하세요:")
            if new_name:
                messagebox.showinfo("이름 변경 완료", f"안녕하세요, {new_name}님!")
        elif confirm == "아니오":
            messagebox.showinfo("이름 유지", f"이름을 변경하지 않겠습니다. 여전히 {nick_name}님입니다.")
            return
        
        else:
            messagebox.showerror("입력 오류", "네 또는 아니오로 입력해주세요.")
            confirm = simpledialog.askstring("확인", "이름을 변경하시겠습니까? (네/아니오)")
    if choice == '주원에게 말걸기':
        messagebox.showinfo("점검중", "이 기능은 아직 준비중 입니다.")
        choice = simpledialog.askstring(
        "메뉴 선택",
        "무엇을 하시겠습니까?\n(쉬기, 이름변경, 주원에게 말걸기, 4, 5 중에서 입력)"
    )

    elif choice in [ "4", "5"]:
        messagebox.showinfo("준비 중", f"기능 {choice}은 아직 준비 중입니다.")
    else:
        messagebox.showerror("잘못된 입력", "알 수 없는 선택입니다.")

# GUI 창 시작
root = tk.Tk()
root.withdraw()  # 기본 tkinter 창 숨기기
start_program()