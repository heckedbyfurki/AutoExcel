import AutoExcelv2.text_extractor as text_extractor
from AutoExcelv2.excel_writer import ExcelWriter
from AutoExcelv2.rate_limiter import RateLimiter
import AutoExcelv2.info_extractor as ie
import asyncio
import time

ew = ExcelWriter()

async def main():
    limiter = RateLimiter(60, 1)
    for i in range(ew.sheet_number()):
        keywords = ew.get_keywords(i)
        result = await asyncio.gather(*[get_row_async(path, keywords, limiter) for path in text_extractor.get_image_paths()])
        print(result)
        ew.write(result, i)
    input('Press any key to exit...')


async def get_row_async(path, keywords, limiter):  # returns a list of values
    text = await text_extractor.extract_text_async(path)
    print('Text extracted from image: ', path)
    values = await ie.get_values_async(text, keywords, limiter)
    print('Values extracted from text: ', values)
    return values



