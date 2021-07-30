# MOOC-Workbench ![mooc-wb](/medias/images/mooc-workbench.png)

Il ne s'agit pas d'un tuto sur FreeCAD, mais d'un cours sur la modélisation 3D. FreeCAD n'est
ici qu'un outil support du propos. L'intérêt porté par l'apprenant pour le sujet ou l'amusement
qu'il procure, doit être le moteur de découverte de FreeCAD.

Cet atelier FreeCAD vous suivra tous le long de ce mooc pour vous guider dans l'apprentissage de la modélisation 3D avec FreeCAD. Il permet d'afficher les tutoriels interactif et d'évaluer votre travail.

## Sommaire
*  ### [Installation](https://framagit.org/freecad-france/mooc-workbench#installation)
    * [Avec l'addon manager](https://framagit.org/freecad-france/mooc-workbench#installation-avec-laddon-manager)
    * [Manuellement](https://framagit.org/freecad-france/mooc-workbench#installation-manuelle)
*  ### [Utilisation](https://framagit.org/freecad-france/mooc-workbench#utilisation)
    * [Tutoriels](https://framagit.org/freecad-france/mooc-workbench#mooc-player)
    * [Évaluation](https://framagit.org/freecad-france/mooc-workbench#mooc-grader)

## Installation

### Installation avec l'addon manager

1. Démarrer FreeCAD.
2. Aller dans le menu Outils puis Addon Manager
3. Si c'est la première fois un message vous informe que les addons sont développer par la communauté et peuvent contenir des bugs. Cliquer sur OK.
4. Dans la fenêtre qui s'ouvre, attendre le chargement de la liste des addons.
5. Chercher l'atelier MOOC et cliquer une fois dessus.
6. Cliquer sur le bouton Install / update
7. À la fin de l'installation quand la fenêtre dit "Successfully installed ..." cliquer sur le bouton Close.
8. Enfin REDÉMARRER FreeCAD.


### Installation manuelle

1. Télécharger l'archive zip à cette adresse : [Mooc-Workbench.zip](https://framagit.org/freecad-france/mooc-workbench/-/archive/master/mooc-workbench-master.zip)

2. Extraire l'archive dans le dossier Mod de FreeCAD
L'emplacement du dossier Mod de FreeCAD dépend de votre système d'exploitation :

    *  Windows : habituellement C:\Users\username\AppData\Roaming\FreeCAD\Mod

    *  Mac : habituellement /Users/username/Library/Preferences/FreeCAD/Mod

    *  Linux : habituellement /home/username/.FreeCAD/Mod

    *  Si le dossier mod n'existe pas, créer le.

3. (Re)Lancer FreeCAD

## Utilisation

L'atelier est disponible depuis le menu Affichage puis Atelier ou depuis le sélecteur d'atelier :

<img src="/medias/images/MenuSelectWB.png" width=45% > <img src="/medias/images/ToolSelectWB.png" width=45% >

L'atelier MOOC propose 2 outils :

*  ![mooc-wb](/medias/images/mooc-player.png) MOOC Player qui permet de lancer les tutoriels interactifs.

*  ![mooc-wb](/medias/images/mooc-grader.png) MOOC Grader qui permet de faire une  évaluation d'un exercice.

### MOOC Player

Voir la vidéo : https://cloud.freecad-france.com/index.php/s/ZHgrfos6zpmyf73

Les tutoriaux interactif sont accessible depuis le menu **MOOC** puis **Voir un tutoriel** en cliquant sur le bouton : ![mooc-wb](/medias/images/mooc-player.png)

Une fenêtre s'ouvre avec une liste des tutoriel disponible :

<img src="/medias/images/ListeTuto.png" width=45% >

En faisant un simple clic sur un élément de la liste nous obtenons la description en dessous.

Pour valider le tutoriel à suivre faites un double clic ou cliquer sur le bouton OK.

Une nouvelle fenêtre s'ouvre et c'est le tutoriel qui commence.

<img src="/medias/images/PlayerWindow.png" width=45% >

<img src="/medias/images/OVPlayer.png" width=45% >

Le premier panneaux vous donne les consignes à suivre pour l'étape en cours.

Le bouton Vidéo ouvre une vidéo dans votre navigateur web par défaut.

Le bouton aide vous proposera les liens vers la documentation de chaque outils utilisé dans l'étape en cours.

Ensuite il y a la liste des objectifs qui s'affiche en rouge tant que l'objectif n'est pas remplie.

L'objectif passe au vert dès que qu'il est atteint.
Par exemple à cette étape la première chose à faire est de créer un nouveau document, dès que c'est fait, la ligne passe en vert.

Enfin vous avez des boutons pour passer à l'étape suivante ou pour revenir. Vous n'avez pas besoin de remplir tous les objectifs pour passer à l'étape suivante.

Lorsque vous avez atteint la fin du tutoriel vous pouvez fermer la fenêtre en cliquant sur la croix de fermeture.

### MOOC Grader

Lorsque vous avez terminer un exercice, vous allez pouvoir l'évaluer à l'aide du MOOC Grader.

Accessible depuis le menu **MOOC** puis **Évaluer un exercice** ou en cliquant sur le bouton : ![mooc-wb](/medias/images/mooc-grader.png)

<img src="/medias/images/FreeCADGraderWindow.png" width=45% >

Choisir l'éxercice dans la premiere liste.

Choisir le document FreeCAD à évaluer.

Cliquer sur le bouton **Lancer l'évaluation**.

Dans le panneau de gauche vous verrez les différent critère d'évaluation listé. Si vert alors c'est ok si c'est rouge c'est faux.

Quand l'évaluation vous satisfait vous pouvez transmettre les résultats en cliquant sur le bouton **Envoyer les résultats**

<img src="/medias/images/EnvoieResult.png" width=45% >

Une fenêtre s'ouvre avec une chaîne de caractère qu'il faut copier/coller dans votre espace MOOC. Vous pouvez cliquer sur le bouton **Copier** pour copier la chaine de caractère dans le presse papier. Il vous restera juste à le coller (clic droit coller ou avec le raccouris Ctrl+V).

<img src="/medias/images/CopyPasteResult.png" width=45% >


## Fonctionnement:

Chaque leçon ou t

## Créer un tutoriel

Il faut d'abord créer un dossier dans le dossier lessons.

Dans ce dossier il y aura :
 - un fichier python pour le contenu des étapes et les appels de vérification.
 - un dossier images avec les médias nécessaire au contenu du tutoriel.


Ensuite il faut l'éditer le fichier py :

Ligne 26 : renseigner votre nom

    __author__ = "Votre nom"

Ligne 41 : Changer le titre du cours.

        self.data_tutorial["title"] = "Le titre comme il apparaît dans la liste."

Ligne 42 : Changer la description du cours.

        self.data_tutorial["description"] = '''Mettre ICI la description du tutoriel : \
        On met un slashback "\" à la  fin des lignes dans le code \
        et on peut mettre "\n" pour faire un retour à la ligne.'''

Ligne 43 : renseigner le lien vers la vidéo

        url = "https://video_url.com"

Ensuite il faut copié collé le code de la ligne 45 à 57 autant de fois qu'il y a d'étapes dans votre tutoriel.

Une étape complète :

    # Step 1
    step = {}
    img1 = os.path.join(self.moocWB_icons_path, "Document-new.svg")
    step["video"] = str(url) + "?start=0m00s"
    step["objectives"] = ["Create a new document.",]
    step["checks"] = ["MoocChecker.document_presence()",]

    step["description"] = """<h3>Preparation</h3>
        <p><img src= %s width="25"/> Create a new document :
        <ul><li>with menu <i>File</i> then <i>New.</li>
        <li>with the shortcut Ctrl + N</li></ul></p> """ % (img1, )

    self.data_tutorial["steps"].append(step)


Ajouter des variable pour les icônes et les images :

    img1 = os.path.join(self.moocWB_icons_path, "icone.svg")
    img2 = os.path.join(self.moocWB_images_path, "image.png")

Définir l'horodotage de la vidéo :

    step["video"] = str(url) + "?start=0m00s"

La liste des objectifs à atteindre (les lignes qui passent de rouge à vert) :

    step["objectives"] = ["Objectif 1.",]

Les commandes à effectuer pour vérifier les objectifs :

    step["checks"] = ["MoocChecker.document_presence()",]

Pour les commandes il faut étudier le fichier MoocChecker.py qui contient de nombreuse fonctions de vérification.
