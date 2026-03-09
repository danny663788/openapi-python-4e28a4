from __future__ import annotations

from openai.types.responses.web_search_tool import AllowedDomain, BlockedDomain, WebSearchTool
from openai.types.responses.web_search_tool_param import (
    AllowedDomain as AllowedDomainParam,
    BlockedDomain as BlockedDomainParam,
    WebSearchToolParam,
)


def test_web_search_tool_with_allowed_domains() -> None:
    tool = WebSearchTool(
        type="web_search_preview",
        allowed_domains=[
            AllowedDomain(domain="github.com"),
            AllowedDomain(domain=".edu"),
        ],
    )
    assert tool.allowed_domains is not None
    assert len(tool.allowed_domains) == 2
    assert tool.allowed_domains[0].domain == "github.com"
    assert tool.allowed_domains[1].domain == ".edu"
    assert tool.blocked_domains is None


def test_web_search_tool_with_blocked_domains() -> None:
    tool = WebSearchTool(
        type="web_search_preview",
        blocked_domains=[
            BlockedDomain(domain="example.com"),
            BlockedDomain(domain=".gov"),
        ],
    )
    assert tool.blocked_domains is not None
    assert len(tool.blocked_domains) == 2
    assert tool.blocked_domains[0].domain == "example.com"
    assert tool.blocked_domains[1].domain == ".gov"
    assert tool.allowed_domains is None


def test_web_search_tool_without_domain_filters() -> None:
    tool = WebSearchTool(type="web_search_preview")
    assert tool.allowed_domains is None
    assert tool.blocked_domains is None


def test_web_search_tool_param_with_allowed_domains() -> None:
    param: WebSearchToolParam = {
        "type": "web_search_preview",
        "allowed_domains": [{"domain": "openai.com"}, {"domain": ".org"}],
    }
    assert param["allowed_domains"][0]["domain"] == "openai.com"
    assert param["allowed_domains"][1]["domain"] == ".org"


def test_web_search_tool_param_with_blocked_domains() -> None:
    param: WebSearchToolParam = {
        "type": "web_search_preview_2025_03_11",
        "blocked_domains": [{"domain": "spam.com"}],
    }
    assert param["blocked_domains"][0]["domain"] == "spam.com"


def test_allowed_domain_param_can_be_instantiated() -> None:
    d: AllowedDomainParam = {"domain": "github.com"}
    assert d == {"domain": "github.com"}


def test_blocked_domain_param_can_be_instantiated() -> None:
    d: BlockedDomainParam = {"domain": "malicious.com"}
    assert d == {"domain": "malicious.com"}
