import Tkinter as tk

def create_window():
        t = tk.Toplevel(root)
        t.wm_title("Window 1")
        l = tk.Label(t, text="This is window ")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

if __name__ == "__main__":
    root = tk.Tk()
   # root.pack(side="top", fill="both", expand=True)
    btn=tk.Button(root,text="New Window",command=create_window)
    btn.pack()
    root.mainloop()

