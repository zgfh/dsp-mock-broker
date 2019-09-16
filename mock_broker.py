#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 18/3/14 上午10:26
"""
import logging

from flask import Flask, jsonify, request

LOG = logging.getLogger(__name__)

app = Flask(__name__)


def mock_plan():
    result = []
    for cpu in [100, 500, 1000, 2000]:
        for memory in [512, 1024, 2048, 4096]:
            for disk in [50, ]:
                result.append({
                    "name": "plan-{}cpu-{}m-{}g-0gpu".format(cpu, memory, disk),
                    "id": "plan-{}cpu-{}m-{}g-0gpu".format(cpu, memory, disk),
                    "description": "plan-{}cpu-{}m-{}g-0gpu".format(cpu, memory, disk),
                    "metadata": {
                        "bullets": [
                            "cpu:{}cpu".format(cpu),
                            "memory:{}m".format(memory),
                            "storage:{}g".format(disk),
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
    """

    :param instance_id:
    :param body:{
      "service_id": "string",
      "plan_id": "string",
      "context": {},
      "organization_guid": "string",
      "space_guid": "string",
      "parameters": {}
    }
    :return:
    """
    LOG.debug("create_instance %s param: %s", instance_id, request.get_json())
    return jsonify({"dashboard_url": "http://csp-test.daocloud.io/"}), 201
    # return jsonify({ "operation": "123123123123"}), 202
    # return jsonify({}), 400
    # return jsonify({"error": "string","description": "string"}), 409
    # return jsonify({"error": "string","description": "string"}), 422


# create instance
@app.route('/v2/service_instances/<instance_id>', methods=['PATCH'])
def update_instance(instance_id):
    """

    :param instance_id:
    :param body:{
          "context": {},
          "service_id": "string",
          "plan_id": "string",
          "parameters": {},
          "previous_values": {
            "service_id": "string",
            "plan_id": "string",
            "organization_id": "string",
            "space_id": "string"
          }
        }
    :return:
    """
    LOG.debug("update_instance %s param: %s", instance_id, request.get_json())
    return jsonify({}), 200
    # return jsonify({ "operation": "123123123123"}), 202
    # return jsonify({}), 400
    # return jsonify({"error": "string","description": "string"}), 422


# delete instance
@app.route('/v2/service_instances/<instance_id>', methods=['DELETE'])
def delete_instance(instance_id):
    service_id = request.args.get('service_id')
    plan_id = request.args.get('plan_id')
    LOG.debug("delete_instance %s %s %s param: %s", instance_id, service_id, plan_id, request.get_data())
    return '{}', 200
    # return jsonify({ "operation": "123123123123"}), 202
    # return jsonify({}), 400
    # return jsonify({}), 410
    # return jsonify({"error": "string","description": "string"}), 422


@app.route('/v2/service_instances/<instance_id>/last_operation', methods=['GET'])
def last_operation(instance_id):
    # data: service_id,plan_id,operation
    LOG.debug("last_operation %s param: %s", instance_id, request.get_data())
    return jsonify({"state": "succeeded"}), 200
    # return jsonify({}), 400
    # return jsonify({}), 410


@app.route('/v2/service_instances/<instance_id>/service_bindings/<binding_id>', methods=['PUT'])
def create_service_bindings(instance_id, binding_id):
    """

    :param instance_id:
    :param binding_id:
    :param body: {
          "context": {},
          "service_id": "string",
          "plan_id": "string",
          "app_guid": "string",
          "bind_resource": {
            "app_guid": "string",
            "route": "string"
          },
          "parameters": {}
        }
    :return:
    """
    LOG.debug("create_service_bindings %s %s param: %s", instance_id, binding_id, request.get_json())
    return jsonify({
        "credentials": {},
        "syslog_drain_url": "string",
        "route_service_url": "string",
        "volume_mounts": [
            {
                "driver": "string",
                "container_dir": "string",
                "mode": "r",
                "device_type": "shared",
                "device": {
                    "volume_id": "string",
                    "mount_config": {}
                }
            }
        ]
    }), 200
    # return jsonify({}), 400
    # return jsonify({"error": "string","description": "string"}), 409
    # return jsonify({"error": "string","description": "string"}), 422


@app.route('/v2/service_instances/<instance_id>/service_bindings/<binding_id>', methods=['DELETE'])
def delete_service_bindings(instance_id, binding_id):
    service_id = request.args.get('service_id')
    plan_id = request.args.get('plan_id')
    LOG.debug("delete_service_bindings %s %s %s %s param: %s", instance_id, binding_id, service_id, plan_id,
              request.get_data())

    return '{}', 200
    # return jsonify({}), 400
    # return jsonify({}), 410


@app.route('/')
def index():
    return 'mock broker', 200


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8989, debug=False)
