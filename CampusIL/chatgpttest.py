import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

# Dictionary containing evidence for evolution by field with expanded explanations
evolution_evidence = {
    "Biology": [
        {
            "title": "DNA similarities between species",
            "details": """DNA, the molecule that carries genetic information, is remarkably similar across different species. For example, humans share about 98% of their DNA with chimpanzees. This level of similarity suggests a common ancestor, which is a cornerstone of evolutionary theory.

Biblical creation, such as the story of Adam and Eve, suggests that humans were created separately from animals. However, the overwhelming genetic similarity between humans and other species indicates that life is interconnected through shared ancestry, contradicting the idea that humans are uniquely separate from other life forms.

Consider the similarity of the hemoglobin protein in humans and chimpanzees. It's nearly identical, down to the sequence of amino acids. This level of detail in genetic similarity is hard to explain if all life was created independently and perfectly, as suggested by the Bible.

For more information, see this [article on genetic similarities](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1698473/).""",
            "image": "dna_similarity.jpg",
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1698473/"]
        },
        {
            "title": "Natural selection in bacteria",
            "details": """Natural selection is not just a theory but something we can observe directly, especially in microorganisms like bacteria. For example, bacteria have evolved resistance to antibiotics, a phenomenon that has been documented extensively in scientific studies.

When antibiotics are used, they kill most bacteria, but some may survive due to random mutations. These survivors reproduce, passing the resistant trait to the next generation. Over time, the population of bacteria becomes predominantly resistant to the antibiotic, demonstrating evolution in action.

This observable process of adaptation and evolution in bacteria challenges the biblical narrative that all life forms were created perfectly and do not change. The Bible's account does not account for such ongoing, observable changes in species.

Read more about this [study on antibiotic resistance](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4378521/).""",
            "image": "bacteria.jpg",
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4378521/"]
        }
    ],
    "Anatomy": [
        {
            "title": "Vestigial structures",
            "details": """Vestigial structures are parts of the body that have lost their original function through evolution. The human appendix is one example; it’s a small, tube-like structure attached to the large intestine, and in our ancestors, it was used to digest cellulose from plant material. Today, it serves no critical function and can even cause health issues like appendicitis.

The presence of vestigial structures is hard to explain under the creationist view that humans were designed perfectly by God. Why would a perfect creation include redundant or even potentially harmful parts? Evolutionary theory provides a clear explanation: these structures are leftovers from our ancestors, who had different dietary needs.

Consider the tailbone, or coccyx, in humans. It’s a remnant of a tail that was useful to our primate ancestors. In a creationist view, there's no reason for humans to have a tailbone if we were created in our current form. Evolution, however, explains this as a vestige of our evolutionary history.

For more information, see this [article on vestigial structures](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3006708/).""",
            "image": "vestigial_structures.jpg",
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3006708/"]
        },
        {
            "title": "Homologous structures",
            "details": """Homologous structures are body parts that are similar in structure but different in function, indicating a common ancestry. The limbs of humans, whales, and bats are a classic example. All these limbs have the same basic bone structure, but they are adapted to different uses: walking, swimming, and flying, respectively.

This structural similarity despite different functions supports the theory that these species evolved from a common ancestor. It contradicts the biblical notion that each species was created separately and uniquely.

If all creatures were designed perfectly by a creator, we would expect to see unique designs tailored to each species' needs. However, the fact that such diverse animals share a similar bone structure suggests they are all variations on a common theme, refined by millions of years of evolution.

For more information, see this [article on homologous structures](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1689594/).""",
            "image": "homologous_structures.jpg",
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1689594/"]
        }
    ],
    "Archeology": [
        {
            "title": "Fossil evidence of transitional species",
            "details": """The fossil record is one of the most compelling pieces of evidence for evolution. Transitional fossils, like the Archaeopteryx, show characteristics of both dinosaurs and birds, indicating a transition from one major group to another.

According to the Bible, all species were created in their present form. However, fossils of transitional species demonstrate gradual changes over time, suggesting a slow process of evolution rather than instant creation.

The Archaeopteryx, for example, has features of both reptiles (like teeth and a long bony tail) and birds (like feathers and wings), showing a clear evolutionary link. This directly contradicts the creationist view that birds and reptiles were created as separate, distinct groups.

For more information, see this [article on Archaeopteryx](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3146471/).""",
            "image": "archaeopteryx.jpg",
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3146471/"]
        },
        {
            "title": "Artifacts and early human remains",
            "details": """Archeological findings of early human fossils, such as Homo habilis, show a gradual progression from earlier hominids to modern humans. These fossils provide physical evidence of the evolution of humans over millions of years.

The Bible’s creation story, which depicts humans as being created in their current form, does not account for the vast array of hominid fossils showing a gradual transition from ape-like ancestors to Homo sapiens.

For example, Homo habilis, an early human species, had a smaller brain and larger teeth compared to modern humans, but it shows clear advancements over earlier hominids. This gradual development challenges the notion of an instant creation of humans as described in the Bible.

For more information, see this [article on early human fossils](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1852147/).""",
            "image": "early_humans.jpg",
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1852147/"]
        }
    ],
    "Genetics": [
        {
            "title": "Mutations as a source of variation",
            "details": """Mutations are changes in the DNA sequence that can introduce new traits into a population. While some mutations can be harmful, others can be beneficial and may help organisms adapt to their environment. Over time, these beneficial mutations can spread through a population, leading to evolutionary changes.

In contrast, the Bible suggests that all species were created in a perfect, unchanging form. The concept of mutations introducing variation and driving evolution directly contradicts the idea of a static creation.

An example of beneficial mutations is lactose tolerance in humans. Originally, most humans could not digest lactose, the sugar in milk, after childhood. However, a mutation that allowed some adults to digest lactose became more common in populations where dairy farming was prevalent, showing how mutations can lead to new traits that spread through natural selection.

For more information, see this [article on mutations and evolution](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1208690/).""",
            "image": "mutations.jpg",
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1208690/"]
        },
        {
            "title": "Chromosomal similarities",
            "details": """Humans have 23 pairs of chromosomes, while chimpanzees have 24. The difference is due to the fusion of two chromosomes in the human lineage. This fused chromosome in humans is directly comparable to two separate chromosomes in chimpanzees, providing strong evidence of our shared ancestry.

The Bible suggests humans were created separately from animals, but this chromosomal evidence clearly shows that humans share a common ancestor with other primates, contradicting the biblical account.

For more information, see this [article on chromosomal similarities](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1283085/).""",
            "image": "chromosome.jpg",
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1283085/"]
        }
    ],
    "Paleontology": [
        {
            "title": "Fossil record",
            "details": """The fossil record shows a progression of life forms from simple to more complex over millions of years. The gradual changes in fossils found in different geological layers support the theory of evolution by showing how species have changed over time.

The Bible’s account of creation suggests that all life was created in its current form. However, the fossil record provides clear evidence that life has evolved gradually, with older layers of rock containing simpler organisms and more recent layers containing more complex life forms.

For example, the evolution of the horse is well-documented in the fossil record, showing a gradual transition from a small, multi-toed ancestor to the large, single-toed horse we know today. This slow, step-by-step process contradicts the idea of a sudden creation of species as described in the Bible.

For more information, see this [article on the fossil record](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817382/).""",
            "image": "fossil_record.jpg",
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817382/"]
        },
        {
            "title": "Extinction events",
            "details": """The history of life on Earth is marked by several mass extinction events, where a significant portion of species died out. These events, such as the extinction of the dinosaurs, paved the way for the evolution of new species that adapted to the changed environment.

The Bible suggests that species were created perfectly and have remained unchanged. However, extinction events followed by the rise of new species show that life on Earth has been in a constant state of flux, driven by evolutionary processes.

For example, after the extinction of the dinosaurs, mammals became the dominant land animals, eventually leading to the rise of humans. This turnover in species challenges the idea of a static creation and supports the theory of evolution.

For more information, see this [article on extinction events](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4844565/).""",
            "image": "extinction_events.jpg",
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4844565/"]
        }
    ]
}

# Function to open links in a web browser
def open_link(url):
    webbrowser.open_new(url)

# Function to display expanded evidence details
def display_details(details, image_path, sources=None):
    detail_window = tk.Toplevel(root)
    detail_window.title("Expanded Explanation")
    
    # Displaying the image
    img = Image.open(image_path)
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(detail_window, image=img)
    img_label.image = img
    img_label.pack(pady=10)

    # Displaying the detailed explanation
    details_label = tk.Label(detail_window, text=details, wraplength=500, justify="left", font=("Arial", 12))
    details_label.pack(pady=10)
    
    # Displaying sources as clickable links if available
    if sources:
        for source in sources:
            source_label = tk.Label(detail_window, text=source, fg="blue", cursor="hand2", font=("Arial", 10, "underline"))
            source_label.pack(pady=5)
            source_label.bind("<Button-1>", lambda e, url=source: open_link(url))

    close_button = ttk.Button(detail_window, text="Close", command=detail_window.destroy)
    close_button.pack(pady=10)

# Function to display the evidence list for the selected field
def display_evidence(field):
    field_evidence = evolution_evidence[field]
    evidence_window = tk.Toplevel(root)
    evidence_window.title(f"Evidence in {field}")
    
    for evidence in field_evidence:
        evidence_frame = tk.Frame(evidence_window)
        evidence_frame.pack(fill="x", pady=10)

        title_label = tk.Label(evidence_frame, text=evidence["title"], font=("Arial", 14, "bold"))
        title_label.pack(anchor="w")

        brief_button = ttk.Button(evidence_frame, text="Expand", 
                                  command=lambda e=evidence: display_details(e["details"], e["image"], e.get("sources")))
        brief_button.pack(anchor="e")

# Function to display the fields of evidence
def display_fields():
    for field in evolution_evidence.keys():
        field_button = ttk.Button(root, text=field, command=lambda f=field: display_evidence(f))
        field_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Evolution Evidence")
root.geometry("600x400")

title_label = tk.Label(root, text="Explore Evidence for Evolution", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

description_label = tk.Label(root, text="Select a field to explore the evidence that supports evolution, "
                                         "including detailed explanations, images, and sources.", wraplength=550, justify="center", font=("Arial", 12))
description_label.pack(pady=10)

display_fields()

root.mainloop()
