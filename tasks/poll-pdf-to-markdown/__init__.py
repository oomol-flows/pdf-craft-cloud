#region generated meta
import typing
class Inputs(typing.TypedDict):
    session_id: str
    poll_interval: float
    max_attempts: float
class Outputs(typing.TypedDict):
    download_url: str
#endregion

from oocana import Context
import httpx
import asyncio

async def main(params: Inputs, context: Context) -> Outputs:
    """Poll the PDF to Markdown transformation progress."""
    session_id = params["session_id"]
    poll_interval = params.get("poll_interval", 5)
    max_attempts = params.get("max_attempts", 60)

    token = await context.oomol_token()
    url = f"https://fusion-api.oomol.com/v1/pdf-transform-markdown/result/{session_id}"
    headers = {"Authorization": token}

    attempts = 0

    async with httpx.AsyncClient(timeout=30.0) as client:
        while attempts < max_attempts:
            attempts += 1

            response = await client.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            print(data)

            if not data.get("success", False):
                raise Exception("API request was not successful")

            state = data.get("state", "processing")
            api_progress = data.get("progress", 0)

            context.report_progress(min(api_progress, 99))

            if state == "completed":
                context.report_progress(100)
                download_url = data.get("data", {}).get("downloadURL", "")
                return {"download_url": download_url}

            if state == "failed":
                error_msg = data.get("data", {}).get("error", "Transformation failed")
                raise Exception(error_msg)

            await asyncio.sleep(poll_interval)

    raise Exception(f"Polling timeout after {max_attempts} attempts")
