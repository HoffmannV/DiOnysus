from views.main_window import create_main_window, draw_main_window

if __name__ == "__main__":
    root = create_main_window()
    draw_main_window(root)
    root.mainloop()
