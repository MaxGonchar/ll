## Simple Validation
- validate JWT sigh
- validate expiration time

## Advanced Validation
When user register/login:
- generate access token and refresh token
- store refresh + access token in DB

When user request for service
- validate JWT sigh
- validate expiration time
- validate token against DB

When user request a token refresh
- generate new access and new refresh tokens
- store in db