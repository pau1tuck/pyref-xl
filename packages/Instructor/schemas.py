# apps/insights/services/openai/schemas.py

from pydantic import BaseModel, Field
from typing import List


class KeyMetric(BaseModel):
    name: str
    value: float

    @classmethod
    def ordered_metrics(cls) -> List["KeyMetric"]:
        return [
            cls(name="Average Sessions", value=0),
            cls(name="Average Users", value=0),
            cls(name="Average New Users", value=0),
            cls(name="Average Pageviews", value=0),
            cls(name="Pages per Session", value=0),
            cls(name="Average Session Duration", value=0),
            cls(name="Bounce Rate", value=0),
            cls(name="Conversion Rate", value=0),
            cls(name="Average Transactions", value=0),
            cls(name="Average Revenue", value=0),
        ]

    def validate_name(self) -> bool:
        expected_names = [metric.name for metric in self.ordered_metrics()]
        if self.name not in expected_names:
            raise ValueError(f"Unexpected metric name: {self.name}")
        return True


class SummaryOutput(BaseModel):
    dataset_summary: str = Field(
        ..., description="A concise English summary of the dataset."
    )
    key_metrics: List[KeyMetric] = Field(
        ..., description="List of key metrics extracted from the dataset."
    )

    def enforce_ordered_metrics(self):
        ordered_names = [metric.name for metric in KeyMetric.ordered_metrics()]
        self.key_metrics = sorted(
            self.key_metrics,
            key=lambda metric: (
                ordered_names.index(metric.name)
                if metric.name in ordered_names
                else float("inf")
            ),
        )
        # Ensure no unexpected metrics
        for metric in self.key_metrics:
            metric.validate_name()


class KeyMetricComparison(BaseModel):
    name: str
    value1: float
    value2: float
    description: str


class ComparisonOutput(BaseModel):
    comparison_summary: str = Field(
        ...,
        description="A concise English summary highlighting differences and similarities between the current week and the previous week.",
    )
    key_metrics_comparison: List[KeyMetricComparison] = Field(
        ...,
        description="Key metrics with values from both weeks and descriptions of differences.",
    )
