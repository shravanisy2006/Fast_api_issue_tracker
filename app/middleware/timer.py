import time
from fastapi import Request
async def timing_middleware(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    response.heahders["X-Process-Time"] = str(time.perf_counter() - start_time)
    return response
