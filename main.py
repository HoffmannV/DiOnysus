from views.main_window import create_main_window


if __name__ == "__main__":
    root = create_main_window()
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()
