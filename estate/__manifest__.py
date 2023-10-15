{
    "name": "Estate",  # The name that will appear in the App list
    "category": "Real Estate/Brokerage",
    "version": "16.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base", "web"],  # dependencies
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_view.xml",
        "views/estate_property_menu.xml",
    ],
    "installable": True,
    'license': 'LGPL-3',
}
