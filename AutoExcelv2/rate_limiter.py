import asyncio
import time


class RateLimiter:
    def __init__(self, max=1, period=1):
        self.period = period
        self.max = max
        self.signal = asyncio.Event()
        self.lock = asyncio.Lock()
        self._tasks = [asyncio.create_task(self.ticker())]
        self.signal.set()

    # This signals the event period/max times/second (so if
    # max=4 and period=1, this fires the signal ever 0.25 seconds).
    async def ticker(self):
        while True:
            await asyncio.sleep(self.period / self.max)
            self.signal.set()

    # When entering the context, 
    async def __aenter__(self):
        async with self.lock:
            await self.signal.wait()
            self.signal.clear()
        return self

    async def __aexit__(self, *args):
        pass
        
