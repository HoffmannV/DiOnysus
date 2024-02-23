from data_strucktures.min_heap import MinHeap
from views.main_window import create_main_window, draw_main_window

#if __name__ == "__main__":
#    root = create_main_window()
#    draw_main_window(root)
#    root.update()
#    root.minsize(root.winfo_width(), root.winfo_height())
#    root.mainloop()


heap = MinHeap(1)
heap.insert(2)
heap.insert(8)
heap.insert(4)
heap.insert(3)
heap.insert(9)
heap.insert(5)
