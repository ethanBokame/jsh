# Importation des modules


from tkinter import font
import pyperclip # Pour ajouter des éléments au presse papier



from PIL import Image

import webbrowser    # Pour créer des liens cliquables


import customtkinter

import os 


# Création de l'objet

app = customtkinter.CTk()

# Icone de l'app

icon = app.iconbitmap("programming-code-signs.ico")


# Titre de l'app

app.title("JsH")

# Taille de la frame du menu

width_menu = (app.winfo_screenwidth()*15)/100    # winfo_screenwidth renvoie la largeur de l'écran en pixel

height = app.winfo_screenheight()

# Largeur des frames en fonction de la largeur de la fenetre

width_frame = (app.winfo_screenwidth()*85)/100


# Style

font_algo = customtkinter.CTkFont(family= "Helvetica", size= 20)

font_menu = customtkinter.CTkFont(family= "Helvetica", size= 13)

font_btn_algo = customtkinter.CTkFont(family= "Helvetica", size= 14)

font_conv = customtkinter.CTkFont(family= "Helvetica", size= 14)

font_btn_prog = customtkinter.CTkFont(family= "Helvetica", size= 14)

font_label_prog = customtkinter.CTkFont(family= "Helvetica", size= 19)

font_label_advice = customtkinter.CTkFont(family= "Helvetica", size= 19)


app._state_before_windows_set_titlebar_color = 'zoomed'   # Pour mettre le fenêtre en fullscreen

app.resizable(width = False, height = False)   # Pour bloquer la taille de la fenêtre


# Couleur par défaut

customtkinter.set_appearance_mode("dark")

# Fonction pour switch de fonctionnalté

def clear(random_frame):
    
    slaves = random_frame.pack_slaves()    # Variable contenant la liste de tous les widgets enfants de la frame random_frame crée avec pack
    
    for x in slaves:    # Itère et supprime tous les enfants de la frame random_frame
        x.destroy()

def clear2(frame):
    slaves = frame.grid_slaves()
    for x in slaves:
        x.destroy()




# Frame du menu

frame = customtkinter.CTkFrame(app, width= width_menu, height= height, fg_color="#34383D", corner_radius=0)
frame.pack(fill="y", side="left")    # Allongé et à gauche

# Frame pour le corps de la fenêtre

framebody = customtkinter.CTkFrame(app,width= width_frame, height= height,corner_radius=0)
framebody.pack(fill="both", expand="True")    # fill="both" permet au widget de s'étendre sur tout l'espace disponible

# Taille de l'image

width_image = (app.winfo_screenwidth()*40)/100

height_image = (app.winfo_screenheight()*60)/100

# Margin top de l'image

margin_top = (app.winfo_screenheight()*15)/100

# add `from PIL import Image` on top
image_body = customtkinter.CTkImage(light_image=Image.open('programming-code-signs (3).png'),    # Image pour le body
                                    dark_image=Image.open('programming-code-signs (3).png'),
                                    size=(width_image, height_image))

label = customtkinter.CTkLabel(framebody, text = "", image = image_body)    # Label pour l'image
label.pack(pady = (margin_top, 0))

# Fonction pour les boutons des algorithmes
def active_algo():
    clear2(framebody)
    clear(framebody)    #Fonction qui efface tous les enfants de la frame frambody

    framescroll= customtkinter.CTkScrollableFrame(framebody,width= width_frame, height= height,corner_radius=0)  # Frame scrollante pour l'affichage des algo
    framescroll.pack(expand="True")
    
    label_algo = customtkinter.CTkLabel(framescroll, text="Voici les exercices d'algorithmes corrigés que je peux te proposer :", font = font_btn_algo)  # Phrase pour présenter les algo
    label_algo.pack(pady=(30, 12))
    
    margin_algo = (app.winfo_screenwidth()*2)/100 # Marge pour les algo
    
    algo = "-Algorithme"
    
    i = 1    # compteur des algo
    
    list_algo = [
                "de somme",
                "de calcul du carré d'un nombre",
                "de calcul de moyenne",
                "de calcul de factoriel",
                "de conversion secondes-heure",
                "de valeur absolue",
                "de parité-imparité",
                "de conversion degré-radiant",
                "de minimum-maximum",
                "de table de multiplication",
                "de recherches d'occurrences",
                "de recherche de PGCD",
                "de résolution d'équation du second degré",
                "de nombre premier",
                "de somme des valeurs d'un tableau",
                "de recherche d'élément dans un tableau",
                "de tri par ordre croissant",
                "de recherche de maximum et de minimum dans un tableau à deux dimensions"
                ]
    
    enonce = "Enoncé :"
    
    dict_enonce = {
        "1": "Ecrire un algorithme permettant de calculer et d'afficher la somme de deux nombres entiers entrés par l'utilisateur",
        "2": "Ecrire un algorithme permettant de calculer et d'afficher le carré d'un nombre entier entré par l'utilisateur",
        "3": "Ecrire un algorithme permettant de calculer et d'afficher la moyenne de deux notes entrées par l'utilisateur",
        "4": "Ecrire un algorithme permettant de calculer et d'afficher le factoriel d'un nombre entier n entré par l'utilisateur (n ≥ 0)",
        "5": "Ecrire un algorithme permettant de convertir le temps entré en secondes par l'utilisateur en heures, minutes et secondes",
        "6": "Ecrire un algorithme permettant de calculer et d'afficher la valeur absolue d'un nombre entier entré par l'utilisateur",
        "7": "Ecrire un algorithme permettant de vérifier si un nombre est pair ou impair et d'afficher le message correspondant",
        "8": "Ecrire un algorithme permettant de convertir le degré entré en radiant",
        "9": "Ecrire un programme qui demande de saisir 20 entiers et qui recherche et affiche le maximum et le minimum parmi les 20 entiers",
        "10": "Ecrire un algorithme permettant d'afficher la table de multiplication d'un nombre entier entré par l'utilisateur",
        "11": "Ecrire un programme qui demande de saisir 10 entiers et qui affiche le nombre d'occurrences de la note la plus haute",
        "12": "Ecrire un algorithme permettant de rechercher et d'afficher le PGCD entre deux nombres entiers entrés par l'utilisateur",
        "13": "Ecrire un algorithme permettant de résoudre une équation du second degré",
        "14": "Ecrire un algorithme permettant de vérifier si un nombre est premier ou non",
        "15": "Ecrire un algorithme permettant de calculer et d'afficher la somme des valeurs d'un tableau de 10 entiers entrés par l'utilisateur",
        "16": "Ecrire un programme qui demande à l'utilisateur de saisir 10 entiers stockés dans un tableau ainsi qu'un entier R. Le programme doit rechercher si R se trouve dans le tableau et afficher \"R se trouve dans le tableau\" ou \"R ne se trouve pas dans le tableau\"",
        "17": "Ecrire un algorithme permettant de trier par ordre croissant un tableau de 10 entiers entrés par l'utilisateur",
        "18": "Ecrire un algorithme permettant de rechercher et d'afficher le maximum et le minimum d'un tableau à 2 dimensions (tab[10][10])"
    }

    
    s = "          "    # Variable contenant des espaces

    dict_algo = {
        "1": "Algorithme : somme\n\nVariable a, b, resultat : entier\n\nDébut\n\nEcrire \"Entrez un premier nombre\"\n\nLire a\n\nEcrire \"Entrez un deuxième nombre\"\n\nLire b\n\nresultat ← a + b\n\nEcrire \"la somme de\"  a  \"et\"  b  \"est\"  resultat\n\nFin",
        "2": "Algorithme : carré d'un nombre\n\nVariable a, resultat : entier\n\nDébut\n\nEcrire \"Entrez un nombre\"\n\nLire a\n\nresultat ← a * a\n\nEcrire \"le carré de\"  a  \"est\"  resultat\n\nFin",
        "3": "Algorithme : moyenne\n\nVariable note_1, note_2, resultat : réel\n\nDébut\n\nEcrire \"Entrez la première note\"\n\nLire note_1\n\nEcrire \"Entrez la deuxième note\"\n\nLire note_2\n\nresultat ← (note_1 + note_2) / 2\n\nEcrire \"la moyenne est\"  resultat\n\nFin",
        "4": f"Algorithme : calcul de factoriel\n\nVariable n, factoriel, i : entier\n\nDébut\n\nEcrire \"Entrez un nombre entier\"\n\nLire n\n\nSi n = 0 Alors\n\n{s}factoriel ← 1\n\nSinon\n\n{s}factoriel ← 1\n\n{s}Pour i ← 1 à n Faire\n\n{s}{s}factoriel ← factoriel * i\n\n{s}FinPour\n\nFinSi\n\nEcrire \"Le factoriel de\"  n  \"est\"  factoriel\n\nFin",
        "5": "Algorithme : conversion secondes-heure\n\nVariable seconde_1, heure, minute, seconde_2 : entier\n\nDébut\n\nEcrire \"Entrez le nombre de secondes à convertir\"\n\nLire seconde_1\n\nheure ← seconde_1 DIV 3600\n\nminute ← (seconde_1 MOD 3600) DIV 60\n\nseconde_2 ← (seconde_1 MOD 3600) MOD 60\n\nEcrire \"La conversion de\"  seconde_1  \"donne\"  heure  \"heures\"  minute  \"minutes\"  seconde_2  \"secondes\"\n\nFin",
        "6": f"Algorithme : valeur absolue\n\nVariable a, resultat : entier\n\nDébut\n\nEcrire \"Entrez un nombre\"\n\nLire a\n\nSi a < 0 Alors\n\n{s}resultat ← a * -1\n\nSinon\n\n{s}resultat ← a\n\nFin Si\n\nEcrire \"La valeur absolue de\"  a  \"est\"  resultat\n\nFin",
        "7": f"Algorithme : parité-imparité\n\nVariable a : entier\n\nDébut\n\nEcrire \"Entrez un nombre entier\"\n\nLire a\n\nSi a MOD 2 = 0 Alors\n\n{s}Ecrire \"Le nombre est pair\"\n\nSinon\n\n{s}Ecrire \"Le nombre est impair\"\n\nFin Si\n\nFin",
        "8": "Algorithme : conversion degré-radiant\n\nVariable degre, radiant : réel\n\nDébut\n\nEcrire \"Entrez un angle en degré\"\n\nLire degre\n\nradiant ← degre * (3.14 / 180)\n\nEcrire \"La conversion de\"  degre  \"degrés en radiant donne\"  radiant\n\nFin",
        "9": f"Algorithme : minimum-maximum\n\nVariable min, max : réel ;  i : entier\n\nTableau nombre[ 20 ] : réel\n\nDébut\n\nEcrire \"Entrez le premier nombre\"\n\nLire nombre[ 0 ]\n\nmax ← nombre[ 0 ]\n\nmin ← nombre[ 0 ]\n\nPour i ← 1 à 19 Faire\n\n{s}Ecrire \"Entrez le nombre\" i + 1\n\n{s}Lire nombre[ i ]\n\n{s}Si nombre[ i ] > max Alors\n\n{s}{s}max ← nombre[ i ]\n\n{s}SinonSi nombre[ i ] < min Alors\n\n{s}{s}min ← nombre[ i ]\n\n{s}FinSi\n\nFinPour\n\nEcrire \"Le maximum de la série est :\"  max  \"et le minimum de la série est :\"  min\n\nFin",
        "10": f"Algorithme : table de multiplication\n\nVariable nombre, i : entier\n\nDébut\n\nEcrire \"Entrez un nombre\"\n\nLire nombre\n\nPour i ← 1 à 10 Faire\n\n{s}Ecrire nombre  \"x\"  i  \"=\"  nombre * i\n\nFinPour\n\nFin",
        "11": f"Algorithme : nombre d'occurrences\n\nVariable occurrence, i, max : entier\n\nTableau nombre[ 10 ] : entier\n\nDébut\n\noccurrence ← 1\n\nEcrire \"Entrez le premier nombre\"\n\nLire nombre[ 0 ]\n\nmax ← nombre[ 0 ]\n\nPour i ← 1 à 9 Faire\n\n{s}Ecrire \"Entrez le nombre\" i + 1\n\n{s}Lire nombre[ i ]\n\nFinPour\n\nPour i ← 0 à 9 Faire\n\n{s}Si nombre[ i ] > max Alors\n\n{s}{s}max ← nombre[ i ]\n\n{s}{s}occurrences ← 1\n\n{s}SinonSi nombre[ i ] = max Alors\n\n{s}{s}occurrence ← occurrence + 1\n\n{s}FinSi\n\nFinPour\n\nEcrire \"Le nombre d'occurrences de la plus haute valeur est :\"  occurrence\n\nFin",
        "12": f"Algorithme : PGCD\n\nVariable diviseur, dividende, reste : entier\n\nDébut\n\nEcrire \"Entrez le premier nombre\"\n\nLire diviseur\n\nEcrire \"Entrez le deuxième nombre\"\n\nLire dividende\n\nTantQue reste ≠ 0\n\nFaire\n\n{s}reste ← dividende MOD diviseur\n\n{s}dividend ← diviseur\n\n{s}diviseur ← reste\n\nFinTantQue\n\nEcrire \"Le PGCD est :\" diviseur\n\nFin",
        "13": f"Algorithme : équation du second degré\n\nVariable a, b, c, delta, racine1, racine2 : réel\n\nDébut\n\nEcrire \"Entrez les coefficients a, b et c\"\n\nLire a, b, c\n\ndelta ← b * b - 4 * a * c\n\nSi delta < 0 Alors\n\n{s}Ecrire \"Pas de solutions réelles\"\n\nSinonSi delta = 0 Alors\n\n{s}racine1 ← -b / (2 * a)\n\n{s}Ecrire \"La solution double est :\" racine1\n\nSinon\n\n{s}racine1 ← (-b + sqrt(delta)) / (2 * a)\n\n{s}racine2 ← (-b - sqrt(delta)) / (2 * a)\n\n{s}Ecrire \"Les solutions sont :\" racine1, racine2\n\nFinSi\n\nFin",
        "14": f"Algorithme : vérification de nombre premier\n\nVariable n, i : entier\n\nDébut\n\nEcrire \"Entrez un nombre entier\"\n\nLire n\n\nSi n < 2 Alors\n\n{s}Ecrire \"Ce n'est pas un nombre premier\"\n\nSinon\n\n{s}pour i ← 2 à racine(n) Faire\n\n{s}{s}Si n MOD i = 0 Alors\n\n{s}{s}{s}Ecrire \"Ce n'est pas un nombre premier\"\n\n{s}{s}{s}Fin\n\n{s}{s}FinPour\n\n{s}Ecrire \"C'est un nombre premier\"\n\nFinSi\n\nFin",
        "15": f"Algorithme : somme tableau\n\nVariable somme, i : entier\n\nTableau nombre[10] : entier\n\nDébut\n\nsomme ← 0\n\nPour i ← 0 à 9 Faire\n\n{s}Ecrire \"Entrez le nombre\" i + 1\n\n{s}Lire nombre[i]\n\n{s}somme ← somme + nombre[i]\n\nFinPour\n\nEcrire \"La somme des valeurs est :\" somme\n\nFin",
        "16": f"Algorithme : recherche dans un tableau\n\nVariable R, i : entier\n\nTableau nombre[10] : entier\n\nDébut\n\nEcrire \"Entrez un entier R\"\n\nLire R\n\nPour i ← 0 à 9 Faire\n\n{s}Ecrire \"Entrez le nombre\" i + 1\n\n{s}Lire nombre[i]\n\nFinPour\n\nTrouvé ← Faux\n\nPour i ← 0 à 9 Faire\n\n{s}Si nombre[i] = R Alors\n\n{s}{s}Trouvé ← Vrai\n\n{s}{s}FinSi\n\nFinPour\n\nSi Trouvé Alors\n\n{s}Ecrire \"R se trouve dans le tableau\"\n\nSinon\n\n{s}Ecrire \"R ne se trouve pas dans le tableau\"\n\nFinSi\n\nFin",
        "17": f"Algorithme : tri tableau\n\nVariable i, j, temp : entier\n\nTableau nombre[10] : entier\n\nDébut\n\nPour i ← 0 à 9 Faire\n\n{s}Ecrire \"Entrez le nombre\" i + 1\n\n{s}Lire nombre[i]\n\nFinPour\n\nPour i ← 0 à 8 Faire\n\n{s}Pour j ← i + 1 à 9 Faire\n\n{s}{s}Si nombre[i] > nombre[j] Alors\n\n{s}{s}{s}temp ← nombre[i]\n\n{s}{s}{s}nombre[i] ← nombre[j]\n\n{s}{s}{s}nombre[j] ← temp\n\n{s}{s}FinSi\n\n{s}FinPour\n\nFinPour\n\nEcrire \"Le tableau trié est :\"\n\nPour i ← 0 à 9 Faire\n\n{s}Ecrire nombre[i]\n\nFinPour\n\nFin",
        "18": f"Algorithme : min et max dans un tableau 2D\n\nVariable i, j, min, max : entier\n\nTableau tab[10][10] : entier\n\nDébut\n\nPour i ← 0 à 9 Faire\n\n{s}Pour j ← 0 à 9 Faire\n\n{s}{s}Ecrire \"Entrez l'élément tab[\" i \"][\" j \"]\"\n\n{s}{s}Lire tab[i][j]\n\n{s}FinPour\n\nFinPour\n\nmin ← tab[0][0]\n\nmax ← tab[0][0]\n\nPour i ← 0 à 9 Faire\n\n{s}Pour j ← 0 à 9 Faire\n\n{s}{s}Si tab[i][j] < min Alors\n\n{s}{s}{s}min ← tab[i][j]\n\n{s}{s}FinSi\n\n{s}{s}Si tab[i][j] > max Alors\n\n{s}{s}{s}max ← tab[i][j]\n\n{s}{s}FinSi\n\n{s}FinPour\n\nFinPour\n\nEcrire \"Le minimum est :\" min\n\nEcrire \"Le maximum est :\" max\n\nFin"
    }

    for item in list_algo:   # Boucle pour afficher les algo
        
        def action_button(ite):    # Fonction d'affichage des algorithmes ciblés lors du click d'un bouton d'algorithme
            
            clear(framescroll)
            
            label_enonce = customtkinter.CTkLabel(framescroll, text=f"{enonce} {dict_enonce[str(ite)]}.", justify="left", font = font_algo, wraplength = (app.winfo_screenwidth()*75)/100)
            label_enonce.pack(pady=(10,15), padx=(margin_algo), anchor="nw")
            
            label_algo = customtkinter.CTkLabel(framescroll, text=f"{dict_algo[str(ite)]}", justify="left", font = font_algo)
            label_algo.pack(pady=(10,10), padx=(margin_algo), anchor="nw")    # anchor="nw" pour mettre le label en haut à gauche
        
        button = customtkinter.CTkButton(framescroll, text=f"{i}{algo} {item}", width=140, height=28, command = lambda i = i : action_button(i), font = font_btn_algo)    # Bouton des algorithmes 
        button.pack(pady=(10))
        
        i += 1    # Incémentation d'un compteur pour les numéros des algorithmes

# Bouton pour l'affichage des algorithmes

button_algo = customtkinter.CTkButton(frame, text="Exemples d'algorithmes", width= width_menu, height=40, corner_radius=0, command=active_algo, font = font_menu)
button_algo.pack(fill="both")

# Fonction pour la conversion de bases de numération
def conv():
    clear2(framebody)
    clear(framebody)    # Effacement de la frame body
    
    margin_top = (app.winfo_screenheight()*15)/100
    
    frame_conversion = customtkinter.CTkFrame(framebody, width=200, height=200)    # frame pour regrouper tous les éléments de conversion
    frame_conversion.pack(pady=(margin_top,0))
    
    nombre = customtkinter.CTkLabel(frame_conversion, text="Nombre:", fg_color='transparent') # Mot nombre en haut de la première entrée
    nombre.pack(anchor = "w", padx = (31, 0), pady=(25,0))
    
    entry = customtkinter.CTkEntry(frame_conversion, width=300, height=40, corner_radius=0, border_width=1)    # Entrée du nombre à convertir
    entry.pack(padx = (10), pady=(0,10))
    
    delabase = customtkinter.CTkLabel(frame_conversion, text="De la base: ", fg_color='transparent') # Mot delabase en haut de la deuxième entrée
    delabase.pack(anchor = "w", padx = (31, 0))
    
    
    liste_base = ["2 (binaire)", "8 (octal)", "10 (décimal)", "16 (hexadécimal)"]    # liste pour les bases de numérations
    
    def optionmenu_callback1(choice):
        return 0
    
    optionmenu_var1 = customtkinter.StringVar(value = "10 (décimal)")
    optionmenu1 = customtkinter.CTkOptionMenu(frame_conversion,values = liste_base,width=300, height=40, command=optionmenu_callback1, variable = optionmenu_var1, corner_radius=0)
    optionmenu1.pack(pady=(0,10))
    
    verslabase = customtkinter.CTkLabel(frame_conversion, text="Vers la base: ", fg_color='transparent') # Mot verslabase en haut de la troisième entrée
    verslabase.pack(anchor = "w", padx = (31, 0))
    
    
    liste_base = ["2 (binaire)", "8 (octal)", "10 (décimal)", "16 (hexadécimal)"]    # liste pour les bases de numérations
    
    def optionmenu_callback2(choice):
        return 0
    
    optionmenu_var2 = customtkinter.StringVar(value = "2 (binaire)")
    
    optionmenu2 = customtkinter.CTkOptionMenu(frame_conversion,values = liste_base,width=300, height=40, command=optionmenu_callback2, variable = optionmenu_var2, corner_radius=0)    # Base de numération finale
    optionmenu2.pack(pady = (0,10))
    
    image_convert = customtkinter.CTkImage(light_image=Image.open("refresh-regular-24.png"),    # image de conversion
                                dark_image=Image.open("refresh-regular-24.png"),
                                size=(20, 20))
    
    def conversion():
        
        global resultat_final    # Résultat final
        
        base1 = 0    # base de départ
        
        base2 = 0    # base d'arrivée


        def verificator(input, number_max):
            
            for i in input:
                try:
                    if int(i) > number_max:
                        entry.configure(fg_color = "#800E0E")
                        label_resultat.configure(text = "")
                        return False
                    
                except:
                    entry.configure(fg_color = "#800E0E")
                    label_resultat.configure(text = "")
                    return False
    
        def verificator_16(input):
            ok = True

            liste_hexadecimal = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F","a","b","c","d","e","f"]

            for i in input:

                if i in liste_hexadecimal:
                    ok = True

                else:
                    ok = False
                    entry.configure(fg_color = "#800E0E")
                    label_resultat.configure(text = "")
                    return False


        
        if optionmenu_var1.get() == "2 (binaire)":
            base1 = 2
        
        elif optionmenu_var1.get() == "8 (octal)":
            base1 = 8
        
        elif optionmenu_var1.get() == "10 (décimal)":
            base1 = 10
        
        elif optionmenu_var1.get() == "16 (hexadécimal)":
            base1 = 16
        
        if optionmenu_var2.get() == "2 (binaire)":
            base2 = 2
        
        elif optionmenu_var2.get() == "8 (octal)":
            base2 = 8
        
        elif optionmenu_var2.get() == "10 (décimal)":
            base2 = 10
        
        elif optionmenu_var2.get() == "16 (hexadécimal)":
            base2 = 16
        
        if base1 == 2 and base2 == 2:    # Premier cas de la base 2

            
            if verificator(entry.get(), 1) != False:
                
                resultat_final = int(entry.get())
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 2 and base2 == 8:
            
            if verificator(entry.get(), 1) != False:
                
                resultat_final = int(entry.get(), 2)
                resultat_final = oct(resultat_final)
                resultat_final = resultat_final[1:]    # Permet d'enlever le 0
                resultat_final = resultat_final[1:]
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 2 and base2 == 10:
            
            if verificator(entry.get(), 1) != False:
                
                resultat_final = int(entry.get(), 2)
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 2 and base2 == 16:
            
            if verificator(entry.get(), 1) != False:
                
                resultat_final = int(entry.get(), 2)
                resultat_final = hex(resultat_final)
                resultat_final = resultat_final[1:]    # Permet d'enlever le 0
                resultat_final = resultat_final[1:]
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide
    
        if base1 == 8 and base2 == 8:    # Premier cas de la base 8
            
            
            if verificator(entry.get(), 7) != False:
                
                resultat_final = int(entry.get())
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 8 and base2 == 2:
            
            if verificator(entry.get(), 7) != False:
                
                resultat_final = int(entry.get(), 8)
                resultat_final = bin(resultat_final)
                resultat_final = resultat_final[1:]    # Permet d'enlever le 0
                resultat_final = resultat_final[1:]
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 8 and base2 == 10:
            
            if verificator(entry.get(), 7) != False:
                
                resultat_final = int(entry.get(), 8)
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 8 and base2 == 16:
            
            if verificator(entry.get(), 7) != False:
                
                resultat_final = int(entry.get(), 8)
                resultat_final = hex(resultat_final)
                resultat_final = resultat_final[1:]    # Permet d'enlever le 0
                resultat_final = resultat_final[1:]
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 10 and base2 == 10:    # premier cas de la base 10
            
            if verificator(entry.get(), 9) != False:
                
                resultat_final = int(entry.get())
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 10 and base2 == 2:    
            
            if verificator(entry.get(), 9) != False:
                
                resultat_final = bin(int(entry.get()))
                resultat_final = resultat_final[1:]    # Permet d'enlever le 0
                resultat_final = resultat_final[1:]
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 10 and base2 == 8:    
            
            if verificator(entry.get(), 9) != False:
                
                resultat_final = oct(int(entry.get()))
                resultat_final = resultat_final[1:]    # Permet d'enlever le 0
                resultat_final = resultat_final[1:]
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 10 and base2 == 16:    
            
            if verificator(entry.get(), 9) != False:
                
                resultat_final = hex(int(entry.get()))
                resultat_final = resultat_final[1:]    # Permet d'enlever le 0
                resultat_final = resultat_final[1:]
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 16 and base2 == 16:    # premier cas de la base 16
            
            if verificator_16(entry.get()) != False:
                
                resultat_final = entry.get()
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 16 and base2 == 2:
            
            if verificator_16(entry.get()) != False:
                
                resultat_final = int(entry.get(), 16)
                resultat_final = bin(resultat_final)
                resultat_final = resultat_final[1:]    # Permet d'enlever le 0
                resultat_final = resultat_final[1:]
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 16 and base2 == 8:
            
            if verificator_16(entry.get()) != False:
                
                resultat_final = int(entry.get(), 16)
                resultat_final = oct(resultat_final)
                resultat_final = resultat_final[1:]    # Permet d'enlever le 0
                resultat_final = resultat_final[1:]
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide

        if base1 == 16 and base2 == 10:
            
            if verificator_16(entry.get()) != False:
                
                resultat_final = int(entry.get(), 16)
                
                label_resultat.configure(text = resultat_final)
                entry.configure(fg_color = "#343638")    # Revenir à la couleur par défaut en cas d'entrée valide



    button_convert = customtkinter.CTkButton(frame_conversion,image = image_convert, text='Convertir', width=140, height=28, corner_radius = 2, command = conversion)    # Bouton de conversion
    button_convert.pack(pady=(10))
    
    result = customtkinter.CTkLabel(frame_conversion, text="Résultat:", fg_color='transparent') # Mot résultat
    result.pack(anchor = "w", padx = (30, 0))
    
    resultat = customtkinter.CTkScrollableFrame(frame_conversion,width=300, height=40, orientation = "horizontal", corner_radius = 2)    # Frame où sera affiché le résultat 
    resultat.pack(pady = (0, 10), padx = (30, 30))
    
    
    label_resultat = customtkinter.CTkLabel(resultat, text = "", fg_color='transparent')    # Résultat en lui même
    label_resultat.pack()
    
    resultat.pack()
    
    # add `from PIL import Image` on top
    image_copy = customtkinter.CTkImage(light_image=Image.open("copy-solid-24.png"),    # image pour la copie
                                    dark_image=Image.open("copy-solid-24.png"),
                                    size=(30, 30))
    
    def copy():
        pyperclip.copy(resultat_final)
    
    button_copy = customtkinter.CTkButton(frame_conversion, image = image_copy, text = "Copy", width=40, height=28, command = copy, corner_radius = 2)    # Bouton pour copier
    button_copy.pack(side = "left", padx = (30, 0), pady = (10, 30),)

button_conv = customtkinter.CTkButton(frame, text="Conversion de base de numération", height=40, corner_radius=0, command=conv, font = font_menu)
button_conv.pack(fill="both")

# Fonction pour les langages de programmation

def prog():
    
    clear2(framebody)    # Effacement des fenêches précédentes
    clear(framebody)
    
    margin = (app.winfo_screenwidth()*0.93)/100
    
    margin_label_prog = (app.winfo_screenwidth()*2)/100
    
    padding_top = app.winfo_screenheight()*3/100    
    
    index_bouton = 1    # index de la liste
    
    
    framescroll= customtkinter.CTkScrollableFrame(framebody,width= width_frame, height= height,corner_radius=0)  # Frame scrollante pour l'affichage des langages de programmation
    framescroll.pack(expand="True")
    
    list_prog = [
                "Python",
                "C",
                "Html",
                "Css",
                "Java",
                "C++", 
                "Javascript",
                "Php",
                "Sql",
                "Prolog",
                "Perl",
                "Dart",
                ]
    
    s = "\n\nSite: "    # Variable qui servira à factoriser la string qu'il contient dans l'affichage des définitions
    
    dict_prog = {
                "1" : f"Python est un langage de programmation interprété, de haut niveau, multi-paradigme et de scripts orienté objet. Il a été conçu par Guido Van Rossum dans les années 90. Python est utilisé dans la création d'algorithmes de machine learning, dans le développement d'intelligences artificielles, dans l'analyse de données à grande comme à petite échelle, etc. Sa syntaxe simple se rapprochant de l'algorithme de base le rend plus compréhensible par l'être humain et moins << prise de tête >>. Bénéficiant d'une large communauté active et d'une syntaxe simple, python est un langage idéal pour débuter en programmation et mettre en pratique toute la théorie algorithmique.{s}",
                
                "2" : f"Le langage C est un langage de programmation compilé, procédural et de bas niveau. Il a été créé en 1972 par les développeurs et scientifiques en informatique Dennis Ritchie et Ken Thompson. Etant un langage compilé, le C doit être traduit à l'aide d'un compilateur en langage machine avant d'être exécuté par le processeur. Voici quelques compilateurs C fréquement utilisés par la communauté: Clang, GCC, Turbo C++. Son niveau bas, c'est à dire plus proche du langage machine, lui permet de mieux intéragir avec le système d'exploitation et le processeur. Le langage C est utilisé dans le développement de systèmes d'exploitations (ex: Linux), dans la programmation de systèmes embarqués (ex: Arduino) et même dans le développement de jeux vidéos. Son allocation statique de la mémoire et sa syntaxe rigoureuse font de lui un très bon choix pour apprendre les bonnes pratiques de la programmations.{s}",
                
                "3" : f"Le Html (Hypertext Markup Language) n'est en réalité pas un langage de programmation mais un langage de balisage utilisé pour sctructurer une page web et son contenu à l'aide de balises. A noter que c'est l'un des langages de balisage les plus utilisé monde, de par sa syntaxe facile et de sa compréhension rapide par l'humain. Le Html s'impose comme un pilier du web à l'heure actuelle. Mais avec un peu de pratique tu t'en rendras bien compte, le Html seul ne permet pas de faire un site web qui se vaut aujourd'hui. Il aura donc besoin de son complémentaire, le Css.{s}",
                
                "4" : f"Le Css (Cascading Style Sheets) n'est pas un langage de programmation mais un langage de feuilles de style en cascade complémentaire du html, c'est à dire que les feuilles de style peuvent être appliquées à plusieurs éléments de la même page web. Il permet de personnaliser l'apparence d'un site web en utilisant des propriétés appliquées à des classes attribuées aux éléments du html (en gros il permet de rendre le site plus beau et plus attrayant). Il est utilisé la plupart du temps dans le développement de sites web, mais peut servir à bien d'autres choses.{s}",
                
                "5" : f"Java est un langage orienté objet, multi-plateforme et de haut niveau. Lorsqu’un programmeur écrit une application Java, le code compilé (appelé bytecode) peut s’exécuter sur la plupart des systèmes d’exploitation (OS), y compris Windows, Linux et Mac OS grâce à la JVM (Java Virtual Machine). Java est utilisé dans la réalisation d'applications web, desktop, android et même de jeux. sa polyvalence fait de lui un langage incontournable à l'heure actuelle dans le monde numérique. Pour la petite histoire le logo de Java est une tasse parce qu'à l'époque les développeurs de Java ont bu beaucoup de tasses de café en travaillant sur celui-ci haha.{s}",
                
                "6" : f"Le C++ est un langage de programmation compilé, multi-paradigme et de bas niveau. Développé en 1983 par Bjarne Stroustrup qui voulait incrémenter le langage C (d'où le nom, C++ signifiant \"ajouter 1 à C\"). Ce langage apporte donc de nouvelles fonctionnalités par rapport au C, notamment la programmation orientée objet avec les classes, les méthodes etc et des interfaces graphiques de plus en plus poussées. En plus d'être rapide, de permettre la création de logiciels pour plusieurs platformes en même temps, le C++ bénéficie d'une importante communauté active sur internet. Il est utilisé dans le développement de logiciels systèmes (pilotes) et principalement dans le développement de jeux vidéos, à titre d'exemple : Fortnite, Fifa, Naruto Storm etc. Il est très important de préciser que le C++ est considéré comme l'un des langages les plus difficile à apprendre. Sa compréhension la plus totale demande des années d'expérience et de patience, alors accroche toi !{s}",
                
                "7" : f"JavaScript est un langage de programmation interprété, de haut niveau, multi-paradigme et principalement utilisé côté client dans les navigateurs web. Il a été développé par Brendan Eich en 1995 chez Netscape Communications Corporation. JavaScript est essentiellement utilisé pour rendre les pages web dynamiques et interactives, manipuler le DOM (Document Object Model), gérer des événements, et créer des applications front-end riches sans recharger la page. Sa flexibilité et sa puissance croissantes grâce à des frameworks comme React, Angular, et Vue.js, en font un outil indispensable pour les développeurs web modernes. Malgré son nom, JavaScript n'est pas lié au langage Java, bien qu'il partage certaines similitudes de syntaxe.{s}",
                
                "8" : f"PHP est un langage de script open source, interprété, et de haut niveau. Il a été créé par Rasmus Lerdorf en 1994. PHP est largement utilisé pour le développement web back-end, permettant aux développeurs de créer des applications web dynamiques et interactives. Il est particulièrement populaire pour le développement de sites web e-commerce et de gestion de contenu. PHP est également utilisé pour le développement d'applications mobiles via des frameworks comme Laravel, Symfony, et CodeIgniter. Sa simplicité et sa facilité d'utilisation en font un choix populaire pour les débutants en programmation web.{s}",
                
                "9" : f"SQL (Structured Query Language) n'est pas un langage de programmation au sens traditionnel, mais plutôt un langage de manipulation de bases de données relationnelles. Il permet de créer, modifier, et extraire des données stockées dans des bases de données. SQL est utilisé pour interagir avec des systèmes de gestion de bases de données (SGBD) comme MySQL, PostgreSQL, Oracle Database, et Microsoft SQL Server. Il offre une interface standardisée pour effectuer des opérations complexes telles que les jointures, les sous-requêtes, et les transactions. La maîtrise de SQL est cruciale pour tout développeur ou analyste travaillant avec des bases de données.{s}",
                
                "10" : f"Prolog est un langage de programmation logique et de recherche, utilisé principalement dans les domaines de l'informatique théorique, de l'intelligence artificielle, et de la recherche opérationnelle. Il a été développé dans les années 70 par Alain Colmerauer, Philippe Roussel, et Robert Prost. Prolog est basé sur la logique première ordre et utilise une approche récursive pour résoudre des problèmes. Il est particulièrement adapté pour la représentation du raisonnement et de la résolution de problèmes complexes, comme la planification, la reconnaissance de formes, et la traduction automatique. Sa syntaxe unique et ses capacités avancées en logique font de Prolog un choix spécialisé parmi les langages de programmation.{s}",
                
                "11" : f"Perl est un langage de script interprété, de haut niveau, et multi-paradigme. Il a été créé par Larry Wall en 1987. Perl est connu pour sa grande flexibilité et sa puissance dans le traitement de texte, la manipulation de fichiers, et la gestion de processus. Il est souvent décrit comme un langage \"glue\" car il facilite la liaison entre différents programmes et systèmes. Perl est particulièrement populaire pour le scripting système, le nettoyage de données, et le développement web. Sa syntaxe concise et ses nombreuses bibliothèques font de Perl un outil efficace pour automatiser des tâches complexes.{s}",
                
                "12" : f"Dart est un langage de programmation développé par Google et annoncé en 2011. Dart est un langage compilé, orienté objet, et multi-paradigme. Il est principalement utilisé pour le développement d'applications mobiles avec Flutter, une bibliothèque UI populaire pour la création d'applications Android et iOS. Dart supporte aussi le développement côté serveur avec le framework Dart Server. Sa conception moderne et sa performance optimisée en font un choix solide pour les développeurs cherchant à créer des applications natives performantes. Dart offre également une forte intégration avec les autres technologies Google, comme Firebase et Google Cloud Platform.{s}",
                }
    
    dict_sites = {
        "1" : "https://www.python.org/",
        "2" : "https://fr.wikipedia.org/wiki/C_(langage)",
        "3" : "https://developer.mozilla.org/fr/docs/Web/HTML",
        "4" : "https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/CSS_basics",
        "5" : "https://www.java.com/fr/",
        "6" : "https://devdocs.io/cpp-compiler-support/",
        "7" : "https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide",
        "8" : "https://www.php.net/",
        "9" : "https://www.w3schools.com/sql/",
        "10" : "http://prolog.droogans.com/",
        "11" : "https://www.perl.org/",
        "12" : "https://dart.dev/guides",
    }


    def get_prog(first_language, last_language):
        for j in range(first_language, last_language):
            
            def action_button(ite):    # Fonction d'affichage des LP ciblés lors du click d'un bouton LP
            
                clear(framebody)
            
                label_prog = customtkinter.CTkLabel(framebody, text=f"{dict_prog[str(ite)]}", justify="left", wraplength = (app.winfo_screenwidth()*75)/100, font = font_label_prog) # wraplength pour la taille maximale d'une ligne d'un label
                label_prog.pack(pady=(10,10), padx=(margin_label_prog, 0), anchor="nw")    # anchor="nw" pour mettre le label en haut à gauche
            
                label_site = customtkinter.CTkLabel(framebody, text=f"{dict_sites[str(ite)]}", justify = "left", cursor = "hand2", text_color = "#0078D4", font = ("Times", 20, "underline"))
                label_site.pack(pady=(5,5), padx=(margin_label_prog, 0), anchor="nw")
                label_site.bind("<Button-1>", lambda e: webbrowser.open(dict_sites[str(ite)]))    # Pour créer un lien hypertext
        
            buttonprog = customtkinter.CTkButton(framescroll, text=f"{list_prog[j]}", width=140, height=28, command = lambda i = j+1 : action_button(i), corner_radius = 2, font = font_btn_prog)    # Bouton des algorithmes 
            buttonprog.pack( pady = (15,15), padx = (margin, margin))


    for i in range(5):

        if i == 0:
            
            label_prog = customtkinter.CTkLabel(framescroll, text = "La présentation des langages de programmation est entièrement basée sur le programme universitaire du département informatique de l'institut universitaire d'Abidjan (IUA)",wraplength = (app.winfo_screenwidth()*75)/100, font= font_label_prog)
            label_prog.pack(pady = (padding_top, 0))

        elif i == 1:
            
            label_prog = customtkinter.CTkLabel(framescroll, text = "License 1 :",wraplength = (app.winfo_screenwidth()*75)/100, font= font_label_prog)
            label_prog.pack(pady = (padding_top, 0))
            
            get_prog(0, 4)

        elif i == 2:
            
            label_prog = customtkinter.CTkLabel(framescroll, text = "License 2 :",wraplength = (app.winfo_screenwidth()*75)/100, font= font_label_prog)
            label_prog.pack(pady = (padding_top, 0))
            
            get_prog(4, 10)

        
        elif i == 3:
            
            label_prog = customtkinter.CTkLabel(framescroll, text = "License 3 :",wraplength = (app.winfo_screenwidth()*75)/100, font= font_label_prog)
            label_prog.pack(pady = (padding_top, 0))
            
            get_prog(10, 12)


button_prog = customtkinter.CTkButton(frame, text="Langages de programmations", height=40, corner_radius=0, command = prog, font = font_menu)
button_prog.pack(fill="both")

# Fonction pour l'affichage des conseils
def good_advices():
    
    clear2(framebody)    # Effacement des fenetres précédentes
    clear(framebody)
    
    margin_advice = (app.winfo_screenwidth()*2)/100
    
    framescroll= customtkinter.CTkScrollableFrame(framebody,width= width_frame, height= height,corner_radius=0, )  # Frame scrollante pour l'affichage des algo
    framescroll.pack(expand="True")
    list_advice = [
        "Concentre toi en Algorithmique, c'est le pilier de la programmation !",
        "Commence par apprendre des langages de programmations pas trop chargés comme python, html et css.",
        "Fonctionne par projets. Savoir écrire if en python ne fais pas de toi un développeur. Pour chaque langage que tu vas apprendre, utilise le de manière concrète dans un projet. Réalise des projets personnels qui te motivent réellement !",           
        "Tu fais de la programmation pour toi et toi seul, ce n'est pas une compétition.",
        "Progresser en programmation et en informatique en général demande beaucoup de patience et énormément de temps. Prend ton temps pour bien apprendre, ce n'est pas la course.",
        "Reste calme et patient quand tu rencontres des bugs et des problèmes lors de tes projets. C'est dans le calme qu'on trouve des solutions.",
        "Ne te complexe pas de trouver des manières de faire différentes de celles de autres, tu es unique et c'est ce qui fera de toi un développeur hors pairs.",
        "Soit extrêment fier de ton de travail, n'hésite jamais à l'afficher. Même si c'est un programme qui affiche juste <<Hello World>>.",
        "N'hésite pas à partager ton travail avec d'autres développeurs, voir même avec les non développeurs. A quoi cela sert-il de créer tout cela si personne ne sait que tu le fait?",
        "Recherche toujours un retour utilisateur  sur tes projets, de la part des autres.",
        "Marche avec des gens qui, sont aussi, voir plus performants que toi, laisse ceux qui ne veulent pas travailler dans leur coin.",
        "N'hésite pas à demander de l'aide.",
        "Par dessus tout, amuse toi et fait des trucs fun c'est le plus important :)",
        "Voici les plateformes que je peux te recommander pour apprendre la programmation:",
        ]
    
    #Pour l'en tête
    label_advice1 = customtkinter.CTkLabel(framescroll, text="Voici les conseils que je peux te donner en matière de programmation !", font = font_label_advice)
    label_advice1.pack(pady=(10,15), padx=(margin_advice), anchor="nw")
    
    #Pour le body (les conseils)
    for item in list_advice:    #Boucle pour afficher les conseils
        
        label_advice2 = customtkinter.CTkLabel(framescroll, text=f"{item}", justify = "left", font = font_label_advice, wraplength = (app.winfo_screenwidth()*75)/100)    # justify left pour mettre le texte du label à gauche
        label_advice2.pack(pady=(10,10), padx=(margin_advice), anchor="nw")    # anchor="nw" pour mettre le label en haut à gauche
    
    #Les liens des plateformes pour apprendre la programmation
    list_site = ["https://openclassrooms.com/fr/", "https://www.udemy.com/", "https://www.w3schools.com/", "https://www.alphorm.com/", "https://em-coder.netlify.app/", "https://zestedesavoir.com/bibliotheque/informatique/programmation-et-algorithmique/", "https://roadmap.sh/", "https://developer.mozilla.org/fr/"]
    
    def link(url):    # Fonction pour l'affichage d'un lien fonctionnel
        label_advice = customtkinter.CTkLabel(framescroll, text=f"{url}", justify = "left", cursor = "hand2",text_color = "#0078D4", font = ("Times", 20, "underline"))
        label_advice.pack(pady=(5,5), padx=(margin_advice), anchor="nw")
        label_advice.bind("<Button-1>", lambda e: webbrowser.open(url))    # Pour créer un lien hypertext
    
    for item in list_site:
        link(item)

# Bouton pour atterir à la page de conseils

button_advices = customtkinter.CTkButton(frame, text="Conseils pour la programmation", height=40, corner_radius=0, command = good_advices, font = font_menu)
button_advices.pack(fill="both")

label_advice = customtkinter.CTkLabel(frame, text=f"Créateur", justify = "left", cursor = "hand2",text_color = "#0078D4", font = ("Times", 22, "underline"))
label_advice.pack(pady=(20,5), padx=((app.winfo_screenwidth()*5)/100,0), anchor="nw")
label_advice.bind("<Button-1>", lambda e: webbrowser.open("https://www.linkedin.com/in/ethan-bokam%C3%A9-0b59a430b"))    # Pour créer un lien hypertext


app.mainloop()

