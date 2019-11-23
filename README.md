# RavenRPC

Crazy simple Ravencoin RPC library

Examples:

```python
import ravenrpc

rvn = ravenrpc.Ravencoin('username', 'password')
rvn.getinfo()
rvn.listreceivedbyaddress(0, True)
```

Any other rpc method:

```python
rvn.<METHOD>(<param1>, <param2>, ...)
```
