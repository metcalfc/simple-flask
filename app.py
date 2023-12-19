#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
from os import environ as env
from flask import Flask

app = Flask(__name__)


workspace = env.get('DAYTONA_WS_ID', 'user-repo-abcd1234')
domain = env.get('DAYTONA_WS_DOMAIN', 'daytona.io')
port = 5000

@app.route("/")
def hello():
    return "Hello World! from https://" + str(port) + "-" + workspace + "." + domain

if __name__ == "__main__":
   app.run(host="localhost", port=port, debug=True)


