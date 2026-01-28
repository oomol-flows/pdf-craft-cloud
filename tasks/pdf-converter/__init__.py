#region generated meta
import typing
class Inputs(typing.TypedDict):
    pdf_url: str
    output_format: typing.Literal["markdown", "epub"]
    model: str | None
    poll_interval: float | None
    max_attempts: float | None
    ignore_pdf_errors: bool | None
    ignore_ocr_errors: bool | None
class Outputs(typing.TypedDict):
    download_url: typing.NotRequired[str]
#endregion

from oocana import Context
import httpx
import asyncio


async def main(params: Inputs, context: Context) -> Outputs:
    """Convert PDF to Markdown or EPUB format."""
    pdf_url = params["pdf_url"]
    output_format = params.get("output_format", "markdown")
    model = params.get("model") or "gundam"
    poll_interval = params.get("poll_interval") or 3
    max_attempts = params.get("max_attempts") or 2400
    ignore_pdf_errors = params.get("ignore_pdf_errors")
    if ignore_pdf_errors is None:
        ignore_pdf_errors = True
    ignore_ocr_errors = params.get("ignore_ocr_errors")
    if ignore_ocr_errors is None:
        ignore_ocr_errors = True

    token = await context.oomol_token()

    # Determine API endpoints based on output format
    if output_format == "epub":
        submit_url = "https://fusion-api.oomol.com/v1/pdf-transform-epub/submit"
        result_url_template = "https://fusion-api.oomol.com/v1/pdf-transform-epub/result/{}"
    else:  # markdown
        submit_url = "https://fusion-api.oomol.com/v1/pdf-transform-markdown/submit"
        result_url_template = "https://fusion-api.oomol.com/v1/pdf-transform-markdown/result/{}"

    # Step 1: Submit conversion request
    max_retries = 3
    session_id = None

    for attempt in range(max_retries):
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    submit_url,
                    headers={
                        "Authorization": token,
                        "Content-Type": "application/json"
                    },
                    json={
                        "pdfURL": pdf_url,
                        "model": model,
                        "ignore_pdf_errors": ignore_pdf_errors,
                        "ignore_ocr_errors": ignore_ocr_errors
                    }
                )

                result = response.json()

                if not result.get("success", False):
                    raise Exception(f"Failed to submit PDF conversion: {result}")

                session_id = result.get("sessionID")
                if not session_id:
                    raise Exception("No session ID returned from API")

                break

        except (httpx.ConnectError, httpx.TimeoutException) as e:
            if attempt < max_retries - 1:
                print(f"Connection error (attempt {attempt + 1}/{max_retries}): {e}. Retrying...")
                await asyncio.sleep(2)
                continue
            else:
                raise Exception(f"Failed to submit request after {max_retries} attempts: {e}")

    # Step 2: Poll for conversion progress
    result_url = result_url_template.format(session_id)
    headers = {"Authorization": token}
    attempts = 0

    async with httpx.AsyncClient(timeout=30.0) as client:
        while attempts < max_attempts:
            attempts += 1

            try:
                response = await client.get(result_url, headers=headers)
                response.raise_for_status()

                data = response.json()

                if not data.get("success", False):
                    raise Exception("API request was not successful")

                state = data.get("state", "processing")
                api_progress = data.get("progress", 0)

                # Report progress (keeping 99 as max until completed)
                context.report_progress(min(api_progress, 99))

                if state == "completed":
                    context.report_progress(100)
                    download_url = data.get("data", {}).get("downloadURL", "")
                    if not download_url:
                        raise Exception("No download URL returned from API")
                    return {"download_url": download_url}

                if state == "failed":
                    error_msg = data.get("data", {}).get("error", "Transformation failed")
                    raise Exception(f"Conversion failed: {error_msg}")

                await asyncio.sleep(poll_interval)

            except (httpx.ConnectError, httpx.TimeoutException) as e:
                print(f"Network error on attempt {attempts}/{max_attempts}: {e}")
                if attempts >= max_attempts:
                    raise Exception(f"Failed to connect to API after {max_attempts} attempts: {e}")
                await asyncio.sleep(poll_interval)
                continue

    raise Exception(f"Polling timeout after {max_attempts} attempts")
