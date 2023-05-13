# Scriptes de génération d'étiquettes pour l'inventaire

##  gen_inv_num.py - générateur de numéro d'inventaire

Il s'agit d'un scripte en python 3 pour construire un fichier .csv contenant le numéro d'inventaire à imprimer.

**Utilisation:** gen_inv_num.py <start_inv_num> <page_count>
<start_inv_num> est le numéro d'inventaire de départ, par exemple 2021-000-001.
<page_count> est le nombre de page (84 numéros/étiquettes par page)

**Exemple:** ./gen_inv_num.py 2021-000-001 8
Cette commande génère 8 pages en commençant par le numéro d'inventaire 2021-000-001.

**Sortie de la commande d'exemple:**
> 2021-000-001 
> 2021-000-002 
> 2021-000-003 
> ... 
> 2021-000-669 
> 2021-000-670
> 2021-000-671 
> 2021-000-672

Pour générer un fichier .csv, il suffit de rediriger le résultat dans un fichier.
**Exemple:** ./gen_inv_num.py 2021-000-001 8 > inv_num_2021_000_001-672.csv

## glabels - logiciel de création de cartes de visite et d'étiquettes

Ce logiciel est disponible dans la plupart des distributions linux, il existe aussi une version Windows.

**Comment générer des étiquettes pour le papier SUAFLS0084 ?** 

 1. Ouvrir le fichier 'qrcode.glabels' (Menu Fichier -> Ouvrir).
 2. Ensuite sélectionner le bon fichier .csv (Menu Objects -> Propriétés de fusion)
 3. Mettre le poids du papier en 200g mat sur l'imprimante de ruchonet
 4. attention le papier a un bord a 32mm et un autre a 33 (il faut l'orienter juste dans l'imprimante) le 32 mm va en bas dans l'imprimante
 3. Imprimer (Menu Imprimer ...). 
 
**NOTES IMPORTANTES:** 
Il est recommandé d'imprimer une page en papier ordinaire en faisant une croix sur la feuille pour déterminer l'orientation du papier. 
Les étiquettes du papier SUAFLS0084 ne sont pas centrées, il faut donc déterminer le sens du papier. Le coin en haut à gauche du papier est à 3.2 mm du bord depuis le haut et à 1.2 mm du bord depuis la gauche (3.3 mm du bord depuis le  bas et 1.3 mm du bord depuis la droite). 

