Class: https://ssctech.udemy.com/course/istio-hands-on-for-kubernetes/learn/lecture/23922456#overview

What is it
* builds service mesh
* does this by installing proxy side cars in pods
  * inside -n istio system ther's a istio-sidecar-injector pod that installs these
  * Side car is a helper container that does extra work: in this case a proxy
* containers in pods talk to proxy
* proxy talks to other proxy
* proxys are installed on pods with a lable per namespace
  * If you want istio everywhere you put that lable on all namespaces
  * check for lable in namespace with `k describe ns defalut `(for default namespace)
    * by default you'll have `Labels: <none>`
    * add label for default namespace with
      * `k label namespace default istio-injection=enabled`
  * Once the namespaces are labeled correctly you should see something like
    * `pod_name_1      2/2     Running             0                42m`
    * the 2/2 means that there are 2 containers running in that pod.  This could be one of the proxy/side-cars