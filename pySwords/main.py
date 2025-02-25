import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class SwordSelectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Выбор меча")
        self.root.geometry("700x600")
        self.style = ttk.Style()
        self.style.configure("C.TButton", font=("Helvetica", 12), padding=10)
        self.style.configure("C.TLabel", font=("Helvetica", 14), background="#FFFFFF", padding=10, justify="center")
        self.root.configure(background="#FFFFFF")

        self.start_button = ttk.Button(root, text="Начать подбор", command=self.start_selection, style="C.TButton")
        self.start_button.pack(pady=50)
        self.action_frame = ttk.Frame(root)
        self.exit_button = ttk.Button(self.action_frame, text="Выход", command=self.exit_program, style="C.TButton")
        self.exit_button.pack(side="left", padx=50)
        self.repeat_button = ttk.Button(self.action_frame, text="Начать сначала", command=self.start_selection, style="C.TButton")
        self.repeat_button.pack(side="left", padx=50)
        self.help_button = ttk.Button(self.action_frame, text="Помощь", command=self.show_help, style="C.TButton")
        self.help_button.pack(side="left", padx=50)
        self.action_frame.pack(side="bottom", fill="x")
        self.current_selection = ""
        self.current_question = ""
        self.final_choice = ""
        self.image_label = tk.Label(self.root, bg="#FFFFFF")
        self.image_label.pack(pady=10)

    def show_sword_image(self, sword_name):
        """ Загружает и показывает изображение меча. """
        try:
            image_path = f"{sword_name}.jpg"  # Путь к картинке
            image = Image.open(image_path)
            image = image.resize((500, 400), Image.Resampling.LANCZOS)  # Меняем размер
            self.sword_photo = ImageTk.PhotoImage(image)  # Держим ссылку на изображение

            self.image_label.config(image=self.sword_photo)  # Устанавливаем изображение
            self.image_label.image = self.sword_photo  # ВАЖНО: сохраняем ссылку, чтобы не удалялось сборщиком мусора
            self.image_label.pack(pady=10)
        except Exception as e:
            self.image_label.config(image="", text="Изображение не найдено", font=("Helvetica", 12), fg="red")
            print(f"Ошибка загрузки изображения: {e}")  # Для отладки
    def start_selection(self):
        self.current_selection = ""
        self.current_question = "Выбор рода деятельности в которой вы планируете применять меч - очень важен для дальнейших рекомендаций."
        self.start_button.pack_forget()
        self.clean_window()
        self.ask_question("Для чего вам меч?", [("Для участия в турнире", self.tournament),
                                                ("Для тренировок", self.training),
                                                ("Для интерьера", self.interior)])

    def tournament(self):
        self.current_selection = "Меч для турнира"
        self.clean_window()
        self.ask_question("В какой номинации вы выступаете?", [("Одноручный меч", self.tournament_one_handed),
                                                               ("Полуторный меч", self.tournament_half_handed),
                                                               ("Двуручный меч", self.tournament_two_handed)])

    def tournament_half_handed(self):
        self.current_selection += ", номинация - полуторный меч"
        self.clean_window()
        self.show_result("Фламберг")

    def tournament_two_handed(self):
        self.current_selection += ", номинация - двуручный меч"
        self.clean_window()
        self.show_result("Эсток")

    def tournament_one_handed(self):
        self.current_selection += ", номинация - одноручный меч"
        self.clean_window()
        self.ask_question("Какой вид состязания?", [("Дуэль", self.tournament_one_handed_duel),
                                                    ("Бугурт", self.tournament_one_handed_bugurt)])

    def tournament_one_handed_duel(self):
        self.current_selection += ", состязание - дуэль"
        self.clean_window()
        self.show_result("Романский меч")

    def tournament_one_handed_bugurt(self):
        self.current_selection += ", состязание - бугурт"
        self.clean_window()
        self.show_result("Фальшион")

    def training(self):
        self.current_selection = "Меч для тренировки"
        self.clean_window()
        self.ask_question("В какой номинации вы тренируетесь?", [("Одноручный меч", self.training_one_handed),
                                                                 ("Полуторный меч", self.training_half_handed),
                                                                 ("Двуручный меч", self.training_two_handed)])

    def training_half_handed(self):
        self.current_selection += ", номинация - полуторный меч"
        self.clean_window()
        self.show_result("Федершверт")

    def training_two_handed(self):
        self.current_selection += ", номинация - двуручный меч"
        self.clean_window()
        self.show_result("Клеймор")

    def training_one_handed(self):
        self.current_selection += ", номинация - одноручный меч"
        self.clean_window()
        self.ask_question("Тренировка доспешная?", [("Да", self.training_one_handed_arm),
                                                    ("Нет", self.training_one_handed_noarm)])

    def training_one_handed_arm(self):
        self.current_selection += ", тренировка - доспешная"
        self.clean_window()
        self.show_result("Каролинг")

    def training_one_handed_noarm(self):
        self.current_selection += ", тренировка - бездоспешная"
        self.clean_window()
        self.show_result("Палаш")

    def interior(self):
        self.current_selection = "Меч для интерьера"
        self.clean_window()
        self.ask_question("Клинки какого времени вас интересуют?", [("Античность", self.interior_antiquity),
                                                                    ("Раннее средневековье", self.early_medieval),
                                                                    ("Позднее средневековье", self.late_medieval)])

    def interior_antiquity(self):
        self.current_selection += ", эпоха - античность"
        self.clean_window()
        self.show_result("Гладиус")

    def early_medieval(self):
        self.current_selection += ", эпоха - раннее средневековье"
        self.clean_window()
        self.ask_question("Какие регионы вам по душе?", [("Япония", self.early_medieval_region_Jap),
                                                         ("Скандинавия", self.early_medieval_region_Scan)])

    def early_medieval_region_Jap(self):
        self.current_selection += ", регион - Япония"
        self.clean_window()
        self.show_result("Катана")

    def early_medieval_region_Scan(self):
        self.current_selection += ", регион - Скандинавия"
        self.clean_window()
        self.show_result("Каролинг")

    def late_medieval(self):
        self.current_selection += ", эпоха - позднее средневековье"
        self.clean_window()
        self.ask_question("Какие регионы вам по душе?", [("Восток", self.late_medieval_region_West),
                                                         ("Европа", self.late_medieval_region_Europ)])

    def late_medieval_region_West(self):
        self.current_selection += ", регион - Восток"
        self.clean_window()
        self.show_result("Сабля Нимча")

    def late_medieval_region_Europ(self):
        self.current_selection += ", регион - Европа"
        self.clean_window()
        self.show_result("Цвайхендер")

    def show_result(self, sword_name):
        self.clean_window()
        self.final_choice = f" Исходя из всех раннее сделанных вами выборов, самым лучшим решением, будет выбрать меч вида: {sword_name}. Приятного использования. Не рубите с плеча!"
        self.question_label = ttk.Label(self.root, text=f"Вам подойдёт {sword_name}", style="C.TLabel")
        self.question_label.pack(pady=20)
        self.show_sword_image(sword_name)

    def ask_question(self, question, options):
        self.clean_window()
        self.current_question = question
        self.question_label = ttk.Label(self.root, text=question, style="C.TLabel")
        self.question_label.pack(pady=20)
        for text, command in options:
            button = ttk.Button(self.root, text=text, command=command, style="C.TButton")
            button.pack(pady=5)

    def clean_window(self):
        for widget in self.root.winfo_children():
            if widget != self.action_frame:
                widget.pack_forget()

    def show_help(self):
        help_text = self.final_choice if self.final_choice else self.current_question
        messagebox.showinfo("Помощь", f"Вы выбрали: {self.current_selection}.{help_text}")

    def exit_program(self):
        if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
            self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = SwordSelectionApp(root)
    root.mainloop()