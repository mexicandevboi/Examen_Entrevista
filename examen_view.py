import tkinter as tk

from examen_controller import get_albums, search_albums, get_random_albums

def display_albums(albums):
    for album in albums:
        content = album['Album'] + ' - ' + album['Artista'] + '- Nominado: ' + str(album['Nominado']) + ' - Visitado: '+ str(album['Visitado'])+ '\n'
        text.insert(tk.END, content)

def show_albums():
    display_albums(get_albums())

def search():
    search_text = search_entry.get()
    results = search_albums(search_query=search_text)
    text.delete(1.0, tk.END)
    display_albums(results)

def show_random_albums():
    random_albums = get_random_albums()
    display_albums(random_albums)

window = tk.Tk()
window.title("Examen Entrevista")
window.geometry("800x600")

text = tk.Text(window)
text.pack()

button = tk.Button(window, text="Read File", command=show_albums)
button.pack()


search_entry = tk.Entry(window)
search_entry.insert(0, "Enter search query")
search_entry.pack(pady=10)
search_button = tk.Button(window, text="Search", command=search)
search_button.pack()


clear_button = tk.Button(window, text="Clear", command=lambda: text.delete(1.0, tk.END))
clear_button.pack()

random_button = tk.Button(window, text="Random Albums", command=show_random_albums)
random_button.pack()

window.mainloop()
