from typing import List, Iterable, Pattern
from pydantic import BaseModel
from openai import AzureOpenAI, OpenAI
from holmes.core.issue import Issue
from holmes.core.tool_calling_llm import LLMResult

# Sources must implmenet this
class SourcePlugin:
    def fetch_issues(self, issue_id: Pattern = None) -> List[Issue]:
        raise NotImplementedError()

    # optional
    def stream_issues(self) -> Iterable[Issue]:
        raise NotImplementedError()
    
    # optional
    def write_back_result(self, issue_id: str, result_data: LLMResult) -> None:
        raise NotImplementedError()

# Destinations must implement this
class DestinationPlugin:

    def send_issue(self, issue: Issue, result: LLMResult):
        raise NotImplementedError()

    # def send_grouped_issues(self, issues: List[Issue]):
    #    raise NotImplementedError()

    # def group_issues()
    #    raise NotImplementedError()
