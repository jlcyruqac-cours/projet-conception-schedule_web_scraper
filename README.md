# Projet d'application d'horaire de cours à l'UQAC
---

Ce projet permet un accès rapide à l'horaire de cours et des locaux des cours d'un étudiant

### Tips git  
Pour merger quand branche behind x commit :  
git fetch origin master  
git pull  

### Prérequis
---

LaTeX  
* Installation:   
  * Windows: Texlive ou Miktex ( nécessite ActivePerl )  
  * Linux: Texlive-full  
  * Éditeur: Visual Studio Code  
  * Extensions: LaTeX Workshop, Rewrap  

Python   
* Version: 3.7.5  
  * IDE: PyCharm
  * Éditeur de texte: Sublime Text, Visual Studio Code
  * Requirements: [requirements.txt](code/requirements.txt)  

### Installation
---

L'environnemennt de développement Python devrait être installé en suivant les étapes suivantes:

1. Cloner le projet: 
Via SSH:  
```
git git@github.com:jlcyruqac-cours/projet-conception-schedule_web_scraper.git  
```
Via HTTPS:  
```
https://github.com/jlcyruqac-cours/projet-conception-schedule_web_scraper.git  
```

2. Ce déplacer dans le dossier du projet: 

```
cd projet-conception-schedule_web_scraper/code/
```

3. Créer un environnement virtuel en utilisant virtualenv (qui peut être installé à l'aide de pip): 

- Windows:  
```
python -m venv venv
```
- Linux/MacOs:  

```
python3 -m venv venv
```

4. Activer la venv: 

- Windows:
```
./venv/Scripts/activate
```

- Linux/MacOS:  
```
source venv/bin/activate
```

5. Installer les requirements: 

```
pip install -r requirements.txt
```

Désactivte l'environnement virtuel

```
deactivate
```

## Déploiement
---

À venir...

## Construit avec
---

* [Flask](https://palletsprojects.com/p/flask/) - Framework web utilisé
* [Bootstrap](https://getbootstrap.com) - Frontend, CSS
* [jQuery](https://jquery.com/) - Framework JS utilisé


## Auteurs
---

* **Alissa Bonnel** - *Membre de l'équipe* - [alissalicorne](https://github.com/alissalicorne)
* **Jean-Sébastien St-Pierre** - *Membre de l'équipe* - [alchimyk](https://github.com/alchimyk)
* **Alexis Valotaire** - *Membre de l'équipe* - [Alexis_Valotaire](https://github.com/AlexisCode101)
