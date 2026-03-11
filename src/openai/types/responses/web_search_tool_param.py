# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebSearchToolParam", "UserLocation"]


class UserLocation(TypedDict, total=False):
    type: Required[Literal["approximate"]]
    """The type of location approximation. Always `approximate`."""

    city: Optional[str]
    """Free text input for the city of the user, e.g. `San Francisco`."""

    country: Optional[str]
    """
    The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of
    the user, e.g. `US`.
    """

    region: Optional[str]
    """Free text input for the region of the user, e.g. `California`."""

    timezone: Optional[str]
    """
    The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the
    user, e.g. `America/Los_Angeles`.
    """


class WebSearchToolParam(TypedDict, total=False):
    type: Required[Literal["web_search_preview", "web_search_preview_2025_03_11"]]
    """The type of the web search tool.

    One of `web_search_preview` or `web_search_preview_2025_03_11`.
    """

    search_context_size: Literal["low", "medium", "high"]
    """High level guidance for the amount of context window space to use for the
    search.

    One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[UserLocation]
    """The user's location."""

    allowed_domains: Optional[List[str]]
    """A list of domains to restrict search results to.

    Each entry may be an exact domain (e.g. `"github.com"`) or a wildcard pattern
    (e.g. `"*.edu"`, `"*.gov"`). When set, only results from these domains are
    returned. Mutually exclusive with `blocked_domains`.
    """

    blocked_domains: Optional[List[str]]
    """A list of domains to exclude from search results.

    Each entry may be an exact domain (e.g. `"example.com"`) or a wildcard pattern
    (e.g. `"*.gov"`). When set, results from these domains are filtered out.
    Mutually exclusive with `allowed_domains`.
    """
