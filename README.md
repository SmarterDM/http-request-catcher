# HTTP Request Catcher

This docker container catches outbound HTTP requests. It is useful for the functional testing of services such as API clients and webhook dispatchers.

## Example Usage

```sh
docker run --rm -p 5000:5000 smarterdm/http-request-catcher
```

Once the container is running, make a `POST` request to `http://localhost:5000/foo-bar`.

Now, if you make a `GET` request to `http://localhost:5000/__last_request__` you should receive the following response:

```json
{
    "data": "{\"foo\":\"bar\"}",
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "13",
        "Content-Type": "application/json",
        "Host": "localhost:5000",
        "Postman-Token": "54200866-4f53-48af-9979-a0aca6fc0db4",
        "User-Agent": "PostmanRuntime/6.2.5"
    },
    "method": "POST",
    "time": "2018-07-18T16:17:15.427144",
    "url": "http://localhost:5000/foo-bar"
}
```

## Kubernetes support

This project also supports Kubernetes deployments (tested on k8s 1.17). It might allow you to debug your ingress configuration. As prerequisite, you need a Kubernetes cluster with a Ingress controller configured.

To deploy, update the values of $YOUR_IMAGE and $YOUR_URL in the k8s_manifest.yml.

Then deploy through

```sh
kubectl apply -f k8s_manifest.yml
```

Once deployed, make your POST API calls to `$YOUR_URL/foo-bar` and your GET API calls to `$YOUR_URL/__last_request`