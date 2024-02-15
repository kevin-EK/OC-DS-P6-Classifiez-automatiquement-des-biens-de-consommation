# OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation
La marketplace e-commerce de "Place de marché" permet à des vendeurs de proposer des articles à des acheteurs en postant une photo et une description. 
L'attribution de la catégorie d'un article est effectuée manuellement par les vendeurs, ce qui peut être peu fiable. 
Problématique :
Pour améliorer l'expérience utilisateur, il est donc nécessaire d'automatiser cette tâche en créant un moteur de classification d'articles basé sur une image et une description. 
La mission est de réaliser une étude de faisabilité pour ce moteur de classification, en explorant les données et les différents modèles pour trouver la solution la plus adaptée, en regroupant automatiquement des produits de même catégorie à travers cette approche.

# ETAPE 1 : Classification non supervisée

## A. Traitement des données textuelles
  - Pré-traitement (tokens,stop_words, lemmatizer,..)
  - Bag Of Words & Words Embedding:
  - TF / Tf-idf
  - Word2Vec / Glove / FastText
  - Bert / Elmo /USE
  - Clustering & Visualisation dans espace réduit (2D)
## B. Traitement des données visuelles
  - Retraitement des images (contraste, passage en gris, filtrage du bruit, floutage, etc...)
  - Extraction de Features:
  - Bag of images: ORB-SIFT-SURF
  - Transfert learning (CNN: VGG16)
  - Clustering & Visualisation dans espace réduit (ACP et TSNE)

# ETAPE 2 : Classification supervisée
  - Data augmentation
  - Transfert learning (CNN: VGG16)
  - Evaluation Modèles (score – temps d’exécution- Facilité de MEP, etc...)


    
