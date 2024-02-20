# OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation
La marketplace e-commerce de "Place de marché" permet à des vendeurs de proposer des articles à des acheteurs en postant une photo et une description. 
L'attribution de la catégorie d'un article est effectuée manuellement par les vendeurs, ce qui peut être peu fiable. 
Problématique :
Pour améliorer l'expérience utilisateur, il est donc nécessaire d'automatiser cette tâche en créant un moteur de classification d'articles basé sur une image et une description. 
La mission est de réaliser une étude de faisabilité pour ce moteur de classification, en explorant les données et les différents modèles pour trouver la solution la plus adaptée, en regroupant automatiquement des produits de même catégorie à travers cette approche.

# ETAPE 1 : Classification non supervisée

![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/e43acf51-d5b9-469a-8006-a7d7efbc3294)


## A. Traitement des données textuelles
  - Pré-traitement (tokens,stop_words, lemmatizer,..)
  - Bag Of Words & Words Embedding:
  - TF / Tf-idf
  - Word2Vec / Glove / FastText
  - Bert / Elmo /USE
  - Clustering & Visualisation dans espace réduit (2D)

![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/dd2e2406-ce10-4670-a6b6-38b271f128a0)

![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/bfd432fb-e581-4a65-8050-ec61cde65e35)

![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/62053b31-c46f-4359-862e-6f489d36773e)

![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/19e82167-a13f-41f3-9ee7-9d2722b00fef)

![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/3d977980-56dd-4831-8e7d-95273889619e)

## B. Traitement des données visuelles
  - Retraitement des images (contraste, passage en gris, filtrage du bruit, floutage, etc...)
  - Extraction de Features:
  - Bag of images: ORB-SIFT-SURF
  - Transfert learning (CNN: VGG16)
  - Clustering & Visualisation dans espace réduit (ACP et TSNE)

![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/02d183f4-490c-4e58-846f-523280f8d537)

![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/19fc8048-1f9b-4c07-8c4b-ad535ae392bb)

![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/1d4e7ce2-288b-4996-aa36-14d6ebc94802)


# ETAPE 2 : Classification supervisée
  - Data augmentation
  - Transfert learning (CNN: VGG16)
  - Evaluation Modèles (score – temps d’exécution- Facilité de MEP, etc...)

![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/0412eeeb-a3af-4923-b588-dfa43149d41c)

![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/b45b5f44-7f1e-4d9e-bd7a-6600082f08a1)

![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/a8532ced-f087-48a3-a1aa-699fa1dc8883)
    
![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/c622f09d-278f-42d8-9b94-44db62130636)

# ANNEXE :

## TF-IDF
![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/19bb2875-8584-45b5-b047-d3ea098a15c9)

## Word2Vec
![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/b6ff30e9-f3b3-4e9f-b015-3b3939d42d16)

## GloVe (Global Vector)
![image](https://github.com/kevin-EK/OC-DS-P6-Classifiez-automatiquement-des-biens-de-consommation/assets/69479292/e6547b0b-722e-42f5-9800-72ebd6ceeabd)

## FastText

## BERT et dérivés

## Universal Sentence Encoder 

## Latent Dirichlet Allocation

## Adjusted Rand Index

## T-SNE

## VGG16

## DETECTEUR SIFT
