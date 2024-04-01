import Projet
import util
from tkinter import *

window = Tk()
window.title("Gestion de bibliotheque")
window.config(background='#dee5dc')
window.geometry("500x480")



##################################
##################################

def afficheLivreLibreQuand():
    """
    Cette fonction permet d'afficher dans combien de temps un livre sera empruntable.
    
    (Utiliser par livreLibreQuandButton)
    """
    nbJour = str(Projet.livreLibreQuand(livreEntry.get()))
    livreEntry.delete(0,END)
    if nbJour != "-1":
        if nbJour == "0":
            livreEntry.insert(0,"Livre libre dés maintenant")
        else:
            livreEntry.insert(0,"Livre libre dans "+nbJour+" jours")
    else:
        livreEntry.insert(0,"Référence incorrect")

        
## sous frame livre libre quand
livreLibreQuandBox = Frame(window,bg="#90B5F4")
livreLibreQuandBox.grid(row=0,column=0,padx=10,pady=5,ipadx=10)


### texte box bouton livrelivrequand
textLivreLibreQuand = Label(livreLibreQuandBox,text="Quelle est la reference du livre ?",bg="#90B5F4")
textLivreLibreQuand.pack()
### input reference livre chercher
livreEntry = Entry(livreLibreQuandBox)
livreEntry.insert(0,"Ex : 13")
livreEntry.pack(fill=X)
### bouton livre libre quand
livreLibreQuandButton = Button(livreLibreQuandBox,text="Livre libre Quand ?",bg="#90B5F4",command=afficheLivreLibreQuand)
livreLibreQuandButton.pack()



##################################
##################################




def afficheLivresARendre():
    """
    Cette fonction permet d'ouvrir un nouvelle fenetre tkinter avec la liste detaillée des livres empruntés par un adherent.
    
    (Utiliser par livresARendreButton)
    """
    refAdherent = adherentEntry.get() # recuperation de reference d'adherent
    if any((dictadherent["Référence "]==refAdherent) for dictadherent in Projet.listeDictAdherent) :
        windowTextLivreARendre = Tk() # fenetre d'affichage des livres empruntés
        windowTextLivreARendre.title("Liste des livres à emprunté par l'adherent "+ refAdherent)
        windowTextLivreARendre.geometry("500x360")
        text = Text(windowTextLivreARendre) # texte affiché
        listeCoupleLivreRetour = Projet.livresARendre(refAdherent)
        for coupleLivreRetour in listeCoupleLivreRetour :
            text.insert(END,"- le livre de référence "+str(coupleLivreRetour[0])+" est à rendre dans "+str(coupleLivreRetour[1])+" jours maximum \n\n")
    
    
        text.pack()
        windowTextLivreARendre.mainloop()
        
    else:
        adherentEntry.delete(0,END)
        adherentEntry.insert(0,"Référence incorrect")
        
        

## sous frame livres A Rendre
livresARendreBox = Frame(window,bg="#6085C4")
livresARendreBox.grid(row=0,column=1)


### texte box bouton livres A Rendre
textlivresARendre = Label(livresARendreBox,text="Quelle est la référence de l'adherent ?",bg="#6085C4")
textlivresARendre.pack()
### input reference adherent chercher
adherentEntry = Entry(livresARendreBox)
adherentEntry.insert(0,"Ex : 5")
adherentEntry.pack(fill=X)
### bouton livres A Rendre
livresARendreButton = Button(livresARendreBox,text="Liste des livres à rendre ?",bg="#6085C4",command=afficheLivresARendre)
livresARendreButton.pack()


##################################
##################################


def afficheLivresDispo():
    """
    Cette fonction permet d'ouvrir un nouvelle fenetre tkinter avec la liste detaillé des livres empruntés par un adherent.
    
    (Utiliser par livresARendreButton)
    """
    
    windowTextLivreDispo = Tk() # fenetre d'affichage des livres disponibles
    windowTextLivreDispo.title("Liste des livres disponibles")
    windowTextLivreDispo.geometry("625x360")
    textLivreDispo = Text(windowTextLivreDispo) # texte affiché
    listeLivreDispo = Projet.livresDispo()
    for livre in listeLivreDispo :
        textLivreDispo.insert(END,"- Le livre "+ livre["Titre"] +" de référence "+str(livre["Référence"])+"\n\n")
    
    
    textLivreDispo.pack()
    windowTextLivreDispo.mainloop()



## sous frame livresDispo
livresDispoBox = Frame(window,bg="#6085C4")
livresDispoBox.grid(row=1,column=0)


### bouton livres Dispo
livresDispoButton = Button(livresDispoBox,text="Liste des livres disponibles",bg="#6085C4" ,command=afficheLivresDispo)
livresDispoButton.pack()



##################################
##################################


def createNewAdherent():
    """

    
    """
    
    def actionVerificationButton():
        unlockCreation = True
        if Projet.uniqueAdherentReference(newAdherentRefEntry.get()) and newAdherentRefEntry.get().isnumeric():
            newAdherentRefEntry.config({"background": "Green"})
        else :
            unlockCreation = False
            newAdherentRefEntry.config({"background": "Red"})
            
        if newAdherentNomEntry.get().isalpha() :
            newAdherentNomEntry.config({"background": "Green"})
        else :
            unlockCreation = False
            newAdherentNomEntry.config({"background": "Red"})
                
        if newAdherentPrenomEntry.get().isalpha():
            newAdherentPrenomEntry.config({"background": "Green"})
        else :
            unlockCreation = False
            newAdherentPrenomEntry.config({"background": "Red"})
            
        if util.bonFormatDate(newAdherentDDNEntry.get()) :
            newAdherentDDNEntry.config({"background": "Green"})
        else :
            unlockCreation = False
            newAdherentDDNEntry.config({"background": "Red"})
            
                   
        if unlockCreation:
            createAdherentButton.pack()
        elif createAdherentButton in newAdherentButtonBox.winfo_children():
            createAdherentButton.pack_forget()
            
    def actionAddAdherentButton():
        Projet.addAdherent({'Référence ': newAdherentRefEntry.get() , 'Nom': newAdherentNomEntry.get() , 'Prénom': newAdherentPrenomEntry.get() , 'Date de naissance': newAdherentDDNEntry.get() })
    
    
    
    
    
    
    windowCreateAdherent = Tk() # fenetre de creation d'adherent
    windowCreateAdherent.title("Création d'un nouvel adherent")
    windowCreateAdherent.config(background='#dee5dc')
    windowCreateAdherent.geometry("320x360")
    ##########
    # Référence
    
    ## sous frame récuperation de la référence du nouvel adherent
    newAdherentRefBox = Frame(windowCreateAdherent,bg="#90B5F4")
    newAdherentRefBox.grid(row=0,column=0,pady=10,padx=10)
    
    ### texte récuperation référence new adherent
    refNewAdherent = Label(newAdherentRefBox,text="Quelle est la référence de l'adherent ?",bg="#90B5F4")
    refNewAdherent.pack(fill=X)
    
    ### saisi reference new adherent 
    newAdherentRefEntry = Entry(newAdherentRefBox)
    newAdherentRefEntry.insert(0,"Ex: 1523")
    newAdherentRefEntry.pack(fill=X)
    
    ##########
    # Nom
    
    ## sous frame récuperation du Nom du nouvel adherent
    newAdherentNomBox = Frame(windowCreateAdherent,bg="#6085C4")
    newAdherentNomBox.grid(row=1,column=0,pady=10,padx=10)
    
    ### texte récuperation nom new adherent
    nomNewAdherent = Label(newAdherentNomBox,text="Quel est le nom de l'adherent ?",bg="#6085C4")
    nomNewAdherent.pack(fill=X)
    
    ### saisi nom new adherent 
    newAdherentNomEntry = Entry(newAdherentNomBox)
    newAdherentNomEntry.insert(0,"Ex: Dupont")
    newAdherentNomEntry.pack(fill=X)

    ##########
    # Prenom
    
    ## sous frame récuperation du Prenom du nouvel adherent
    newAdherentPrenomBox = Frame(windowCreateAdherent,bg="#90B5F4")
    newAdherentPrenomBox.grid(row=2,column=0,pady=10,padx=10)
    
    ### texte récuperation Prenom new adherent
    prenomNewAdherent = Label(newAdherentPrenomBox,text="Quel est le prénom l'adherent ?",bg="#90B5F4")
    prenomNewAdherent.pack(fill=X)
    
    ### saisi Prenom new adherent 
    newAdherentPrenomEntry = Entry(newAdherentPrenomBox)
    newAdherentPrenomEntry.insert(0,"Ex: Homer")
    newAdherentPrenomEntry.pack(fill=X)

    ##########
    # Date de naissance
    
    ## sous frame récuperation de la Date de naissance du nouvel adherent
    newAdherentDDNBox = Frame(windowCreateAdherent,bg="#6085C4")
    newAdherentDDNBox.grid(row=3,column=0,pady=10,padx=10)
    
    ### texte récuperation Date de naissance new adherent
    dDNNewAdherent = Label(newAdherentDDNBox,text="Quelle est la date de naissance de l'adherent ?",bg="#6085C4")
    dDNNewAdherent.pack()
    
    ### saisi Date de naissance new adherent 
    newAdherentDDNEntry = Entry(newAdherentDDNBox)
    newAdherentDDNEntry.insert(0,"Ex: 15/11/2005")
    newAdherentDDNEntry.pack(fill=X)

    ########
    # Buttons
    
    ## sous frame button verification des donnees nouvel adherent
    newAdherentVerifButtonBox = Frame(windowCreateAdherent,bg="#6085C4")
    newAdherentVerifButtonBox.grid(row=4,column=0,pady=10,padx=10)
    
    verifAdherentButton = Button(newAdherentVerifButtonBox,text="Verification des données de l'adherent",bg="#90B5F4",padx=20,
                                  command=actionVerificationButton)
    verifAdherentButton.pack()
    
    
    ## sous frame button creation du nouvel adherent
    
    newAdherentButtonBox = Frame(windowCreateAdherent,bg="#6085C4")
    newAdherentButtonBox.grid(row=5,column=0,pady=10,padx=10)
    
    createAdherentButton = Button(newAdherentButtonBox,text="Création d\'adherent",bg="#90B5F4",padx=20,
                                  command=actionAddAdherentButton)
    

    windowCreateAdherent.mainloop()

## sous frame creation adherent
addAdherentBox = Frame(window,bg="#90B5F4")
addAdherentBox.grid(row=1,column=1,pady=10)


### bouton creation adherent
addAdherentButton = Button(addAdherentBox,text="Création et ajout d\'adherent",bg="#90B5F4",padx=20,command=createNewAdherent)
addAdherentButton.pack()



################################
################################





def empruntLivre():
    """
    Cette fonction permet de faire emprunter un livre par un adherent.
    
    """
    
    def actionVerificationEmpruntButton():
        unlockCreation = True
        if not(Projet.uniqueAdherentReference(adherentEmprunteurRefEntry.get())) and adherentEmprunteurRefEntry.get().isnumeric():
            adherentEmprunteurRefEntry.config({"background": "Green"})
        else :
            unlockCreation = False
            adherentEmprunteurRefEntry.config({"background": "Red"})
        listeRefLivreDispo = [dispo["Référence"] for dispo in Projet.livresDispo() ]
        if livreEmpruntRefEntry.get().isnumeric() and livreEmpruntRefEntry.get() in listeRefLivreDispo:
            livreEmpruntRefEntry.config({"background": "Green"})
        else :
            unlockCreation = False
            livreEmpruntRefEntry.config({"background": "Red"})
            
        if unlockCreation:
            empruntButton.pack()
            
        elif empruntButton in empruntButtonBox.winfo_children():
            empruntButton.pack_forget()
            
    def actionEmpruntButton():
        Projet.emprunt(adherentEmprunteurRefEntry.get(),livreEmpruntRefEntry.get())
        Projet.adherentAddEmprunt(adherentEmprunteurRefEntry.get(),livreEmpruntRefEntry.get())
    
    
    windowEmpruntLivre = Tk() # fenetre d'emprunt de livre
    windowEmpruntLivre.title("Emprunt d'un livre")
    windowEmpruntLivre.config(background='#dee5dc')
    windowEmpruntLivre.geometry("490x400")
    
    
    ##################
    # Récuperer les deux Références
    
    
    ###########
    ### adherent
    
    ## sous frame récuperation de la référence de l'adherent qui emprunte
    adherentEmprunteurRefBox = Frame(windowEmpruntLivre,bg="#6085C4")
    adherentEmprunteurRefBox.grid(row=0,column=0,pady=10,padx=10)
    
    ### texte récuperation référence new adherent
    refAdherentEmprunteur = Label(adherentEmprunteurRefBox,text="Quelle est la référence de l'adherent ?",bg="#6085C4")
    refAdherentEmprunteur.pack(fill=X)
    
    ### saisi reference new adherent 
    adherentEmprunteurRefEntry = Entry(adherentEmprunteurRefBox)
    adherentEmprunteurRefEntry.insert(0,"Ex: 1523")
    adherentEmprunteurRefEntry.pack(fill=X)
    
    
    
    def fenetreSelectionListeAdherent():
        """
        Cette fonction permet d'ouvrir un nouvelle fenetre tkinter avec la liste des adherents.
        Un double clic sur un adherent permet de fermer la fenetre et selectionner la reference de ce dernier pour emprunt
        """
        def selection_adherent(event):
            cs = adherentLb.curselection()
            indexAdherent = adherentLb.index(cs[0]) # le i eme element de la liste box
            refAdherent = Projet.listeDictAdherent[adherentLb.index(cs[0])]["Référence "]  # ref de l'adherent selectionné 
            adherentEmprunteurRefEntry.delete(0,END)
            adherentEmprunteurRefEntry.insert(0,refAdherent)
            windowSelectionListeAdherent.destroy()
            
        windowSelectionListeAdherent = Tk() # fenetre d'emprunt de livre
        windowSelectionListeAdherent.title("Selectionne l'adherent")
        windowSelectionListeAdherent.config(background='#dee5dc')
        windowSelectionListeAdherent.geometry("720x400")
        # Creating Listbox
        adherentLb = Listbox(windowSelectionListeAdherent,height=20)
        # Inserting items in Listbox
        for i in range(len(Projet.listeDictAdherent)): # pour tout les i de 0 a nombre adherent -1
            adherentLb.insert(i, "L\'adherent "+str(Projet.listeDictAdherent[i]["Nom"])+" "+str(Projet.listeDictAdherent[i]["Prénom"])+", de réference "+ str(Projet.listeDictAdherent[i]["Référence "]))
           
        # Binding double click with left mouse
        # button with go function
        adherentLb.bind('<Double-1>', selection_adherent)
        adherentLb.pack(fill=X)
        
    ##### sous frame button aide récuperation de la référence de l'adherent qui emprunte
    #
    listeAdherentButtonBox = Frame(windowEmpruntLivre,bg="#6085C4")
    listeAdherentButtonBox.grid(row=0,column=1,pady=10,padx=10)

    afficherListAdherentButton = Button(listeAdherentButtonBox,text="Selectionner un adherent",bg="#90B5F4",padx=20,command=fenetreSelectionListeAdherent)
    afficherListAdherentButton.pack()
    
    #######
    
    
    def fenetreSelectionListeLivre():
        """
        Cette fonction permet d'ouvrir une nouvelle fenetre tkinter avec la liste des adherents.
        Un double clic sur un adherent permet de fermer la fenetre et selectionner la reference de ce dernier pour emprunt
        """
        def selection_Livre(event):
            cs = livreLb.curselection()
            indexLivre = livreLb.index(cs[0]) # le i eme element de la liste box
            refLivre = Projet.livresDispo()[livreLb.index(cs[0])]["Référence"]  # ref du livre selectionné 
            livreEmpruntRefEntry.delete(0,END)
            livreEmpruntRefEntry.insert(0,refLivre)
            windowSelectionListeLivre.destroy()
            
        windowSelectionListeLivre = Tk() # fenetre d'emprunt de livre
        windowSelectionListeLivre.title("Selectionne le livre")
        windowSelectionListeLivre.config(background='#dee5dc')
        windowSelectionListeLivre.geometry("720x400")
        # Creating Listbox
        livreLb = Listbox(windowSelectionListeLivre,height=20)
        # Inserting items in Listbox
        listeLivreDisponible = Projet.livresDispo()
        for i in range(len(listeLivreDisponible)): # pour tout les i de 0 a nombre adherent -1
            livreLb.insert(i, "Le livre "+str(listeLivreDisponible[i]["Titre"])+", écrit par "+str(listeLivreDisponible[i]["Auteur nom"])+", de référence : "+ str(listeLivreDisponible[i]["Référence"]))
           
        # Binding double click with left mouse
        # button with go function
        livreLb.bind('<Double-1>', selection_Livre)
        livreLb.pack(fill=X)
    
    ##### sous frame button aide récuperation de la référence du livre qui va etre emprunté
    #
    listeLivreButtonBox = Frame(windowEmpruntLivre,bg="#6085C4")
    listeLivreButtonBox.grid(row=1,column=1,pady=10,padx=10)

    afficherListLivreButton = Button(listeLivreButtonBox,text="Sélectionner un livre",bg="#6085C4",padx=20,command=fenetreSelectionListeLivre)
    afficherListLivreButton.pack()
    
    ## sous frame récuperation de la référence du livre que l'adherent emprunte
    livreEmpruntRefBox = Frame(windowEmpruntLivre,bg="#90B5F4")
    livreEmpruntRefBox.grid(row=1,column=0,pady=10,padx=10)
    
    ### texte récuperation référence new adherent
    refLivreEmprunt = Label(livreEmpruntRefBox,text="Quelle est la référence du livre ?",bg="#90B5F4")
    refLivreEmprunt.pack(fill=X)
    
    ### saisi reference new adherent 
    livreEmpruntRefEntry = Entry(livreEmpruntRefBox)
    livreEmpruntRefEntry.insert(0,"Ex: 153")
    livreEmpruntRefEntry.pack(fill=X)
    
    



    ########
    # Buttons
    
    ## sous frame button verification des reference pour emprunt
    empruntVerifButtonBox = Frame(windowEmpruntLivre,bg="#6085C4")
    empruntVerifButtonBox.grid(row=3,column=0,pady=10,padx=10)
    
    verifEmpruntButton = Button(empruntVerifButtonBox,text="Vérification des références",bg="#6085C4",padx=20,
                                  command=actionVerificationEmpruntButton)
    verifEmpruntButton.pack()
    
    
    ## sous frame button emprunt
    
    empruntButtonBox = Frame(windowEmpruntLivre,bg="#90B5F4")
    empruntButtonBox.grid(row=3,column=1,pady=10,padx=10)
    
    empruntButton = Button(empruntButtonBox,text="Confirmer l'emprunt",bg="#90B5F4",padx=20,
                                  command=actionEmpruntButton)
    
    windowEmpruntLivre.mainloop()










## sous frame emprunt Livre
empruntBox = Frame(window,bg="#90B5F4")
empruntBox.grid(row=2,column=0,pady=10)


### bouton emprunt Livre
empruntButton = Button(empruntBox,text="Emprunter un Livre",bg="#90B5F4",padx=20,command=empruntLivre)
empruntButton.pack()




## sous frame afficher liste emprunt
addEmpruntListBox = Frame(window,bg="#6085C4")
addEmpruntListBox.grid(row=2,column=1,pady=10)


### bouton afficher liste emprunt
addEmpruntListButton = Button(addEmpruntListBox,text="Ajouter les listes d'emprunt",bg="#6085C4",padx=20,command=Projet.listeAdherentSetEmprunt)
addEmpruntListButton.pack()






##Affichage window
window.mainloop()
