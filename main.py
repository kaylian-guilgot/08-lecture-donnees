"""Programme qui permet de manipuler un fichier"""
#### Imports et définition des variables globales
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, "r", encoding="utf-8") as f:
        lignes = f.readlines()
    return [[int(x) for x in ligne.strip().split(";")] for ligne in lignes]

def get_list_k(data, k):
    """retourne la k-ème liste de data

    Args:
        data (list[list[int]]): Liste à deux dimension d'entier
        k (int): indice de la liste à retourner

    Returns:
        list: k-ème liste de data d'entier
    """
    l = data[k]
    return l

def get_first(l):
    """retourne le premier élément de l

    Args:
        l (list[Type]): Liste qu'on va manipuler

    Returns:
        Type: premier élément de l
    """
    return l[0]

def get_last(l):
    """retourne le dernier élément de l

    Args:
        l (list[Type]): Liste qu'on va manipuler

    Returns:
        Type: dernier élément de l
    """
    return l[-1]

def get_max(l):
    """retourne la plus grande valeur de l

    Args:
        l (list[type]): Liste qu'on va manipuler

    Returns:
        Type: plus grande élément de l
    """
    return max(l)

def get_min(l):
    """retourne la plus petite valeur de l

    Args:
        l (list[type]): Liste qu'on va manipuler

    Returns:
        Type: plus petite élément de l
    """
    return min(l)

def get_sum(l):
    """retourne la somme des éléments de l

    Args:
        l (list[type]): Liste qu'on va manipuler

    Returns:
        Type: somme des éléments de l
    """
    return sum(l)

#### Fonction principale

def main():
    """Appel aux fonctions secondaires pour vérifier leur bon fonctionnement"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))

if __name__ == "__main__":
    main()
