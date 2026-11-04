
import asyncio

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
        print(tools)

        # Find the navigation tool
        navigate_tool = next(
            tool for tool in tools
            if "navigate" in tool.name.lower()
        )

        # Open Google
        result = await navigate_tool.ainvoke({
            "url": "https://www.google.com"
        })

        print("\nWebsite result:")
        print(result)

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())

