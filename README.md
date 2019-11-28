# RavenRPC

Crazy simple Ravencoin RPC library, designed to work with all versions of Ravencoin.

*"I have seen many libraries, this one... is pretty average" - Joe*

INSTALL:

```
pip install ravenrpc
```

## Setting Up Ravend (Linux)

go to your `.raven` folder, add a `raven.conf` file if there is not one already, in that file add:

```
rpcuser=username
rpcpassword=password
```

**Make sure you use a secure username and password!**

Then run `./ravend` in the directory that it is located!

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

Please report any bugs by filling out an issue!

## Use it with other cryptos too!!

Just set the port when accessing:

```
btc = Ravencoin('username', 'password', port=8332)
```

And if you want to use a different host:

```
btc = Ravencoin('username', 'password', host='host.com', port=8333)
```
