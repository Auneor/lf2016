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

Il a pour but de stocker des logs inalterables et archivables; 

Il contient un modele/table avec les colonnes suivantes:
 - id (id postgresql, rajouté automatiquement par odoo)
 - contenu 
 - hash sha-2

Le **contenu** est un champ texte dont la syntaxe exacte reste a definir, qui contient un événement qui doit être archivé pour respecter la loi, entre autres:
 - chaque ligne d'une facture/commande
 - chaque paiement
 - toute operation effectuee sur une ligne de facture (modification par ajout)
 - toute operation effectuee sur un paiement (modification par ajout)
 - tout changement de l'état d'une facture/commande (validation, anulation?)
 - une impression de facture ?
 - une reimpression de facture ?
 - une écriture comptable? 

Le **hash** sha2 est le hash de la chaine suivante: 
 - contenu de la ligne courante concaténé au hash de la ligne précédente
 - contenu de la ligne courante pour la premiere ligne de la table

Cette structure nous permet de garantir qu'aucune donnée n'a été altérée de deux manières:
 - les id postgresql de chaque ligne de la table doivent être continus, il ne doit y avoir aucun trou
 - tous les hash correpondent a ce qu'ils doivent correspondre

On envisage, dans ce module, d'ajouter une adresse email configurable, et une periodicité configurable aussi, a laquelle le module envoie par email l'id de la derniere ligne de la table ainsi que le hash de cette ligne, avec quelques infos telles que le nom de la base, le serveur, etc.. Cet email peut être hebergé chez des prestataires externes, type ovh, gmail, qui nous garantissent du coup l'inalterabilité de ce hash. 
Grace au contenu d'un email, on peut s'assurer que la base n'a pas été modifiée
  
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


