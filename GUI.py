import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import os
from SHA256.SecureHashingAlgorithm import sha_256

root = tk.Tk()
root.title("File Integrity Checker")

def sha256_file(path):
    with open(path, "rb") as f:
        data = f.read()
    return sha_256(data).hex()  

def create_manifest():
    folder = filedialog.askdirectory(title="Select folder")
    if not folder:
        return

    save_path = filedialog.asksaveasfilename(
        title="Save manifest",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if not save_path:
        return

    output_text.delete("1.0", tk.END)

    with open(save_path, "w", encoding="utf-8") as m:
        for root_dir, dirs, files in os.walk(folder):
            for file in files:
                if file == os.path.basename(save_path):
                    continue
                path = os.path.join(root_dir, file)
                file_hash = sha256_file(path)
                if not file_hash:
                    continue
                rel_path = os.path.relpath(path, folder)
                line = f"{file_hash}  {rel_path}\n"
                m.write(line)
                output_text.insert(tk.END, line)

    messagebox.showinfo("Success", "Manifest created")

def verify_manifest():
    manifest = filedialog.askopenfilename(
        title="Select manifest",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        initialdir=os.path.expanduser("~/Desktop")
    )
    if not manifest:
        return

    folder = filedialog.askdirectory(
        title="Select base folder for files",
        initialdir=os.path.dirname(manifest)
    )
    if not folder:
        return

    output_text.delete("1.0", tk.END)

    with open(manifest, "r", encoding="utf-8") as m:
        for line in m:
            saved_hash, rel_path = line.strip().split(maxsplit=1)
            path = os.path.join(folder, rel_path)
            if not os.path.exists(path):
                result = f"[MISSING] {rel_path}\n"
            else:
                current_hash = sha256_file(path)
                result = "[OK] " if current_hash == saved_hash else "[TAMPERED] "
                result += rel_path + "\n"
            output_text.insert(tk.END, result)

tk.Label(root, text="File Integrity Checker", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Create Manifest", command=create_manifest, width=25).pack(pady=5)
tk.Button(root, text="Verify Manifest", command=verify_manifest, width=25).pack(pady=5)

output_text = scrolledtext.ScrolledText(root, width=80, height=25)
output_text.pack(pady=10)

root.mainloop()