# Projet de Recherche de Motifs dans un Texte

## Description

Ce projet contient des implémentations en Python de quatre algorithmes de recherche de motifs bien connus : 

Ce projet, réalisé dans le cadre de mon cursus en Master 1 Bioinformatique, vise à implémenter des algorithmes de recherche de motifs dans un texte et à analyser leur complexité théorique et expérimentale. Les algorithmes implémentés couvrent divers aspects de la recherche de motifs, et ce projet offre une contribution pratique à la compréhension et à l'application de ces algorithmes dans le domaine de la bioinformatique. 

**Boyer-Moore (BM)**, **Aho-Corasick (AC)**, **Rabin-Karp (RK)**, et **Commentz-Walter (CW)**. Chaque algorithme est codé en dur pour démontrer leur fonctionnalité dans la recherche de motifs dans un texte donné. Ces algorithmes sont largement utilisés dans diverses applications, notamment le traitement de texte, la bioinformatique, et l'exploration de données.



## Algorithmes Implémentés



### 1. Boyer-Moore (BM)
Recherche d'un seul motif M de longueur m dans un texte T de longueur n.

### 2. Aho-Corasick (AC)
Recherche multiple d'un ensemble de motifs (S1, S2, ... Sk) dans un texte T.

### 3. Rabin-Karp (RK)
Recherche multiple d'un ensemble de motifs (S1, S2, ... Sk) en utilisant 3 fonctions de hachage (filtre de Bloom).

### 4. Commentz-Walter (CW)
L'algorithme Commentz-Walter étend l'approche Boyer-Moore pour gérer plusieurs motifs à la fois. Il combine des idées des algorithmes Aho-Corasick et Boyer-Moore pour rechercher efficacement plusieurs motifs en un seul passage dans le texte.

## Comparaison des Algorithmes (Aho-Corasick et Rabin-Karp)

### Commentz-Walter (CW)
- Illustration de son déroulement sur un exemple de recherche de motifs (S1, S2, S3) dans un texte T.
- Réalisation de plusieurs tests pour comparer les performances des algorithmes [CW] et [AC].
- Analyse des résultats de test en suivant la même procédure que dans la question 2.



