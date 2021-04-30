import tkinter

window = tkinter.Tk()
window.title("AL Form Project 201010298 팽건우")
window.geometry("1080x720") #가로 * 세로

sort_label = tkinter.Label(window, 
                text="정렬방식:",
                font = ("Arial", "25", "italic")).pack(anchor='w')

def sort_select():
    sort_num = sort_var.get()
    if (sort_num == 1):
        sort_show.config(text="선택 정렬")
    elif (sort_num == 2):
        sort_show.config(text="버블 정렬")
    elif (sort_num == 3):
        sort_show.config(text="삽입 정렬")
    elif (sort_num == 4):
        sort_show.config(text="병합 정렬")
    else:
        sort_show.config(text="퀵 정렬")

sort_var = tkinter.IntVar()

selection_sort = tkinter.Radiobutton(window, text='선택 정렬', variable=sort_var, value=1, command=sort_select, font = ("Arial", "20", "italic")).pack(anchor='w')
bubble_sort = tkinter.Radiobutton(window, text='버블 정렬', variable=sort_var, value=2, command=sort_select, font = ("Arial", "20", "italic")).pack(anchor='w')
insert_sort = tkinter.Radiobutton(window, text='삽입 정렬', variable=sort_var, value=3, command=sort_select, font = ("Arial", "20", "italic")).pack(anchor='w')
merge_sort = tkinter.Radiobutton(window, text='병합 정렬', variable=sort_var, value=4, command=sort_select, font = ("Arial", "20", "italic")).pack(anchor='w')
quick_sort = tkinter.Radiobutton(window, text='퀵 정렬', variable=sort_var, value=5, command=sort_select, font = ("Arial", "20", "italic")).pack(anchor='w')



sort_show = tkinter.Label(window)
sort_show.pack(anchor='w')

window.mainloop()