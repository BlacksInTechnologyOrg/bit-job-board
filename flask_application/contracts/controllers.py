from flask import Blueprint, request, redirect, render_template
from flask_application.controllers import TemplateView
from flask_application.users.models import Contract
from flask_application.contracts.forms import ContractForm
contracts = Blueprint('contracts', __name__)


class ContractView(TemplateView):
    blueprint = contracts
    route = '/contract/<int:contract_id>'
    route_name = 'contract'
    template_name = 'contracts/contract.html'
    methods = ['GET','POST']

    def dispatch_request(self, *args, **kwargs):
        form = ContractForm()
        contract = Contract.objects(contract_id=self.contract_id)

        if request.method == 'POST' and form.validate():
            form.populate_obj(contract)
            contract.save()
            return redirect(self.route)

        return render_template(self.template_name, form=form, contract=contract)
