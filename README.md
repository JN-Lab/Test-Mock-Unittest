# Test-Mock-Unittest
Ce dépôt est associé à un article que vous pouvez retrouver à cette address: (en construction)
Il a pour objectif de décrire le fonctionnement des mockes via le module unittest.

## Description
Ce dépôt contient plusieurs fichiers:
* app.py : le programme à tester
* test_without.py : une classe test qui modifie le retour d'une méthode sans utiliser l'objet Mock ou le décorateur patch du module unittest
* test_mock.py : une classe test qui utilise l'objet Mock du module unittest
* test_patch_1.py : une classe test qui utilise le décorateur patch du module unittest
* test_patch_2.py : une classe test qui utilise également le décorateur patch du module unittest
* test_patch_error.py : une classe test qui utilise le décorateur patch du module unittest et qui ne valide volontairement pas le test

## Installation
Une fois le dépôt cloné, pour lancer le programme, il suffit de lancer la commande suivante:
```
python3 app.py
```

Pour lancer les tests, il suffit de lancer la commande suivante:
```
python3 -m unittest -v
```


