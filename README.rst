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

On remarque qu'en l'état actuel, vu que quand l'utilisateur du pos est hors ligne, les données de caisses sont stockées dans la cache (localstorage) du navigateur, on ne peut pas garantir l'inalterabilité (sauf a modifier le code source des navigateurs ce qui est inatteignable.) En effet, l'utilisateur peut toujours vider le cache du navigateur, ou le modifier grace a la console javascript. On veut donc interdire les ventes quand le pos est hors ligne, et remonter en temps réel les opérations faites sur le pos.

On développe plusieurs modules:

Le module lf2016_logs
~~~~~~~~~~~~~~~~~~~~~~

Il a pour but de stocker des logs inalterables et archivables; 

Il contient un modele/table avec notamment les colonnes suivantes:
 - id (id postgresql, rajouté automatiquement par odoo)
 - create_date (date de création, rajouté automatiquement par odoo)
 - contenu 
 - hash sha-2

Le **contenu** est un champ texte dont la syntaxe exacte reste a definir, qui contient un événement qui doit être archivé pour respecter la loi, entre autres:
 - chaque ajout/suppression/modification d'une ligne d'une facture/commande/devis
 - chaque ajout/suppression/modification d'un paiement
 - toute opération effectuee sur une ligne de facture
 - toute opération effectuee sur un paiement 
 - tout changement de l'état d'une facture/commande/devis (validation, anulation?)
 - une impression de devis/commande/ticket/facture ? (condition 5 du referentiel)
 - une reimpression de devis/commande/facture ? (condition 5 du referentiel)
 - une piece/écriture comptable
 - les comptes et les journaux comptables
 - les taxes


Le **hash** sha2 est le hash de la chaine suivante:
 - date+contenu de la ligne courante concaténé au hash de la ligne précédente
 - date+contenu de la ligne courante pour la premiere ligne de la table


Cette structure nous permet de garantir qu'aucune donnée n'a été altérée de deux manières:
 - les id postgresql de chaque ligne de la table doivent être continus, il ne doit y avoir aucun trou
 - tous les hash correpondent a ce qu'ils doivent correspondre

On envisage, dans ce module, d'ajouter une adresse email configurable, et une periodicité configurable aussi, a laquelle le module envoie par email l'id de la derniere ligne de la table ainsi que le hash de cette ligne, avec quelques infos telles que le nom de la base, le serveur, si c'est une base de test ou non, etc.. Cet email peut être hebergé chez des prestataires externes, type ovh, gmail, qui nous garantissent du coup l'inalterabilité de ce hash. 
Grace au contenu d'un email, on peut s'assurer que la base n'a pas été modifiée

Il faut rajouter une interface qui permet de telecharger un sous ensemble de cette table, pour par exemple une journée, ou une année comptable, ou pour une periode arbitraire pour une seule societe, ou plusieurs sociétés. Ce telechargement peut être au format csv

Le module lf2016_sale
~~~~~~~~~~~~~~~~~~~~~~

Il depend de lf2016_logs et herite de create et write sur les devis/commandes, et a chaque create/write, il regarde si c'est un ajout, ou une modification dans les devis/commandes, et le reporte au module de log

Il fait un suivi également de tous les changements d'états, et de toutes les impressions (comment???)

Le module lf2016_invoice
~~~~~~~~~~~~~~~~~~~~~~~~~

Il depend de lf2016_logs et herite de create et write sur les factures et reglements, et a chaque create/write, il regarde si c'est un ajout, ou une modification dans les factures, et le reporte au module de log

Il fait un suivi également de tous les changements d'états, et de toutes les impressions (comment???)

Le module lf2016_account
~~~~~~~~~~~~~~~~~~~~~~~~~

A l'installation, il rajoute dans les logs la listes des comptes/journaux
Il depend de lf2016_logs et rajoute chaque creation de piece comptable, de ligne comptable, changement d'etat d'une piece comptable, chaque modification dans le module log
Il reporte la creation/modif/suppression des compte et les journaux comptables
  
Le module lf2016_pos 
~~~~~~~~~~~~~~~~~~~~~

Un gros morceau :)

Il depend de lf2016_logs et herite de create et write sur les commandes et les reglements du pos, et a chaque create/write, il regarde si c'est un ajout, ou une modification et le reporte au module de log

Il effectue des modifications dans le point de vente pour interdire les ventes hors ligne, et reporter au serveur chaque paiement, ainsi que chaque modification de paiement, chaque modification de ligne, chaque impression, modifie impression en "reimpression" si elle a deja été effectuée

il faut rajouter un horodatage des heures d'envoi des données, et des heures d'arrivée sur odoo, ainsi qu'une valeur incrementale a chaque information envoyée par le pos à odoo

Le module lf2016_test
~~~~~~~~~~~~~~~~~~~~~~

Ce module, doit **obligatoirement** être installé si une base est une base de test, il est transversal, et rajoute FACTICE dans tous les rapports, par exemple en passant par le external header ou footer
Il modifie le pos, et les impressions de celui ci en y rajoutant FACTICE
Dans il modifie le module lf2016_logs et rajoute FACTICE au debut de chaque ligne de contenu

Le module lf2016_cloture (a partir de v9)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Il s'agit de reimplementer les clotures comptables dans odoo, qui existaient avant la v9, mais ont disparu à partir de la v9

**a approfondir, pour repertorier exactement ce qu'il faut faire**


Divers
-------
Reflexions et plan d'action partagé par rapport à la loi finances 2016 et Odoo/Openerp

*Si vous voulez un accés en modification, envoyez moi le nom de votre compte github à simon@auneor-conseil.fr*

Liens:
 - http://bofip.impots.gouv.fr/bofip/10691-PGP
 - https://www.lne.fr/fr/certification/reglements/referentiel-certification-systemes-caisse.pdf
 - https://mensuel.framapad.org/p/wcqzwJ4COq


