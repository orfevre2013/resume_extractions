from career_coach import extract_experiences


fake_resume = """
Curriculum Vitae
Informations Personnelles
Nom: John Doe
Adresse: 123 Main Street, Anytown, USA
Téléphone: (555) 123-4567
E-mail: john.doe@email.com
Date de Naissance: 10 janvier 1985
Résumé
Je suis un professionnel expérimenté avec une expertise dans le développement de logiciels innovants, la coordination de campagnes marketing réussies et une solide formation académique. J'ai travaillé dans divers secteurs, notamment la technologie et le marketing. Ma passion pour l'excellence et mon engagement envers l'efficacité m'ont permis de réussir dans mes rôles précédents. Je suis à la recherche de nouvelles opportunités passionnantes pour continuer à contribuer au succès de l'entreprise.

Expériences Professionnelles
Lead Developer - Tech Innovators
Entreprise: Tech Innovators
Lieu: San Francisco, CA
Date de Début: Mai 2015
Date de Fin: Août 2020
Type d'Emploi: Temps Plein
Salaire/Compensation: USD 120,000 par an
Références: John Smith (CTO), jsmith@email.com
Description:
En tant que Lead Developer chez Tech Innovators, j'ai dirigé une équipe de développeurs dans la création de solutions logicielles innovantes. J'ai géré l'ensemble du cycle de développement, de la conception au déploiement. J'ai collaboré avec des équipes pluridisciplinaires pour atteindre les objectifs du projet. J'ai mis en œuvre des méthodologies agiles pour une gestion de projet efficace. J'ai développé et maintenu des applications web complexes en utilisant des technologies de pointe.

Compétences:

Gestion de Projet Agile
Développement Full-Stack
Leadership d'Équipe
Méthodologies Agiles
Développement d'Applications Web
Résultats Accomplis:

Mise en place réussie de méthodologies agiles, entraînant une augmentation de 20% de l'efficacité des projets.
Livraison ponctuelle et dans les limites du budget de 15 applications web.
Responsabilités:

Direction d'une équipe de 8 développeurs
Gestion des calendriers de projet
Collaboration avec les chefs de produit
Conception et mise en œuvre d'applications web
Marketing Coordinator - Global Marketing Solutions
Entreprise: Global Marketing Solutions
Lieu: New York, NY
Date de Début: Avril 2012
Date de Fin: Juin 2014
Type d'Emploi: Temps Plein
Salaire/Compensation: USD 50,000 par an
Références: Sarah Johnson (Marketing Manager), sjohnson@email.com
Description:
En tant que Coordinateur Marketing chez Global Marketing Solutions, j'ai coordonné des campagnes marketing pour des clients de diverses industries. J'ai participé à la recherche et à l'analyse de marché. J'ai créé des supports marketing et réalisé des présentations clients. J'ai géré les comptes de médias sociaux et analysé les performances. J'ai collaboré avec une équipe diversifiée pour élaborer des stratégies marketing réussies.

Compétences:

Stratégie Marketing
Recherche de Marché
Relations Client
Gestion des Médias Sociaux
Analyse de Données
Résultats Accomplis:

Développement et exécution de campagnes marketing réussies pour 10 clients, entraînant une augmentation de 15% de l'engagement client.
Analyse des tendances du marché et fourniture d'informations précieuses aux clients.
Responsabilités:

Assistance à la recherche de marché
Création de supports marketing
Gestion des comptes de médias sociaux
Réalisation de présentations clients
Collaboration avec des équipes pluridisciplinaires
Formation
Master en Informatique - Université de Californie
Université: Université de Californie
Lieu: San Francisco, CA
Année d'Obtention: 2015
Description: Master en Informatique avec spécialisation en Développement Logiciel
Baccalauréat en Marketing - Université de New York
Université: Université de New York
Lieu: New York, NY
Année d'Obtention: 2012
Description: Baccalauréat en Marketing avec concentration en Stratégie Marketing
"""

print(extract_experiences(resume=fake_resume))