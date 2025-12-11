import csv
import os
import re

from PyQt6.QtWidgets import *
from GUI import *


class Logic(QMainWindow, Ui_Voting_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submit_button.clicked.connect(lambda : self.vote())

    #saves vote into a databace and checks if vote is valid
    def vote(self):
        try:
            # checks if id is corect
            id = self.id_text.text().strip()
            best = 'none'
            worst = 'none'

            match_id = False
            vote_exists = os.path.isfile("vote.csv")


            with open('id.csv', 'r') as ID_R:
                reader = csv.reader(ID_R)
                for line in reader:

                    if line and id == line[0].strip():
                        match_id = True
                        break

            if not match_id:
                self.invaled_text.setText("invaled ID")
                return



            # best checks
            if self.Tiffany_best.isChecked():
                best = 'tiffany'
            elif self.grabbit_best.isChecked():
                best = 'grabbit'
            elif self.rattles_best.isChecked():
                best = 'rattles'
            elif self.froggert_best.isChecked():
                best = 'froggert'
            elif self.adonis_best.isChecked():
                best = 'adonis'
            elif self.selene_best.isChecked():
                best = 'selene'
            elif self.madam_best.isChecked():
                best = 'madam mowzee'

            # worst checks
            if self.tiffany_worst.isChecked():
                worst = 'tiffany'
            elif self.grabbit_worst.isChecked():
                worst = 'grabbit'
            elif self.rattles_worst.isChecked():
                worst = 'rattles'
            elif self.froggert_worst.isChecked():
                worst = 'froggert'
            elif self.adonis_worst.isChecked():
                worst = 'adonis'
            elif self.selene_worst.isChecked():
                worst = 'selene'
            elif self.madam_worst.isChecked():
                worst = 'madam mowzee'

            if best == 'none' or worst == 'none':
                self.invaled_text.setText("please pick a vote in the best and worst categories")
                return

            if best == worst:
                self.invaled_text.setText("votes can not be the same")
                return

            #submits votes
            with open('vote.csv', "a", newline="") as Vote_W:
                writer = csv.writer(Vote_W)
                if not vote_exists:
                    writer.writerow(["id", "best", "worst"])
                writer.writerow([id, best, worst])

            self.invaled_text.setText("vote submitted")

        except Exception as e:
            self.invaled_text.setText(f"Error: {e}")

        #clears out everything
        self.id_text.clear()
        self.Tiffany_best.setChecked(False)
        self.grabbit_best.setChecked(False)
        self.rattles_best.setChecked(False)
        self.froggert_best.setChecked(False)
        self.adonis_best.setChecked(False)
        self.selene_best.setChecked(False)
        self.madam_best.setChecked(False)
        self.tiffany_worst.setChecked(False)
        self.grabbit_worst.setChecked(False)
        self.rattles_worst.setChecked(False)
        self.froggert_worst.setChecked(False)
        self.adonis_worst.setChecked(False)
        self.selene_worst.setChecked(False)
        self.madam_worst.setChecked(False)
