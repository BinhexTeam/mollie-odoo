from collections import defaultdict

from odoo import models, _
from odoo.exceptions import ValidationError


class MollieSyncTerminal(models.TransientModel):
    _inherit = 'sync.mollie.terminal'

    def sync_now(self):
        """
        Override base sync_now to sync terminals for each unique POS Mollie API key.
        Groups all pos.configs by their mollie_terminal_api_key and syncs once per unique key.
        """
        pos_configs = self.env['pos.config'].search([
            ('mollie_terminal_api_key', '!=', False),
            ('company_id', 'in', self.env.companies.ids),
        ])

        if not pos_configs:
            raise ValidationError(_('Configure a Mollie Terminal API key on at least one POS configuration.'))

        configs_by_key = defaultdict(lambda: self.env['pos.config'])
        for config in pos_configs:
            configs_by_key[config.mollie_terminal_api_key] |= config

        for api_key in configs_by_key.keys():
            self.env['mollie.pos.terminal'].with_context(
                mollie_api_key=api_key
            )._sync_mollie_terminals()
