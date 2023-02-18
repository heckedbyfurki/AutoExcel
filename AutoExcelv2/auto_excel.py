import AutoExcelv2.text_extractor as text_extractor
from AutoExcelv2.excel_writer import ExcelWriter
import AutoExcelv2.info_extractor as ie
import asyncio

ew = ExcelWriter()


async def main():
    for i in range(ew.sheet_number()):
        keywords = ew.get_keywords(i)
        result = await asyncio.gather(*[get_row_async(path, keywords) for path in text_extractor.get_image_paths()])
        ew.write(result, i)
    input('Press any key to exit...')


async def get_row_async(path, keywords):  # returns a list of values
    text = await text_extractor.extract_text_async(path)
    # print(text, end='\n--------------------\n')
    values = await ie.get_values_async(text, keywords)
    # print('\n------< VALUES >------\n')
    # print("values: ", values, end='\n-------<ENDL>-------\n')
    return values