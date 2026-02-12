"""Module providing the logic of the 2048 game"""

import random, copy
from typing import List, Tuple

TAILLE:int = 4


# ==========================================================
# 🎯 FONCTION PUBLIQUE (API POUR L’INTERFACE)
# ==========================================================

def nouvelle_partie() -> Tuple[List[List[int]], int]:
    """
    Crée une nouvelle partie du jeu 2048.

    :return: Une grille TAILLExTAILLE initialisée avec deux tuiles, ainsi que le score à 0.
    :rtype: Tuple[List[List[int]], int]
    """
    plateau =_creer_plateau_vide()
    plateau2 = _ajouter_tuile(plateau)
    plateau3 = _ajouter_tuile(plateau2)
    return plateau3, 0

def jouer_coup(plateau: List[List[int]], direction: str) -> tuple[List[List[int]], int, bool]:
    """
    Effectuer un mouvement sur le plateau.

    :param plateau: Une grille TAILLExTAILLE du jeu.
    :type plateau: List[List[int]]
    :param direction: La direction du déplacement : 'g' (gauche), 'd' (droite), 'h' (haut), 'b' (bas).
    :type direction: str
    :return: Retourne un tuple (nouveau_plateau, points, est_fini).
    :rtype: tuple[List[List[int]], int, bool]
    """

    raise NotImplementedError("Fonction jouer_coup non implémentée.")

# ==========================================================
# 🔒 FONCTIONS PRIVÉES (LOGIQUE INTERNE)
# ==========================================================

def _creer_plateau_vide() -> List[List[int]]:
    """
    Crée une grille TAILLExTAILLE remplie de zéros.
    :return: Une grille vide.
    :rtype: List[List[int]]
    """
    return [[0 for _ in range(TAILLE)] for _ in range(TAILLE)]


def _get_cases_vides(plateau: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Retourne les coordonnées des cases vides sous forme d'une liste de coordonnées

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Une liste de coordonnées
    :rtype: List[Tuple[int, int]]
    """
    return [(i,j) for i in range(len(plateau)) for j in range(len(plateau)) if plateau[i][j]==0]
    # liste = []
    # for i in range(len(plateau)):
    #     for j in range(len(plateau)):
    #         if plateau[i][j] == 0:
    #             liste.append((i,j))
    # return liste
# 

def _ajouter_tuile(plateau: List[List[int]]) -> List[List[int]]:
    """
    Ajoute une tuile de valeur 2 sur une case vide.

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Une nouvelle grille avec une tuile ajoutée.
    :rtype: List[List[int]]
    """
    liste = _get_cases_vides(plateau)
    (i,j)=random.choice(liste)
    nouveau_plateau = copy.deepcopy(plateau)
    nouveau_plateau[i][j]= 2
    return nouveau_plateau
    



def _supprimer_zeros(ligne: List[int]) -> List[int]:
    """
    Supprime les zéros d'une ligne.

    :param ligne: Une ligne de la grille.
    :type ligne: List[int]
    :return: La ligne sans zéros.
    :rtype: List[int]
    """
    #return [value for value in ligne if value==0]

    result = []
    for value in ligne:
        if value != 0:
            result.append(value)
    return result

def _fusionner(ligne: List[int]) -> Tuple[List[int], int]:
    """
    Fusionne les valeurs identiques consécutives d'une ligne.

    :param ligne: Une ligne sans zéros.
    :type ligne: List[int]
    :return: La ligne après fusion, les points gagnés
    :rtype: Tuple[List[int], int]
    """
    liste_fusionnee = []
    i = 0
    points = 0
    
    while i < len(ligne):
        if (i+1)< len(ligne) and ligne[i]==ligne[i+1]:
            fusion = ligne[i] + ligne[i+1]
            points += fusion
            liste_fusionnee.append(fusion)
            i += 2
        else:
            liste_fusionnee.append(ligne[i])
            i += 1
    return liste_fusionnee, points


def _completer_zeros(ligne: List[int]) -> List[int]: # ajouter les annotations de type
    """
    complète les zéros manquant d'une ligne après un déplacement

    :param ligne: Une ligne sans zéros.
    :type ligne: List[int]
    :return: la ligne avec des zéros
    :rtype: List[int]
    """
    liste = ligne
    while len(liste)<TAILLE:
        liste.append(0)
    return liste
        


def _deplacer_gauche(plateau: List[List[int]]) -> List[List[int]] : # ajouter les annotations de type
    """
    déplace à gauche

    :param plateau: Une liste de listes d'entiers .
    :type plateau: List[List[int]]
    :return: le nouveau plateau modifié, les nouveaux points
    :rtype: Tuple(List[List[int]],[int]) 
    """
    nouveau_plateau = []
    nouveaux_points = 0
    for i in range(len(plateau)):
        ligne_sans_zeros = _supprimer_zeros(plateau[i])
        ligne_fusionnee, points = _fusionner(ligne_sans_zeros)
        nouveaux_points += points
        ligne_finale = _completer_zeros(ligne_fusionnee)
        nouveau_plateau.append(ligne_finale)
    return nouveau_plateau, nouveaux_points

def _inverser_lignes(plateau: List[List[int]]) -> List[List[int]]: # ajouter les annotations de type
    """
    inverse chaque ligne du plateau pour un futur déplacement à droite

    :param plateau: Une liste de listes d'entiers .
    :type plateau: List[List[int]]
    :return: le nouveau plateau avec les lignes inversées
    :rtype: List[List[int]]
    """
    
    return [ligne[::-1] for ligne in plateau]
    
    
    #nouv_plateau = []
    #for liste in plateau:
    #    ligne = []
    #    for i in range(len(ligne)-1,-1,-1):
    #le deuxième -1 est là pour inclure la dernière valeur (ici à l'envers)
    #        ligne.append(ligne[i])
    #    nouv_plateau.append(ligne)
    #return nouv_plateau



def _deplacer_droite(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers la droite en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :type plateau: List[List[int]]
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    :rtype: Tuple[List[List[int]], int]
    """
    plateau1 = _inverser_lignes(plateau)
    plateau2, score = _deplacer_gauche(plateau1)
    plateau3 = _inverser_lignes(plateau2)
    return plateau3, score


def _transposer(plateau): # ajouter les annotations de type
    """
    Inverse les lignes et les colonnes dans le plateau 

    :param plateau: La grille actuelle du jeu.
    :type plateau: List[List[int]]
    :return: le plateau transposé
    :rtype: List[List[int]
    """
    nouv_plateau = []
    for i in range(len(plateau)):
        ligne=[]
        for j in range(len(plateau)):
            ligne.append(plateau[j][i])
        nouv_plateau.append(ligne)
    return nouv_plateau

def _deplacer_haut(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers le haut en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    """
    raise NotImplementedError("Fonction _deplacer_haut non implémentée.")


def _deplacer_bas(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers le bas en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    """
    raise NotImplementedError("Fonction _deplacer_bas non implémentée.")

def _partie_terminee(plateau: List[List[int]]) -> bool:
    """
    DOCSTRING À ÉCRIRE
    """
    # Partie non terminee si il y a des cases vides
    # Partie non terminee si il y a des fusions possibles (horizontale ou verticale)
    # Sinon c'est vrai

    raise NotImplementedError("Fonction _partie_terminee non implémentée.")