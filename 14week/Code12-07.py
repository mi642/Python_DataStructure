from tkinter import*

window = Tk()
window.geometry("600x600")
photo = PhotoImage(file = 'pet01.gif')

photoAry = []
h = photo.height()
w = photo.width()

for i in range(h):
    for k in range(w):
        r, g, b = photo.get(i, k)
        value = (r + g + b) // 3
        photoAry.append(value)

paper = Label(window, image = photo)
paper.pack(expand = 1, anchor = CENTER)
window.mainloop()