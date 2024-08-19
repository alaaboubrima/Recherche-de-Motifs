# French

### Table des Suffixes

**Description**: Ce projet, mené dans le cadre de mon Master 1 en Bioinformatique, vise à implémenter des algorithmes de traitement de texte en Python, basés sur la construction et l'utilisation de tables de suffixes. Les différentes opérations sont réalisées à travers un menu à choix multiples, permettant de répondre à des questions spécifiques liées à un texte donné, T.

**Construction de la Table des Suffixes (TS)**: Création de la table des suffixes pour le texte T (TS) et affichage de cette table.

**Recherche de Motif avec la Table des Suffixes (TS)**: Recherche d'un motif M dans le texte T en utilisant la table des suffixes TS.

**Construction de la Table des Préfixes Communs (HTR)**: Construction de la table HTR pour le texte T, en montrant le préfixe commun entre deux suffixes consécutifs, suivie de l'affichage de la table HTR.

**Utilisation de TS et HTR pour Trouver et Afficher**:
- Les plus longs facteurs répétés dans le texte.
- Les facteurs qui se répètent au moins 3 fois.

**Construction de l'Inverse de la Table des Suffixes (ITS)**: Création de l'inverse de la table des suffixes (ITS) pour le texte T, et affichage de cette inverse.

**Détermination des Plus Courts Facteurs Uniques**: Construction de la table LgCandidat et détermination des plus courts facteurs uniques du texte.

**Détermination des Répétitions Super-Maximales**: Identification des répétitions super-maximales présentes dans le texte.

**Retrouver le Plus Long Facteur Commun entre Deux Textes (T1 et T2)**: Utilisation des structures TS et HTR pour retrouver le plus long facteur commun entre deux textes, T1 et T2.

**Tests et Mesures de Performance**: Réalisation de plusieurs tests sur des textes de tailles variables (100, 200, 600, 1000, 2000, 5000, ...) avec enregistrement des temps d'exécution afin d'évaluer les performances du programme.


# English

### Suffix Array Project

**Description**: This project, completed as part of my Master’s in Bioinformatics, involves implementing text processing algorithms in Python based on the construction and use of suffix arrays. Various operations are executed through a multi-choice menu to answer specific questions regarding a given text T.

**Construction of the Suffix Array (SA)**: Building the suffix array of text T (SA). Displaying the suffix array.

**Pattern Search Using the Suffix Array (SA)**: Searching for a pattern M in the text using the suffix array SA.

**Construction of the Longest Common Prefix Table (LCP)**: Building the LCP table of T by showing the common prefix between two consecutive suffixes. Displaying the LCP table.

**Using SA and LCP to Find and Display**:
- The longest repeated substring(s) in the text.
- Substrings that repeat at least 3 times.

**Construction of the Inverse Suffix Array (ISA)**: Building the inverse ISA of the suffix array of T. Displaying the inverse ISA.

**Determination of the Shortest Unique Substrings**: Constructing the Candidate Length table. Determining the shortest unique substrings of the text.

**Determination of Super-Maximal Repeats**: Determining the super-maximal repeats in the text.

**Finding the Longest Common Substring Between Two Texts (T1 and T2)**: Finding the longest common substring between two texts T1 and T2 using the SA and LCP structures.

**Tests and Performance Measurements**: Conducting several tests on texts of varying sizes (100, 200, 600, 1000, 2000, 5000, ...) by recording execution time to evaluate the program's performance.