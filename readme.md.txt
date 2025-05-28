Comment installer et utiliser notre Analyseur


Le langage de programmation étant Python, le code fourni ne nécessite pas d’être compilé avant d’être exécuté. Après avoir renseigné les noms des fichiers d'entrées et de sorties dans le fichier main.py, il suffit d’exécuter ce dernier avec la commande python3.7 main.py ou en utilisant un IDE dédié.




Description du code du projet


Le langage de programmation requis pour l’utilisation de l’analyseur est Python dans sa version Python 3.7. L’exécutable est le fichier main.py présent dans le dossier principal de l’archive.
Pour exécuter le programme, il suffit de renseigner le nom du fichier contenant la trame et le nom du fichier de sortie (le résultat de l’analyse). 


L’architecture globale du code est composé de:
-Un répertoire Trames contenant au format .txt, les trames à analyser ;
-Un répertoire Protocols contenant: 
-Un fichier de configuration par protocole analysable(ARP, IP, Ethernet, ICMP, TCP, HTTP);
-Un fichier analyzer.py contenant un code plus ou moins générique permettant l’analyse de tous les protocoles analysables;
-Un fichier Transformers.py qui contient les fonctions de transformations des octets lus;
-Le fichier exécutable main.py;
-Un fichier utils.py contenant des fonctions les fonctions de lecture de trames et d’écriture de l’analyse;