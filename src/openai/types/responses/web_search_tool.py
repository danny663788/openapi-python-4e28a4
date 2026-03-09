# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WebSearchTool", "UserLocation", "AllowedDomain", "BlockedDomain"]


class UserLocation(BaseModel):
    type: Literal["approximate"]
    """The type of location approximation. Always `approximate`."""

    city: Optional[str] = None
    """Free text input for the city of the user, e.g. `San Francisco`."""

    country: Optional[str] = None
    """
    The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of
    the user, e.g. `US`.
    """

    region: Optional[str] = None
    """Free text input for the region of the user, e.g. `California`."""

    timezone: Optional[str] = None
    """
    The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the
    user, e.g. `America/Los_Angeles`.
    """


class AllowedDomain(BaseModel):
    domain: str
    """The domain to allow, e.g. `github.com` or `.edu`."""


class BlockedDomain(BaseModel):
    domain: str
    """The domain to block, e.g. `example.com` or `.gov`."""


class WebSearchTool(BaseModel):
    type: Literal["web_search_preview", "web_search_preview_2025_03_11"]
    """The type of the web search tool.

    One of `web_search_preview` or `web_search_preview_2025_03_11`.
    """

    allowed_domains: Optional[List[AllowedDomain]] = None
    """A list of domains to restrict search results to.

    Supports exact matches (e.g. `github.com`) and wildcards (e.g. `.edu`, `.gov`).
    When set, only results from these domains will be returned. Cannot be used
    together with `blocked_domains`.
    """

    blocked_domains: Optional[List[BlockedDomain]] = None
    """A list of domains to exclude from search results.

    Supports exact matches (e.g. `example.com`) and wildcards (e.g. `.gov`).
    When set, results from these domains will be excluded. Cannot be used
    together with `allowed_domains`.
    """

    search_context_size: Optional[Literal["low", "medium", "high"]] = None
    """High level guidance for the amount of context window space to use for the
    search.

    One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[UserLocation] = None
    """The user's location."""
