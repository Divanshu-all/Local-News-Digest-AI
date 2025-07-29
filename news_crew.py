import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool

def main():
    """
    Main function to run the local news digest crew.
    """
    # Load environment variables from .env file
    load_dotenv()

    print("## Welcome to the Local News Digest Crew! ##")
    print('-----------------------------------------------')
    
    # You can change this to any local news website
    news_website_url = 'https://www.tribuneindia.com/news/himachal'

    # 1. Define the Tool
    # The scraper agent will use this tool to scrape website content.
    scrape_tool = ScrapeWebsiteTool()

    # 2. Define the Agents
    # Each agent has a specific role, goal, and backstory.

    # Agent 1: Web Scraper
    scraper = Agent(
      role='Local News Scraper',
      goal=f'Scrape the full content of the top news articles from {news_website_url}',
      backstory="""You are an expert web scraper. You are known for your ability to
      efficiently extract clean, relevant text content from any webpage, ignoring
      ads, navigation, and other non-essential elements.""",
      verbose=True,
      allow_delegation=False,
      tools=[scrape_tool]
    )

    # Agent 2: Summarizer
    summarizer = Agent(
      role='Expert News Summarizer',
      goal='Create a concise, easy-to-read summary of each news article',
      backstory="""You are a seasoned journalist with a talent for distillation.
      Your summaries capture the essence of a story—the who, what, where, when, and
      why—in just two or three compelling sentences.""",
      verbose=True,
      allow_delegation=False,
    )

    # Agent 3: Category Classifier
    classifier = Agent(
      role='News Category Classifier',
      goal='Classify each summarized news article into a relevant category',
      backstory="""You are a meticulous librarian of information. You have an
      encyclopedic knowledge of news beats and can instantly categorize any story
      into predefined topics like 'Local Politics', 'Sports', 'Technology',
      'Lifestyle', or 'Weather'.""",
      verbose=True,
      allow_delegation=False,
    )

    # 3. Define the Tasks
    # The tasks are sequential, with the output of one feeding into the next.

    # Task 1: Scrape the news
    scrape_task = Task(
      description=f'Scrape the news articles from the website: {news_website_url}',
      expected_output='A clean list of the full text content of the latest news articles.',
      agent=scraper
    )

    # Task 2: Summarize the scraped content
    summarize_task = Task(
      description="""For each article, create a compelling and concise summary
      that is no more than 3 sentences long.""",
      expected_output='A list of summarized news articles, each with a clear headline.',
      agent=summarizer,
      context=[scrape_task]
    )

    # Task 3: Classify the summarized news
    classify_task = Task(
      description="""Take the list of summarized articles and classify each one
      into one of the following categories:
      - Local Politics
      - Business
      - Sports
      - Technology
      - Environment
      - General News""",
      expected_output="""A final report with each news summary neatly organized
      under its assigned category.""",
      agent=classifier,
      context=[summarize_task]
    )

    # 4. Assemble and Run the Crew
    news_digest_crew = Crew(
      agents=[scraper, summarizer, classifier],
      tasks=[scrape_task, summarize_task, classify_task],
      verbose=True
    )

    print("\n🚀 Crew: Kicking off the Local News Digest creation...\n")
    result = news_digest_crew.kickoff()

    print("\n\n########################")
    print("✅ Crew: Here is your Local News Digest!")
    print("########################\n")
    print(result)

if __name__ == '__main__':
    main()