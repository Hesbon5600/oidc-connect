import requests
import logging
from django.conf import settings

LOGGER = logging.getLogger(__name__)


def revoke_token(token_type, token):
    """Revoke an OIDC token."""

    token_revoke_payload = {
        "client_id": settings.OIDC_RP_CLIENT_ID,
        "client_secret": settings.OIDC_RP_CLIENT_SECRET,
        "token": token,
        "token_type_hint": token_type,
    }

    try:
        response = requests.post(
            settings.OIDC_OP_TOKEN_REVOKE_ENDPOINT, data=token_revoke_payload
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        LOGGER.error("Failed to revoke token: %s", e)


def oidc_logout(request):
    """Logout the user."""

    token_types = {
        "refresh_token": request.session.get("oidc_refresh_token"),
        "access_token": request.session.get("oidc_access_token"),
    }

    for token_type, token in token_types.items():
        if token:
            LOGGER.info("Revoking token of type %s", token_type)
            revoke_token(token_type, token)
