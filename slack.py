import httpx
from typing import Any, Mapping
from pydantic import BaseModel, Field, HttpUrl


class SlackMessage(BaseModel):
    text: str = Field(..., description="Plain-text message")


async def send_slack(
    webhook_url: HttpUrl | str,
    payload: SlackMessage | Mapping[str, Any],
    *,
    timeout: float | None = 10.0,
) -> httpx.Response:
    if not isinstance(payload, SlackMessage):
        payload = SlackMessage.model_validate(payload)

    async with httpx.AsyncClient(http2=True, timeout=timeout) as client:
        response = await client.post(str(webhook_url), json=payload.model_dump())
        response.raise_for_status()
    return response