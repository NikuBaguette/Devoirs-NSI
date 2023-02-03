# exo 1 (non demandé)

def recherche(lettre, mot):
    n = 0
    for v in mot:
        if v == lettre:
            n += 1
    return n

print(recherche('e', "sciences")) # Doit être 2
print(recherche('i',"mississippi")) # Doit être 4
print(recherche('a',"mississippi")) # Doit être 0


# rendu monnaie recursif
Pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = Pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, i+1)

print(rendu_glouton(68,[],0)) # Doit être [50, 10, 5, 2, 1]
print(rendu_glouton(291,[],0)) # Doit être [100, 100, 50, 20, 20, 1]
