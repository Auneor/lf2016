Module pour odoo V10
Pour rajouter une ligne dans le log, il faut rajouter dans le code python quelque chose du style:
self.env['lf2016_logs.lf2016_logs'].create({'name':"contenu"}), et le hash sera calculé automatiquement