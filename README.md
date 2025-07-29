# Local News Digest AI

A CrewAI-powered application that automatically scrapes, summarizes, and categorizes local news.

---

## Project Contents

| File             | Description                                |
|------------------|--------------------------------------------|
| news_crew.py     | Main application logic using CrewAI        |
| requirements.txt | Project dependencies for pip               |
| .env             | Environment variables for API keys         |
| LICENSE          | MIT License                                |
| README.md        | Project instructions and documentation     |


---

## Complete Setup & Run Instructions

Follow these steps in your terminal. Each command is designed for a direct copy-paste workflow.

1.  **Clone the Repository**

    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create and Activate Conda Environment**

    ```bash
    conda create --name crew_env python=3.11 -y
    conda activate crew_env
    ```

3.  **Create `requirements.txt` File**

    This command creates the file and adds the necessary package names.

    ```bash
    echo -e "crewai\ncrewai_tools\npython-dotenv" > requirements.txt
    ```

4.  **Install All Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Create `.env` File for Your API Key**

    This command creates the file and adds the placeholder key. **Remember to replace** `"YOUR_API_KEY_HERE"` with your actual key.

    ```bash
    echo "OPENAI_API_KEY='YOUR_API_KEY_HERE'" > .env
    ```

6.  **Run the Project**

    Once the setup is complete, execute the main script.

    ```bash
    python news_crew.py
    ```
