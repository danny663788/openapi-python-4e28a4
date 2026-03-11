from openai.types.responses import WebSearchTool
from openai.types.responses.web_search_tool_param import WebSearchToolParam


def test_web_search_tool_allowed_domains() -> None:
    tool = WebSearchTool(type="web_search_preview", allowed_domains=["github.com", "*.edu"])
    assert tool.allowed_domains == ["github.com", "*.edu"]
    assert tool.blocked_domains is None


def test_web_search_tool_blocked_domains() -> None:
    tool = WebSearchTool(type="web_search_preview", blocked_domains=["*.gov", "example.com"])
    assert tool.blocked_domains == ["*.gov", "example.com"]
    assert tool.allowed_domains is None


def test_web_search_tool_no_domain_filter() -> None:
    tool = WebSearchTool(type="web_search_preview")
    assert tool.allowed_domains is None
    assert tool.blocked_domains is None


def test_web_search_tool_param_allowed_domains() -> None:
    param: WebSearchToolParam = {
        "type": "web_search_preview",
        "allowed_domains": ["github.com", "*.edu"],
    }
    assert param["allowed_domains"] == ["github.com", "*.edu"]
    assert "blocked_domains" not in param


def test_web_search_tool_param_blocked_domains() -> None:
    param: WebSearchToolParam = {
        "type": "web_search_preview",
        "blocked_domains": ["*.gov", "example.com"],
    }
    assert param["blocked_domains"] == ["*.gov", "example.com"]
    assert "allowed_domains" not in param


def test_web_search_tool_both_domain_fields_accepted_by_model() -> None:
    # The library does not enforce mutual exclusivity at the Python level;
    # the API is expected to validate that only one field is used at a time.
    tool = WebSearchTool(
        type="web_search_preview",
        allowed_domains=["github.com"],
        blocked_domains=["example.com"],
    )
    assert tool.allowed_domains == ["github.com"]
    assert tool.blocked_domains == ["example.com"]
