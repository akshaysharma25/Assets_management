import jwt
from jwt import PyJWKClient
from utils.environment_configs import EnvironmentConfigs


def token_validator(token):
    issuer = EnvironmentConfigs.issuer_url
    jwks_endpoint = issuer + '/.well-known/openid-configuration/jwks'
    try:
        token = token.split(' ')[1]
    except IndexError:
        raise jwt.exceptions.InvalidTokenError('Invalid token header')

    # jwt verification options
    options = {
        'verify_signature': True,
        'require': ["nbf", "exp", "iss"],
        'verify_nbf': True,
        'verify_exp': True,
        'verify_iss': True,
        'verify_aud': False,
    }

    # Verify the JWT token
    try:
        jwks_client = PyJWKClient(uri=jwks_endpoint, cache_keys=True, lifespan=1200)
        jwk_set = jwks_client.get_jwk_set()
        jwk_key = jwk_set.keys[0]
        decoded_token = jwt.decode(jwt=token, key=jwk_key.key, algorithms=['RS256'],
                                   options=options, issuer=issuer)
        return decoded_token
    except jwt.InvalidSignatureError:
        raise jwt.InvalidSignatureError('invalid signature')
    except jwt.ExpiredSignatureError:
        raise jwt.ExpiredSignatureError('token expired')
    except jwt.InvalidAudienceError:
        raise jwt.InvalidAudienceError('invalid audience')
    except jwt.InvalidIssuerError:
        raise jwt.InvalidIssuerError('invalid issuer')
    except jwt.InvalidIssuedAtError:
        raise jwt.InvalidIssuedAtError('invalid issued at')
    except jwt.ImmatureSignatureError:
        raise jwt.ImmatureSignatureError('immature token')
    except jwt.InvalidKeyError:
        raise jwt.InvalidKeyError('invalid key')
    except jwt.InvalidAlgorithmError:
        raise jwt.InvalidAlgorithmError('invalid algo')
    except jwt.MissingRequiredClaimError:
        raise jwt.MissingRequiredClaimError('missing claims')
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError('invalid token')
    except Exception as e:
        raise e
