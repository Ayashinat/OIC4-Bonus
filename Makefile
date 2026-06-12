# ************************************************************** #
#           *Application Streamlit autour du nombre Pi           #
#                                                                #
# Nom     : OIC Streamlit 4.3                                    #
# Fichier : Makefile                                             #
# Rôle    : Gérer l'installation et le lancement de l'app        #
# Auteurs : Wewe Maitre 24001170 et Sylvain Maitre 24002886      #
# Version : v2.1 du 03-06-2026                                   #
# Licence : CC-BY-SA                                             #
# Cours   : L1 OIC - 4.3 Streamlit Pi                            #
#                                                                #
# Utilisation : make [cible]                                     #
# Cibles possibles :                                             #
#      all, bienvenue, install, run, distclean, help             #
#                                                                #
# ************************************************************** #

.ONESHELL:

VENV   = venv
PIP    = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python
STREAM = $(VENV)/bin/streamlit

all: bienvenue install pi run

bienvenue:
	@echo "Bienvenue dans le fantastique projet Streamlit PI de Wewe et Sylvain !"

$(VENV)/bin/activate:
	python3 -m venv $(VENV)

pi:
	@echo "Génération du fichier de décimales de pi"
	@$(PYTHON) genere_pi.py

install: $(VENV)/bin/activate
	@echo "Installation des dépendances"
	@$(PIP) install -r requirements.txt

run:
	@echo "Lancement de l'application avec Streamlit."
	@$(STREAM) run app.py

distclean:
	@echo "Nettoyage de l'environnement virtuel et des fichiers générés"
	@rm -rf $(VENV)
	@echo "Done."

help:
	@echo "Usage:"
	@echo "  make all        - Installation et lancement de l'application"
	@echo "  make bienvenue  - Affiche un message de bienvenue"
	@echo "  make install    - Installe les dépendances dans un environnement virtuel"
	@echo "  make run        - Lance l'application Streamlit"
	@echo "  make distclean  - Supprime l'environnement virtuel et nettoie les fichiers générés"
	@echo "  make help       - Affiche ce message d'aide"

.PHONY: all bienvenue install pi run distclean help
