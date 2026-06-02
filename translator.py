from tkinter import *
from tkinter import ttk, messagebox

translator_import_error = None
translator = None
try:
    from deep_translator import GoogleTranslator
except Exception as exc:
    translator_import_error = exc

# -------- Main Window --------
root = Tk()
root.title("Translator")
root.geometry("520x720")
root.config(bg="blue")

Label(root, text="Translator", font=("Times New Roman", 20, "bold"),
      bg="blue", fg="black").place(x=110, y=20, height=40, width=300)

# -------- Source Text --------
Text_src = Text(root, font=("Times New Roman", 14), wrap=WORD)
Text_src.place(x=10, y=80, height=220, width=500)

# -------- Language List --------
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-cn",
    "Chinese (Traditional)": "zh-tw",
    "Arabic": "ar",
    "Italian": "it",
    "Portuguese": "pt",
    "Turkish": "tr",
    "Dutch": "nl",
    "Greek": "el",
    "Thai": "th",
    "Vietnamese": "vi",
}

# -------- Dropdowns --------
Label(root, text="Source Language", font=("Times New Roman", 12),
      bg="blue", fg="black").place(x=10, y=290)
comb_src = ttk.Combobox(root, values=list(languages.keys()), state="readonly")
comb_src.place(x=10, y=320, height=40, width=240)
comb_src.set("English")

Label(root, text="Target Language", font=("Times New Roman", 12),
      bg="blue", fg="black").place(x=280, y=290)
comb_dest = ttk.Combobox(root, values=list(languages.keys()), state="readonly")
comb_dest.place(x=280, y=320, height=40, width=230)
comb_dest.set("Hindi")

# -------- Output --------
Label(root, text="Output", font=("Times New Roman", 14),
      bg="blue", fg="black").place(x=10, y=380)
Text_dst = Text(root, font=("Times New Roman", 14), wrap=WORD)
Text_dst.place(x=10, y=420, height=220, width=500)

translator = Translator()

# -------- Translate Function --------
def translate():
    if translator_import_error is not None:
        messagebox.showerror(
            "Translation Error",
            "Unable to load the translation library.\n"
            "Please ensure deep-translator is installed and try again.\n"
            f"Error details: {translator_import_error}"
        )
        return

    src_text = Text_src.get("1.0", END).strip()
    if not src_text:
        messagebox.showwarning("Warning", "Enter text to translate.")
        return

    src_lang = languages.get(comb_src.get(), "en")
    dest_lang = languages.get(comb_dest.get(), "en")

    try:
        result = GoogleTranslator(source=src_lang, target=dest_lang).translate(src_text)
        Text_dst.delete("1.0", END)
        Text_dst.insert(END, result)
    except Exception as exc:
        Text_dst.delete("1.0", END)
        Text_dst.insert(END, f"Translation failed:\n{exc}")

# -------- Button --------
Button(root, text="Translate", relief=RAISED, command=translate).place(x=200, y=660, height=40, width=120)

root.mainloop()
