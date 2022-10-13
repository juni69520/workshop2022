import tkinter as tk
from unittest import result
from tkinter import messagebox


class Modal():
    def modalYesNo(self):
        result = messagebox.askyesno(
            title='Détecteur d\'émotion Teams',
            message='Accepter vous le traitement de capture photo ?',
            detail='Appuyez sur non pour quitter.'
        )

        if not result:
            exit()