import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Головне вікно - Текстовий редактор")
        self.create_menu()

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Новий", command=self.new_file)
        file_menu.add_command(label="Відкрити", command=self.open_file)
        file_menu.add_command(label="Зберегти", command=self.save_file)
        file_menu.add_command(label="Закрити", command=self.close_file)

        edit_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Правка", menu=edit_menu)
        edit_menu.add_command(label="Скасувати", command=self.undo)
        edit_menu.add_command(label="Вирізати", command=self.cut)
        edit_menu.add_command(label="Копіювати", command=self.copy)
        edit_menu.add_command(label="Вставити", command=self.paste)

        help_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Допомога", menu=help_menu)
        help_menu.add_command(label="Про програму", command=self.show_about)

    def new_file(self):
        new_window = tk.Toplevel(self.root)
        TextEditor(new_window)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            new_window = tk.Toplevel(self.root)
            editor = TextEditor(new_window)
            with open(file_path, 'r', encoding='utf-8') as file:
                editor.text.insert('1.0', file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.text.get('1.0', tk.END))

    def close_file(self):
        self.root.destroy()

    def undo(self):
        self.text.event_generate("<<Undo>>")

    def cut(self):
        self.text.event_generate("<<Cut>>")

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")

    def show_about(self):
        messagebox.showinfo("Про програму", "Простий текстовий редактор з багатовіконністю на Python.")

    def create_text_widget(self):
        self.text = tk.Text(self.root, undo=True)
        self.text.pack(fill=tk.BOTH, expand=1)
        scrollbar = tk.Scrollbar(self.text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)

root = tk.Tk()
app = TextEditor(root)
root.mainloop()
