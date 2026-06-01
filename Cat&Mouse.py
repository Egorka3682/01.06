import tkinter as tk

window = tk.Tk()
window.title("Кошки - мышки")
window.geometry("900x900")
window.maxsize(900, 900)

c = tk.Canvas(window, width=900, height=900, bg="limegreen")
c.pack(fill="both", expand=True)
c.focus_set()

cat = tk.PhotoImage(file="vecteezy_ai-generated-shorthair-cat-on-transparent-background-png-image_34925406.png").subsample(30, 30)
mouse = tk.PhotoImage(file="vecteezy_mouse-isolated-on-transparent-background-generative-ai_48475023.png").subsample(30, 30)

id_cat = c.create_image(100, 100, image=cat, anchor="center")
id_mouse = c.create_image(800, 700, image=mouse, anchor="center")

w = a = s = d = False
up = down = left = right = False

game_over = False


def press(e):
    global w, a, s, d, up, down, left, right
    if e.keysym == "w": w = True
    if e.keysym == "a": a = True
    if e.keysym == "s": s = True
    if e.keysym == "d": d = True
    if e.keysym == "Up": up = True
    if e.keysym == "Down": down = True
    if e.keysym == "Left": left = True
    if e.keysym == "Right": right = True


def release(e):
    global w, a, s, d, up, down, left, right
    if e.keysym == "w": w = False
    if e.keysym == "a": a = False
    if e.keysym == "s": s = False
    if e.keysym == "d": d = False
    if e.keysym == "Up": up = False
    if e.keysym == "Down": down = False
    if e.keysym == "Left": left = False
    if e.keysym == "Right": right = False


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def move_bounded(obj_id, dx, dy):
    # bbox() даёт границы объекта на canvas: x1,y1,x2,y2
    x1, y1, x2, y2 = c.bbox(obj_id)
    w_obj = x2 - x1
    h_obj = y2 - y1

    x, y = c.coords(obj_id)  # центр (anchor="center")
    cw, ch = c.winfo_width(), c.winfo_height()

    half_w = w_obj / 2
    half_h = h_obj / 2

    new_x = clamp(x + dx, half_w, cw - half_w)
    new_y = clamp(y + dy, half_h, ch - half_h)

    c.coords(obj_id, new_x, new_y)


def collide(cat_id, mouse_id):
    # берём прямоугольник кота и смотрим, кто его пересекает
    x1, y1, x2, y2 = c.bbox(cat_id)
    return mouse_id in c.find_overlapping(x1, y1, x2, y2)


def loop():
    global game_over
    if game_over:
        return

    dx_cat = (-5 if a else 0) + (5 if d else 0)
    dy_cat = (-5 if w else 0) + (5 if s else 0)

    dx_mouse = (-5 if left else 0) + (5 if right else 0)
    dy_mouse = (-5 if up else 0) + (5 if down else 0)

    if dx_cat or dy_cat:
        move_bounded(id_cat, dx_cat, dy_cat)
    if dx_mouse or dy_mouse:
        move_bounded(id_mouse, dx_mouse, dy_mouse)

    if collide(id_cat, id_mouse):
        game_over = True
        cw, ch = c.winfo_width(), c.winfo_height()
        c.create_text(cw/2, ch/2, text="Игра окончена", font=("Arial", 48, "bold"))
        return

    window.after(20, loop)


c.bind("<KeyPress>", press)
c.bind("<KeyRelease>", release)

loop()
window.mainloop()