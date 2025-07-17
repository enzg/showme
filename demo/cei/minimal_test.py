#!/usr/bin/env python3
"""Minimal test to identify display issue."""

import tkinter as tk
from tkinter import ttk

def test_display_issue():
    root = tk.Tk()
    root.title("Minimal Display Test")
    
    # Test both tk.Entry and ttk.Entry
    print("Creating display widgets...")
    
    # Frame
    frame = ttk.Frame(root, padding="10")
    frame.pack(fill='both', expand=True)
    
    # Test 1: tk.Entry with StringVar
    var1 = tk.StringVar(value="")
    label1 = tk.Label(frame, text="tk.Entry:")
    label1.grid(row=0, column=0, sticky='w')
    entry1 = tk.Entry(frame, textvariable=var1, state='readonly', width=30)
    entry1.grid(row=0, column=1, padx=5)
    
    # Test 2: Direct text insertion
    label2 = tk.Label(frame, text="Direct Entry:")
    label2.grid(row=1, column=0, sticky='w', pady=5)
    entry2 = tk.Entry(frame, width=30)
    entry2.grid(row=1, column=1, padx=5, pady=5)
    
    # Buttons to test
    def update_displays(text):
        # Update StringVar
        current = var1.get()
        var1.set(current + text)
        
        # Update direct entry
        entry2.insert('end', text)
        
        print(f"StringVar value: '{var1.get()}'")
        print(f"Direct entry: '{entry2.get()}'")
        
        # Force updates
        entry1.update()
        entry2.update()
        root.update_idletasks()
    
    # Button frame
    btn_frame = tk.Frame(frame)
    btn_frame.grid(row=2, column=0, columnspan=2, pady=10)
    
    for i in range(1, 4):
        btn = tk.Button(btn_frame, text=str(i), 
                       command=lambda x=str(i): update_displays(x),
                       width=5, height=2)
        btn.pack(side='left', padx=2)
    
    # Clear button
    def clear_all():
        var1.set("")
        entry2.delete(0, 'end')
        print("Cleared all")
    
    clear_btn = tk.Button(btn_frame, text="Clear", command=clear_all,
                         width=5, height=2, bg='red', fg='black')
    clear_btn.pack(side='left', padx=10)
    
    print("Test started. Click buttons to test display updates.")
    print("-" * 50)
    
    root.mainloop()

if __name__ == "__main__":
    test_display_issue()