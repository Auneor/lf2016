# -*- coding: utf-8 -*-

from openerp import models, fields, api
import hashlib

class lf2016_logs(models.Model):
    _name = 'lf2016_logs.lf2016_logs'
    name = fields.Char(string="Contenu")
    hash=fields.Char(string="Hash",readonly=True)

    @api.model
    def create(self, vals):
        vals = vals
        self.env.cr.execute("SELECT id from lf2016_logs_lf2016_logs order by -id limit 1")
        lastId=self.env.cr.fetchone()
        toHash=""
        if lastId:
            last=self.browse([lastId[0]])
            toHash+=last.hash

        creation=super(lf2016_logs, self).create(vals)

        toHash+=creation.create_date
        toHash+=creation.name+"\n"
        creation.hash=hashlib.sha256(toHash).hexdigest()

        return creation

    def write(self, cr, uid, ids, vals, context=None):
        if "name" in vals:
            del vals['name']
        return super(lf2016_logs,self).write(cr,uid,ids,vals,context)

class CheckWizard(models.TransientModel):
    _name="lf2016_logs.wizard"
    result=fields.Text(string="Result",readonly=True)

    @api.multi
    def check(self):
        all=self.env["lf2016_logs.lf2016_logs"].search([],order="id")
        res=""
        hashPrecedent=""
        idPrecedent=""
        for a in all:
            if not idPrecedent:
                idPrecedent=a.id
            else:
                if idPrecedent+1!=a.id:
                    res+="Attention, Saut dans les ID, entre "+str(idPrecedent)+" et "+str(a.id)+"\n"
                idPrecedent=a.id
            toHash=hashPrecedent+a.create_date+a.name+"\n"
            if hashlib.sha256(toHash).hexdigest()!=a.hash:
                res+="ERREUR: id "+str(a.id)+" Le hash n'est pas bon\n"
            hashPrecedent=a.hash
        if not res:
            res="Base cohérente, pas d'erreur trouvée"
        self.result=res
