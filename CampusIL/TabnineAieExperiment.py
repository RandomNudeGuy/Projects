import tkinter as tk
from PIL import ImageTk, Image
import webbrowser

# Function to display evidence in a new window
def display_evidence(field):
    evidence_window = tk.Toplevel()
    evidence_window.title(f"Evidence for {field}")
    evidence_text = tk.Text(evidence_window, height=20, width=80)

    # Add evidence for each field here
    if field == "Genetics":
        evidence_text.insert(tk.END, "Genetic evidence for evolution includes the study of DNA, gene flow, and genetic variation.")
        evidence_text.insert(tk.END, "\n\nPhotos demonstrating genetic variation:")
        display_photo(evidence_text, "genetics_photo.jpg")
        display_photo(evidence_text, "genetics_photo2.jpg")
        display_photo(evidence_text, "genetics_photo3.jpg")
        evidence_text.insert(tk.END, "\n\nExamples of studies:")
        evidence_text.insert(tk.END, "\n- Haldane (1927): The role of genetic variation in evolution")
        evidence_text.insert(tk.END, "\n- Wright (1931): Evolution and the genetical theory of natural selection")
        evidence_text.insert(tk.END, "\n- Darwin (1859): On the Origin of Species by Means of Natural Selection")
        evidence_text.insert(tk.END, "\n- Fisher (1930): The Genetical Basis of Evolution")
        evidence_text.insert(tk.END, "\n\nSources:")
        evidence_text.insert(tk.END, "\n- https://www.britannica.com/science/Genetic-Variation")
        evidence_text.insert(tk.END, "\n- https://www.nature.com/articles/cr0274-0060")
        evidence_text.insert(tk.END, "\n- https://www.biography.com/scientist/charles-darwin")
        evidence_text.insert(tk.END, "\n- https://www.biography.com/scientist/james-wright")
    # Add more evidence for other fields here...

    # Add expand button
    expand_button = tk.Button(evidence_window, text="Expand", command=lambda: expand_evidence(evidence_text, field))
    expand_button.pack()

    evidence_text.pack()

# Function to expand evidence
def expand_evidence(text, field):
    if field == "Genetics":
        # Additional expansion options for Genetics field here...
        pass
    # Add more expansion options for other fields here...

# Function to display a photo in the evidence text
def display_photo(text, photo_path):
    image = Image.open(photo_path)
    resized_image = image.resize((200, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    text.image_create(tk.END, image=photo)

# Main application window
root = tk.Tk()
root.title("Evolution Facts")

# List of fields
fields = ["Genetics", "Morphology", "Behavior", "Paleontology", "Fossils"]

# Create a listbox to display fields
field_listbox = tk.Listbox(root, height=len(fields))
for field in fields:
    field_listbox.insert(tk.END, field)
field_listbox.pack(pady=10)

# Button to display evidence
display_button = tk.Button(root, text="Display Evidence", command=lambda: display_evidence(field_listbox.get(field_listbox.curselection())))
display_button.pack()

root.mainloop()