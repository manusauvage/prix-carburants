# Statistiques sur le prix des carburants

Ce script utilise les [données exposées en open data par le Gouvernement français](https://www.prix-carburants.gouv.fr/rubrique/opendata/) pour calculer : 
- Le prix moyen du litre d'essence SP95-E10
- Le prix moyen du litre d'essence E85
- le rapport densité/prix pour ces deux types d'essence.

L'information calculée n'a rien de scientifique, c'est une tentative un peu empirique d'évaluer si le passage au E85 apporte un réel gain ou non. S'il y a une grosse erreur de raisonnement, n'hésitez pas à me la signaler, ou à rebondir sur [la discussion qui m'a poussé à scripter l'analyse](https://mamot.fr/@edasfr/109751282298858307)

Les données de rendement utilisées (énergie libérée par litre) sont issues d'un article
du site [Auto-IES](https://www.auto-ies.com/blog/actualites/e85-le-grand-gagnant-parmi-les-carburants).

Pour référence, les valeurs données sont :
- 6,5KWh par litre pour l'E85
- 10KWh par litre pour l'E85

Si ces chiffres sont fondés, il est donc a priori nécessaire d'utiliser 1,54L d'E85 pour dégager la même énergie qu'un litre de E10. 

Le résultat du script (rapport densité/prix) a pour but de déterminer si, dans ces conditions, l'utilisation du E85 est économique ou non en donnant 2 chiffres comparables pour les 2 types d'essence. Plus le rapport densité/prix est élevé, meilleur est le rendement. Si le rapport calculé pour le E85 est supérieur, c'est donc intéressant financièrement. Dans le cas contraire, il vaut mieux rester sur du E10. Si le chiffre est proche, l'intérêt du E85 n'est pas prouvé (puisqu'il faut dépenser de l'argent pour faire adapter son véhicule).



# Chiffres pour 2021, 2022, et au 26 janvier 2023

    $ python prix_carburants_gouv_fr.py PrixCarburants_annuel_2021.xml
    100%|█████████████████████████████████████████████████████████████████████████| 13386/13386 [00:04<00:00, 2748.35it/s]
    7089 stations vendent du E10 - Prix moyen: 1.552 - rapport densité/prix: 6.442
    2769 stations vendent du E85 - Prix moyen: 0.709 - rapport densité/prix: 9.167

En 2021, le rapport est a priori très favorable au E85. Le prix au litre est très intéressant, même avec une efficacité moindre.


    $ python prix_carburants_gouv_fr.py PrixCarburants_annuel_2022.xml
    100%|█████████████████████████████████████████████████████████████████████████| 13645/13645 [00:05<00:00, 2506.08it/s]
    7246 stations vendent du E10 - Prix moyen: 1.789 - rapport densité/prix: 5.591
    3260 stations vendent du E85 - Prix moyen: 0.813 - rapport densité/prix: 7.991

En 2022, le rapport reste assez favorable au E85.


    $ python prix_carburants_gouv_fr.py /tmp/PrixCarburants_annuel_2023.xml
    100%|█████████████████████████████████████████████████████████████████████████| 13579/13579 [00:00<00:00, 28693.94it/s]
    7133 stations vendent du E10 - Prix moyen: 1.867 - rapport densité/prix: 5.356
    3205 stations vendent du E85 - Prix moyen: 1.127 - rapport densité/prix: 5.767

Au 26 janvier 2023 en revanche, le prix au litre du E85 a fortement augmenté, dans des proportions bien supérieures à celle du E10. Il est trop tôt pour dire si la tendance actuelle va durer ou non, et comparer une période de 26 jours à une année entière n'est pas particulièrement rigoureux. L'indication est cependant intéressante.


Tout cela ne vaut bien entendu que si le raisonnement sous-jacent n'est pas trop fanfaron.
