## Register (Sign-on)
### request
```
POST
{
    "email": ...,
    "first": ...,
    "last": ...,
    "psw": ...
}
```
### response
```
201
{
    "data": {
        "accessToken": ...,
        "refreshToken": ...
    }
}

```

## Log-in
### request
```
POST
{
    "email": ...,
    "psw": ...
}
```
### response
```
201
{
    "data": {
        "accessToken": ...,
        "refreshToken": ...
    }
}
```
```
401
{
    "message": "Unauthorized"
}
```

## Refresh
### request
```
POST
{
    "email": ...,
    "psw": ...
}
```
### response
```
201
{
    "data": {
        "accessToken": ...,
        "refreshToken": ...
    }
}
```
```
401
{
    "message": "Unauthorized"
}
```

## Log-out

## Unregister