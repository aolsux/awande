#! /bin/env python

import connexion

from connexion import RestyResolver
from prometheus_client import start_http_server

if __name__ == "__main__":
    app = connexion.App(__name__, specification_dir='.', swagger_ui=True)
    app.add_api('awande.yaml', resolver=RestyResolver('api'), strict_validation=True)
    # Start up the server to expose the metrics.
    start_http_server(8091)
    app.run(port=8090)
