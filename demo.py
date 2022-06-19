from time import sleep
import asyncio
from src.aiorestlight.restlight import RestLight

from aiohttp import (
    ClientConnectionError,
    ClientResponse,
    ClientSession,
    ClientTimeout,
    ServerDisconnectedError,
)

class Demo:
    def __init__(self) -> None:
        self.light = RestLight(ClientSession(), 1, "hermes", 25741)
    
    async def run(self) -> None:
        print("running demo")
        await self.light.get_info()

        print(f"Light Name: {self.light.name}")
        print(f"Model: {self.light._model}")
        print(f"Is On: {self.light.is_on}")
        print(f"Brightness: {self.light.brightness}")
        print(f"Hue: {self.light.hue}")
        print(f"Saturation: {self.light.saturation}")
        print(f"Effects: {self.light.effects_values}")
        print(f"Selected Effect: {self.light.effect}")
        print(f"Pixel Count: {self.light.pixel_count}")
        print(f"Pixels: {self.light.pixels}")

        await self.light.turn_off()
        sleep(0.5)
        await self.light.set_hue(120)
        sleep(0.5)
        await self.light.set_brightness(25)
        sleep(0.5)
        await self.light.set_saturation(10)
        sleep(0.5)
        await self.light.set_saturation(100)
        sleep(0.5)
        await self.light.set_brightness(100)
        sleep(0.5)
        await self.light.set_effect("Big Sur")
        sleep(1)
        await self.light.set_hue(300)
        sleep(1)
        await self.light.identify()

async def run_async():
    app = Demo()
    await app.run()


if __name__ == "__main__":
    print ("Starting demo")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_async())
    loop.close()
