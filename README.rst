====================================================================================
Changements à apporter à odoo pour être en conformité avec la loi finances 2016
====================================================================================

Introduction
-------------

L'idée est de decouper le travail en plusieurs sous taches, qui pourront être effectuées par differents partenaires odoo

Il s'agit aussi de définir des dates, dates auxquelles ont veut voir une fonctionnalité terminée

Nous nous basons sur le document du lne comme objectif https://www.lne.fr/fr/certification/reglements/referentiel-certification-systemes-caisse.pdf

Architecture
-------------

On developpe plusieurs modules:

Le module lf2016_logs
~~~~~~~~~~~~~~~~~~~~~
Il a pour but de creer des logs inalterables et archivables, avec les caracteristiques suivantes:
 - un modele/table avec les colonnes suivantes
  - contenu
  - hash sha-2
  

Le module lf2016_pos 
~~~~~~~~~~~~~~~~~~~~~
 Il effectue des modifications dans le point de vente pour se mettre en conformité (en notamment qui interdit les ventes hors ligne)




Divers
-------
Reflexions et plan d'action partagé par rapport à la loi finances 2016 et Odoo/Openerp

*Si vous voulez un accés en modification, envoyez moi le nom de votre compte github à simon@auneor-conseil.fr*

Liens:
 - http://bofip.impots.gouv.fr/bofip/10691-PGP
 - https://www.lne.fr/fr/certification/reglements/referentiel-certification-systemes-caisse.pdf
 - https://mensuel.framapad.org/p/wcqzwJ4COq


