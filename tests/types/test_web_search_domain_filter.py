"""Unit tests for domain filtering fields on WebSearchTool / WebSearchToolParam."""

from __future__ import annotations

from openai.types.responses.web_search_tool import WebSearchTool
from openai.types.responses.web_search_tool_param import WebSearchToolParam


# ---------------------------------------------------------------------------
# WebSearchTool (BaseModel – response/output side)
# ---------------------------------------------------------------------------


def test_web_search_tool_defaults_no_domain_filters() -> None:
    """allowed_domains and blocked_domains default to None."""
    tool = WebSearchTool(type="web_search_preview")
    assert tool.allowed_domains is None
    assert tool.blocked_domains is None


def test_web_search_tool_allowed_domains_exact() -> None:
    """Exact domain strings are stored correctly."""
    tool = WebSearchTool(type="web_search_preview", allowed_domains=["github.com", "openai.com"])
    assert tool.allowed_domains == ["github.com", "openai.com"]
    assert tool.blocked_domains is None


def test_web_search_tool_allowed_domains_wildcards() -> None:
    """Suffix-wildcard entries (e.g. '.edu', '.gov') are stored correctly."""
    tool = WebSearchTool(type="web_search_preview", allowed_domains=[".edu", ".gov"])
    assert tool.allowed_domains == [".edu", ".gov"]


def test_web_search_tool_blocked_domains() -> None:
    """blocked_domains stores a list of domain strings."""
    tool = WebSearchTool(type="web_search_preview", blocked_domains=["example.com", ".ads"])
    assert tool.blocked_domains == ["example.com", ".ads"]
    assert tool.allowed_domains is None


def test_web_search_tool_mixed_exact_and_wildcard_allowed() -> None:
    """A mix of exact domains and wildcard suffixes is accepted."""
    domains = ["github.com", ".edu", "docs.python.org"]
    tool = WebSearchTool(type="web_search_preview", allowed_domains=domains)
    assert tool.allowed_domains == domains


# ---------------------------------------------------------------------------
# WebSearchToolParam (TypedDict – request/input side)
# ---------------------------------------------------------------------------


def test_web_search_tool_param_allowed_domains() -> None:
    """WebSearchToolParam accepts allowed_domains and behaves like a plain dict."""
    param: WebSearchToolParam = {
        "type": "web_search_preview",
        "allowed_domains": ["github.com", ".edu"],
    }
    assert param["allowed_domains"] == ["github.com", ".edu"]
    assert "blocked_domains" not in param


def test_web_search_tool_param_blocked_domains() -> None:
    """WebSearchToolParam accepts blocked_domains."""
    param: WebSearchToolParam = {
        "type": "web_search_preview",
        "blocked_domains": ["example.com", ".ads"],
    }
    assert param["blocked_domains"] == ["example.com", ".ads"]
    assert "allowed_domains" not in param


def test_web_search_tool_param_without_domain_filters() -> None:
    """WebSearchToolParam works fine without any domain filter keys."""
    param: WebSearchToolParam = {"type": "web_search_preview"}
    assert "allowed_domains" not in param
    assert "blocked_domains" not in param
