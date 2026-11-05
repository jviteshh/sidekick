
import asyncio
import textwrap

from playwright.async_api import async_playwright
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit


async def main():

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)

        toolkit = PlayWrightBrowserToolkit.from_browser(
            async_browser=browser
        )

        tools = toolkit.get_tools()

        print("Playwright connected successfully!")
      #  print(tools)

        # Find the navigation tool
        navigate_tool = next(
            tool for tool in tools
            if "navigate" in tool.name.lower()
        )

        # Open the website
        result = await navigate_tool.ainvoke({
            "url": "https://edition.cnn.com/"
        })

        print("\nWebsite opened successfully!")

        # Find the extract text tool
        extract_text_tool = next(
            tool for tool in tools
            if "extract_text" in tool.name.lower()
        )

        # Extract website text
        extracted_text = await extract_text_tool.ainvoke({})

        # Display extracted tex
    
        #print("\nExtracted Website Text:\n")
        #print(textwrap.fill(str(extracted_text), width=80))
        main_content = await page.locator("body").inner_text()
        print("\nWebsite content:\n")
        print(main_content)
        print("Browser will remain open. Press ENTER in terminal to close.")
        input()


        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
