from openai.types.responses import WebSearchTool, WebSearchToolParam


def test_web_search_tool_allowed_domains() -> None:
    tool = WebSearchTool(type="web_search_preview", allowed_domains=["github.com", "*.edu"])
    assert tool.allowed_domains == ["github.com", "*.edu"]
    assert tool.blocked_domains is None


def test_web_search_tool_blocked_domains() -> None:
    tool = WebSearchTool(type="web_search_preview", blocked_domains=["*.ads.com", "example.com"])
    assert tool.blocked_domains == ["*.ads.com", "example.com"]
    assert tool.allowed_domains is None


def test_web_search_tool_no_domain_filter() -> None:
    tool = WebSearchTool(type="web_search_preview")
    assert tool.allowed_domains is None
    assert tool.blocked_domains is None


def test_web_search_tool_param_allowed_domains() -> None:
    param: WebSearchToolParam = {
        "type": "web_search_preview",
        "allowed_domains": ["github.com", "*.gov"],
    }
    assert param["allowed_domains"] == ["github.com", "*.gov"]
    assert "blocked_domains" not in param


def test_web_search_tool_param_blocked_domains() -> None:
    param: WebSearchToolParam = {
        "type": "web_search_preview",
        "blocked_domains": ["*.ads.com"],
    }
    assert param["blocked_domains"] == ["*.ads.com"]
    assert "allowed_domains" not in param


def test_web_search_tool_wildcard_patterns() -> None:
    tool = WebSearchTool(
        type="web_search_preview_2025_03_11",
        allowed_domains=["*.edu", "*.gov", "en.wikipedia.org"],
    )
    assert "*.edu" in (tool.allowed_domains or [])
    assert "*.gov" in (tool.allowed_domains or [])
    assert "en.wikipedia.org" in (tool.allowed_domains or [])
