#! /bin/env python

import connexion

from connexion import RestyResolver

if __name__ == "__main__":
    app = connexion.App(__name__, specification_dir='.',  swagger_ui=True)
    app.add_api('awande.yaml', resolver=RestyResolver('api'), strict_validation=True)
    app.run(port=8090)
