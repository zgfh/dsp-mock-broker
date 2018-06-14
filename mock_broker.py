#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 18/3/14 上午10:26
"""
import logging

from flask import Flask, jsonify

LOG = logging.getLogger(__name__)

app = Flask(__name__)


def mock_plan():
    result = []
    for cpu in [100, 500, 1000, 2000, 4000, 8000]:
        for memory in [512, 1024, 2048, 4096, 8192]:
            for disk in [8, 50, 100, 200]:
                result.append({
                    "name": "plan-{}cpu-{}m-{}g-0gpu".format(cpu, memory, disk),
                    "id": "a61c75f24af95a9fe23ec9372a322915",
                    "description": "plan-100cpu-512m-8g-0gpu",
                    "metadata": {
                        "bullets": [
                            "cpu:100cpu",
                            "memory:512m",
                            "storage:8g",
                            "gpu:0gpu"
                        ],
                        "clustersize": "1",
                        "storagesize": "1"
                    },
                    "free": True,
                    "schemas": {
                        "service_instance": {
                            "create": {
                                "parameters": {
                                    "$schema": "http://json-schema.org/draft-04/schema#",
                                    "properties": {
                                        "default_db": {
                                            "description": "Database Creating by default.",
                                            "type": "string",
                                            "default": "default_db",
                                            "unit": "",
                                            "editable": "yes",
                                            "visible": "yes",
                                            "availablevalues": []
                                        },
                                        "mysql_root_password": {
                                            "description": "Root Password of MySQL",
                                            "type": "string",
                                            "default": "dangerous",
                                            "unit": "",
                                            "editable": "yes",
                                            "visible": "yes",
                                            "availablevalues": []
                                        }
                                    },
                                    "type": "object"
                                }
                            },
                            "update": {
                                "parameters": None
                            }
                        }
                    }
                })

    return result


@app.route('/v2/catalog')
def catalog():
    return jsonify({
        "services": [
            {
                "name": "daocloud-mysql",
                "id": "8b22a0f8c6ac487f135db3e7aeb39685",
                "description": "MySQL Master-Slave .\n",
                "bindable": True,
                "plan_updateable": True,
                "tags": [
                    "daocloud-mysql",
                    "database"
                ],
                "requires": [
                    "syslog_drain"
                ],
                "metadata": {
                    "displayName": "daocloud-mysql",
                    "documentationUrl": "https://hub.docker.com/r/tutum/mysql/",
                    "imageUrl": "https://dce.daocloud.io/objects/pictures/mysql-ha/mysql-ha.svg",
                    "longDescription": "",
                    "providerDisplayName": "DaoCloud",
                    "supportUrl": "https://hub.docker.com/r/tutum/mysql/"
                },
                "plans": mock_plan(),
                "dashboard_client": {
                    "id": "555bd7349a14b16ba7f501e61fb23085",
                    "redirect_uri": "http://daocloud.io",
                    "secret": "DaoCloud"
                }
            }
        ]
    })


# create instance
@app.route('/v2/service_instances/<instance_id>', methods=['PUT'])
def create_instance(instance_id):
    return jsonify({"dashboard_url": "http://csp-test.daocloud.io/"}), 201


# delete instance
@app.route('/v2/service_instances/<instance_id>', methods=['DELETE'])
def delete_instance(instance_id):
    return '{}', 200


@app.route('/v2/service_instances/<instance_id>/last_operation', methods=['GET'])
def last_operation(instance_id):
    return jsonify({"state": "succeeded"}), 200


@app.route('/v2/service_instances/<instance_id>/service_bindings/{}', methods=['PUT'])
def service_bindings(instance_id, ):
    return jsonify({"credentials": "xxx"}), 200


@app.route('/')
def index():
    return 'mock broker', 200


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8989, debug=False)
