import tkinter as tk
from pathlib import Path
from tkinter import *
from tkinter import filedialog, ttk
from typing import List

from src.models.entities.exp_info import ExpInfo


class ExpInfoView(tk.Tk):
    def __init__(self, on_submit, exp_info: ExpInfo):
        super().__init__()
        self.blocks = exp_info.blocks
        self.title("Experiment Informations")
        self.geometry("300x350+750+200")
        self.configure(background="#dde")

        self.on_submit = on_submit  # callback para o controller

        # Labels e entradas
        tk.Label(self, text="Experiment:", background="#dde").place(
            x=0, y=10, width=100, height=20
        )

        tk.Label(self, text="Experimenter:", background="#dde").place(
            x=0, y=60, width=100, height=20
        )

        tk.Label(self, text="Participant:", background="#dde").place(
            x=0, y=110, width=100, height=20
        )
        tk.Label(self, text="Save path", background="#dde").place(
            x=0, y=160, width=100, height=20
        )

        self.entry_experiment = tk.Entry(self)
        self.entry_experiment.place(x=10, y=30, width=250, height=20)
        self.entry_experimenter = tk.Entry(self)
        self.entry_experimenter.place(x=10, y=80, width=250, height=20)
        self.entry_participant = tk.Entry(self)
        self.entry_participant.place(x=10, y=130, width=250, height=20)
        self.entry_path = tk.Entry(self)
        self.entry_path.place(x=10, y=180, width=200, height=20)
        self.btn_search = tk.Button(self, text="Search", command=self.select_file)
        self.btn_search.place(x=215, y=180)
        tk.Label(self, text="Block:", background="#dde").place(
            x=10, y=210, width=100, height=20
        )
        self.listbox = Listbox(self)
        self.listbox.place(x=10, y=210, width=200, height=80)
        self.insert_in_list_box(self.listbox)

        # Botão iniciar
        btn = ttk.Button(self, text="Start", command=self.submit)
        btn.place(x=10, y=300, width=100, height=30)

        self.bind("<Return>", lambda e: self.submit())

    def select_file(self):
        path_data = Path(__file__).parent.parent / "data/results/"

        path = filedialog.asksaveasfilename(
            title="Select experiment file",
            initialdir=path_data,
            filetypes=[("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*")],
        )

        if path:
            self.entry_path.delete(0, END)
            self.entry_path.insert(0, path)

    def insert_in_list_box(self, listbox: Listbox):

        for i in self.blocks:
            listbox.insert(END, i)

    def submit(self):
        """Coleta os dados e envia para o controller"""
        selected_block = self.listbox.curselection()
        block = None
        if selected_block:
            first_block = self.listbox.get(selected_block)
            experiment = self.entry_experiment.get().strip()
            experimenter = self.entry_experimenter.get().strip()
            participant = self.entry_participant.get().strip()
            block = selected_block[0]
            if not block:
                block = 0
            # print(block, selected_block)
            self.on_submit(
                {
                    "experiment": experiment,
                    "experimenter": experimenter,
                    "participant": participant,
                    "start_block": block,
                    "save_path": self.entry_path.get().strip(),
                }
            )

            self.destroy()
        else:
            print("No first block selected")
