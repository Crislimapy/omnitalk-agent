import asyncio
import os
from pipecat.frames.frames import EndFrame
from pipecat.pipeline.pipeline import Pipeline
from pipecat.pipeline.runner import PipelineRunner
from pipecat.processors.frameworks.silence_detection import SilenceTimeoutProcessor
from pipecat.transports.services.daily import DailyTransport

async def main():
    transport = DailyTransport(
        room_url=os.getenv("DAILY_ROOM_URL"),
        token=os.getenv("DAILY_TOKEN"),
        bot_name="OmniTalk Agent"
    )

    # TRAVA DE SEGURNÇA: 60 segundos de silêncio encerra o bot
    silence_timeout = SilenceTimeoutProcessor(timeout=90)

    pipeline = Pipeline([
        transport.input(),
        silence_timeout,
        transport.output(),
    ])

    runner = PipelineRunner()
    await runner.run(pipeline)

if __name__ == "__main__":
    asyncio.run(main())
