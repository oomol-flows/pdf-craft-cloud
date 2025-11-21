#region generated meta
import typing
class Inputs(typing.TypedDict):
    pdf_url: str
    model: str
class Outputs(typing.TypedDict):
    success: typing.NotRequired[bool]
    session_id: typing.NotRequired[str]
#endregion

from oocana import Context
import httpx


async def main(params: Inputs, context: Context) -> Outputs:
    """Submit a PDF to EPUB conversion request."""

    pdf_url = params["pdf_url"]
    model = params.get("model", "gundam")

    token = await context.oomol_token()

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            "https://fusion-api.oomol.com/v1/pdf-transform-epub/submit",
            headers={
                "Authorization": token,
                "Content-Type": "application/json"
            },
            json={
                "pdfURL": pdf_url,
                "model": model
            }
        )

        result = response.json()

        return {
            "success": result.get("success", False),
            "session_id": result.get("sessionID", "")
        }
