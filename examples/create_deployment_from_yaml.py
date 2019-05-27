from os import path

from kubernetes import client, config, utils


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()
    k8s_client = client.ApiClient()
    utils.create_from_yaml(k8s_client, "nginx-deployment.yaml")
    k8s_api = client.ExtensionsV1beta1Api(k8s_client)
    deps = k8s_api.read_namespaced_deployment("nginx-deployment", "default")
    print("Deployment {0} created".format(deps.metadata.name))


if __name__ == '__main__':
    main()
