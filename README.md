# RavenRPC

Crazy simple Ravencoin RPC library

INSTALL:

```
pip install RavenRPC
```

**Then run ravend** (This is very important!!!!!!!)

Examples:

```python
from ravenrpc import Ravencoin

rvn = Ravencoin('username', 'password')
rvn.getinfo()
rvn.listreceivedbyaddress(0, True)
```

Any other rpc method:

```python
rvn.<METHOD>(<param1>, <param2>, ...)
```

**Note**: If the username and password are incorrect, then a empty string will be returned. 

Please report any bugs to ME! 
 - jon@jon.network
 - Discord: JonPizza#1675
