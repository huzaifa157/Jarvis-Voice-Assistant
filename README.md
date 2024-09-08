<h1>Jarvis Voice Assistant</h1>

<h3>A Voice-Controlled Personal Assistant</h3>

<p>Jarvis is a voice-controlled assistant that listens to your commands and performs various tasks such as opening websites, playing music, fetching the latest news, and closing applications. This project demonstrates how speech recognition and text-to-speech technologies can be integrated with Python for a seamless, hands-free experience.</p>

<hr>

<h2>Features</h2>

<ul>
    <li><b>Voice Recognition</b>: Understands and processes voice commands using Google Speech Recognition API.</li>
    <li><b>Text-to-Speech</b>: Provides voice responses using the <code>pyttsx3</code> text-to-speech engine.</li>
    <li><b>Web Automation</b>: Opens commonly used websites such as Google, Facebook, YouTube, and LinkedIn.</li>
    <li><b>Music Control</b>: Plays selected music on YouTube.</li>
    <li><b>News Fetching</b>: Retrieves and reads out the latest top headlines using the NewsAPI.</li>
    <li><b>App Control</b>: Can close applications based on window titles.</li>
    <li><b>Wake Word Detection</b>: Responds to various wake words, including "Hello Jarvis," "Hi Jarvis," and others.</li>
    <li><b>Customizable</b>: Easily add more commands and functionality.</li>
</ul>

<hr>

<h2>Installation</h2>

<h3>Prerequisites</h3>
<ul>
    <li>Python 3.x</li>
    <li>A virtual environment for managing dependencies (optional but recommended)</li>
</ul>

<h3>Steps</h3>

<ol>
    <li><b>Clone the Repository</b>:
    <pre><code>git clone https://github.com/huzaifa157/Jarvis-Voice-Assistant.git
cd Jarvis-Voice-Assistant</code></pre></li>

    <li><b>Create and Activate a Virtual Environment</b> (Optional):
    <pre><code>python -m venv .venv
.\.venv\Scripts\Activate</code></pre></li>

    <li><b>Install Dependencies</b>:
    <pre><code>pip install -r requirements.txt</code></pre></li>

    <li><b>Set Up NewsAPI</b>:
    <ul>
        <li>Obtain an API key from <a href="https://newsapi.org" target="_blank">NewsAPI</a>.</li>
        <li>Replace the <code>newsapi</code> variable in <code>main.py</code> with your API key:
        <pre><code>newsapi = "YOUR_API_KEY_HERE"</code></pre></li>
    </ul></li>

    <li><b>Run the Application</b>:
    <pre><code>python main.py</code></pre></li>
</ol>

<hr>

<h2>Usage</h2>

<h3>Basic Commands</h3>
<ul>
    <li><b>Open Websites</b>:
        <ul>
            <li>"Open Google"</li>
            <li>"Open Facebook"</li>
            <li>"Open YouTube"</li>
            <li>"Open LinkedIn"</li>
        </ul>
    </li>
    <li><b>Play Music</b>:
        <ul>
            <li>"Play Coldplay"</li>
            <li>"Play On My Way"</li>
        </ul>
    </li>
    <li><b>Fetch News</b>:
        <ul>
            <li>"News" (Fetches the latest top headlines)</li>
        </ul>
    </li>
    <li><b>Close Applications</b>:
        <ul>
            <li>"Close Google"</li>
            <li>"Close YouTube"</li>
        </ul>
    </li>
    <li><b>Exit</b>:
        <ul>
            <li>"Bye"</li>
            <li>"Exit"</li>
        </ul>
    </li>
</ul>

<h3>Wake Words</h3>
<ul>
    <li>Jarvis responds to wake words such as:
        <ul>
            <li>"Hello Jarvis"</li>
            <li>"Hi Jarvis"</li>
            <li>"Hey Jarvis"</li>
        </ul>
    </li>
</ul>

<hr>

<h2>Technologies Used</h2>
<ul>
    <li><b>Python</b>: Core language for implementing logic and control.</li>
    <li><b>SpeechRecognition</b>: For converting speech to text.</li>
    <li><b>pyttsx3</b>: For text-to-speech conversion.</li>
    <li><b>Webbrowser</b>: For automating browser actions.</li>
    <li><b>PyGetWindow</b>: For window and application control.</li>
    <li><b>NewsAPI</b>: To fetch the latest headlines from news sources.</li>
    <li><b>Google Speech Recognition API</b>: For voice recognition.</li>
</ul>

<hr>

<h2>Troubleshooting</h2>

<h3>Common Issues</h3>
<ul>
    <li><b>PyAudio Error</b>: Ensure that PyAudio is correctly installed. On Windows, use the following command:
    <pre><code>pip install pipwin
pipwin install pyaudio</code></pre></li>

    <li><b>Speech Recognition Not Working</b>: Check your microphone settings and ensure that Google Speech Recognition is accessible.</li>

    <li><b>API Key Error</b>: If you're receiving errors while fetching news, double-check your API key and the NewsAPI configuration.</li>
</ul>

<hr>

<h2>Future Improvements</h2>

<ul>
    <li>Enhanced NLP: Integrate Natural Language Processing for more conversational interactions.</li>
    <li>Task Scheduling: Add the ability for Jarvis to schedule tasks and set reminders.</li>
    <li>Cross-Platform Support: Expand support to macOS and Linux environments.</li>
    <li>AI Features: Introduce machine learning to enable smarter responses.</li>
</ul>

<hr>

<h2>Contributing</h2>

<p>Contributions are welcome! Please follow these steps for contributing:</p>

<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch (<code>git checkout -b feature-branch</code>).</li>
    <li>Commit your changes (<code>git commit -m 'Add new feature'</code>).</li>
    <li>Push to the branch (<code>git push origin feature-branch</code>).</li>
    <li>Open a Pull Request.</li>
</ol>

<hr>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<hr>

<h2>Contact</h2>

<p>If you have any questions or need further assistance, feel free to reach out:</p>

<ul>
    <li><b>GitHub</b>: <a href="https://github.com/huzaifa157" target="_blank">Huzaifa</a></li>
</ul>
