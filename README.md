# YouTube Chatbot

## A Smarter Way to Learn from Videos

Have you ever found yourself in that frustrating situation where you need specific information from a 2-hour YouTube video? You know it's in there somewhere, but you have to skip around, rewind, and watch sections over and over again. We've all been there. That's exactly what this project solves.

**YouTube Chatbot** lets you paste a YouTube link and have an intelligent conversation with an AI that has actually watched and understood the entire video. No more endless scrubbing. No more guessing where that one thing was mentioned. Just ask, and get answers grounded directly in the video's content.

## What This Actually Does

Think of it as having a personal study buddy who's watched the video and is ready to answer any question you throw at them. Here's what happens behind the scenes:

1. **Fetch Video Content** - The system automatically extracts the transcript from any YouTube video you provide
2. **Break It Down** - The transcript gets split into manageable chunks so the AI can better understand context
3. **Smart Retrieval** - When you ask a question, it finds the most relevant parts of the video using AI embeddings
4. **AI-Powered Answers** - Finally, a language model reads those relevant sections and generates an accurate answer based only on what's in the video

## Getting Started

The process is simple. Really simple.

### Prerequisites

You'll need Python 3.9 or later. That's really the main requirement.

### Installation

Here's the step-by-step process:

**Step 1: Clone the Repository**
```bash
git clone https://github.com/iamdivyanshukumar/YouTube-Chatbot-project.git
cd ytub-chatbot
```

**Step 2: Create a Virtual Environment** (highly recommended, but optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Set Up Your OpenAI API Key**

Create a `.env` file in the project root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

If you don't have an OpenAI API key yet, you can get one by creating an account at [OpenAI's platform](https://platform.openai.com/api-keys).

### Running the Chatbot

Once everything is set up, just run:

```bash
python app.py
```

Then follow these simple steps:

**Step 1: Provide a YouTube URL**
```
Enter youtube url: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

**Step 2: Wait for Processing**
The system will extract and index the video transcript. Depending on the video length, this might take a minute or two:
```
Processing video... Please wait.
Video processed successfully.
```

**Step 3: Ask Your Questions**
Now you can ask anything about the video content:
```
Ask a question (or type 'exit'): What is the main topic of this video?

Answer:
The video discusses...
```

**Step 4: Keep Going**
Ask as many questions as you want. When you're done, just type 'exit' to wrap things up.

## How It Works Behind the Scenes

Here's a simple visualization of the process:

```
YouTube Video URL
    |
    v
Extract the Video Transcript
    |
    v
Split into Meaningful Chunks
    |
    v
Create AI Embeddings for Each Chunk
    |
    v
Store Everything in a Vector Database
    |
    v
User Asks a Question
    |
    v
Find the Most Relevant Chunks
    |
    v
Pass to AI Language Model
    |
    v
Get Back a Factual Answer
    |
    v
Display to the User
```

## What Technologies Power This

The project uses a combination of proven, industry-standard tools:

- **LangChain** - A framework that makes it easy to build applications with language models
- **OpenAI API** - For the AI models that understand language and generate responses
- **Chroma** - A vector database that stores and retrieves information semantically
- **Python-dotenv** - For safely managing environment variables like API keys

## Project Organization

Here's what you'll find in the project folder:

```
ytub-chatbot/
├── app.py              # The main Python script that runs everything
├── app.ipynb           # A Jupyter notebook version if you prefer that
├── requirements.txt    # All the Python packages you need to install
├── vector_stores/      # Temporary folder where video data gets stored
└── README.md           # This file!
```

## Customizing the Configuration

By default, the chatbot uses:

- **Embedding Model**: text-embedding-3-small (fast and efficient, perfect for most use cases)
- **Language Model**: gpt-3.5-turbo with temperature set to 0 (this ensures consistent, factual responses)

The temperature setting of 0 is particularly important. It tells the AI to be precise and stick to the facts rather than getting creative. This prevents hallucinations and makes answers more reliable.

If you want to experiment with different models or settings, edit the `emed_model()` and `llm_model()` functions in `app.py`.

## What Makes This Special

Here's what you get with this chatbot:

- Works with any YouTube video that has a transcript
- Answers are grounded in the actual video content (no making stuff up)
- The AI won't hallucinate or add information that wasn't there
- Simple command-line interface that anyone can use
- Automatic cleanup when you're done
- You can reuse previously processed videos without reprocessing them  

## Important Things to Know

**About API Costs**: The OpenAI API isn't free. Using this tool will cost you money based on how many API calls you make. Keep an eye on your usage to avoid surprises.

**Internet Connection**: You'll need to be connected to the internet to fetch videos from YouTube and to call the OpenAI API.

**Privacy**: Video transcripts are processed locally on your machine and stored in the vector_stores folder. Treat this data appropriately.

**Rate Limits**: YouTube has terms of service that you should respect. Don't try to process hundreds of videos in rapid succession.

## Real-World Ways You Can Use This

**Learning from Lectures**: Process educational videos and get instant explanations of concepts

**Tutorial References**: Watch programming or design tutorials once, then ask questions anytime you need clarification

**Research and Notes**: Extract information from conference talks, interviews, and webinars without rewatching

**Content Summaries**: Get quick summaries of video content without sitting through the whole thing

**Study Aid**: Use it as a study buddy to help you understand and retain information from educational content

## Running Into Problems?

Here are some common issues and how to solve them:

**Problem**: You get an "API key not found" error
- Solution: Double-check that your `.env` file is in the project root directory and that it contains the correct OPENAI_API_KEY value.

**Problem**: The application says the video couldn't be loaded
- Solution: Make sure the YouTube URL is valid, publicly accessible, and that the video has captions/transcripts available.

**Problem**: The answers don't seem accurate or relevant
- Solution: Try asking your question in a different way, or provide more context in your question. The AI does better with specific, clear questions.

**Problem**: The process is slow
- Solution: This is normal for longer videos. The system needs time to extract and process the transcript. Have some patience or grab a coffee.

## Want to Help Make This Better?

Found a bug? Have a great idea? We'd love your input:

- Open an issue to report problems or suggest improvements
- Submit pull requests if you've made enhancements
- Share your feedback on how we can make this more useful



