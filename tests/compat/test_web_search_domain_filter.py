from openai.types.responses import WebSearchTool, WebSearchToolParam
from openai.types.chat.completion_create_params import WebSearchOptions


def test_web_search_tool_domain_filter() -> None:
    tool = WebSearchTool(
        type="web_search_preview",
        domain_filter={
            "include": ["github.com", ".edu"],
            "exclude": ["example.com", ".gov"],
        },
    )

    assert tool.domain_filter is not None
    assert tool.domain_filter.include == ["github.com", ".edu"]
    assert tool.domain_filter.exclude == ["example.com", ".gov"]


def test_web_search_domain_filter_params() -> None:
    tool_param = WebSearchToolParam(
        type="web_search_preview",
        domain_filter={"include": ["github.com"], "exclude": [".gov"]},
    )
    assert tool_param == {
        "type": "web_search_preview",
        "domain_filter": {"include": ["github.com"], "exclude": [".gov"]},
    }

    options = WebSearchOptions(
        search_context_size="low",
        domain_filter={"include": ["github.com"], "exclude": [".gov"]},
    )
    assert options == {
        "search_context_size": "low",
        "domain_filter": {"include": ["github.com"], "exclude": [".gov"]},
    }
