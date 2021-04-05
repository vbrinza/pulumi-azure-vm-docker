# Web Server Using Azure Virtual Machine

This example deploys an Azure Virtual Machine and starts a Docker container with an HTTP server on it.

## Prerequisites

1. [Install Pulumi](https://www.pulumi.com/docs/get-started/install/)
1. [Configure Pulumi for Azure](https://www.pulumi.com/docs/intro/cloud-providers/azure/setup/)
1. [Configure Pulumi for Python](https://www.pulumi.com/docs/intro/languages/python/)

## Deploying and running the program

1. Create a new stack:

    ```bash
    $ pulumi stack init dev
    ```

1. Set the required configuration for this example. This example requires you to supply a username and password to the virtual machine that we are going to create.

    ```bash
    $ pulumi config set azure-native:location westeurope    # any valid Azure region will do
    $ pulumi config set username testuser
    $ pulumi config set password --secret <your-password> 
    ```

    Note that `--secret` ensures your password is encrypted safely.


1. Run `pulumi up` to preview and deploy the changes.

1. Get the IP address of the newly-created instance from the stack's outputs: 

    ```bash
    $ pulumi stack output public_ip
    ```

1. Check to see that your server is now running:

    ```bash
    $ curl http://$(pulumi stack output public_ip)
    ```

1. Count the words:
   ```bash
   echo http://$(pulumi stack output public_ip) | python main.py 
   ```
1. Destroy the stack:

    ```bash
    $ pulumi destroy --yes
    ```