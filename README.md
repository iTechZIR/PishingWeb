> # PhishingWeb - Automated Phishing Page Clone Tool

A sophisticated Python tool that automates the cloning of websites for security testing and phishing simulation exercises.

> ## Overview

PhishingWeb is an advanced web cloning utility designed for security professionals and penetration testers to create realistic phishing simulations. It intelligently downloads and reconstructs target websites by embedding all external resources directly into a single HTML file.

> ## Features

- **Complete Website Cloning**: Downloads entire web pages including all CSS and JavaScript dependencies
- **Resource Consolidation**: Embeds all external resources (CSS, JS) directly into the HTML file
- **Multi-threaded Downloading**: Concurrent resource fetching for improved performance
- **Automatic URL Resolution**: Handles relative and absolute URL paths automatically
- **Clean File Naming**: Sanitizes filenames for cross-platform compatibility
- **User-Agent Spoofing**: Mimics legitimate browser requests
- **Session Management**: Maintains consistent connections for better reliability

> ## Installation

> ### Requirements
- Python 3.6 or higher
- Required Python libraries

> ### Setup
```bash
# Install required packages
pip install requests beautifulsoup4
```

> ## Project Structure

```
phishingweb/
├── phishingweb.py              # Main script file
├── __fishing_list__/           # Generated phishing pages directory
│   └── *.html                  # Cloned HTML pages
└── README.md                   # Documentation
```

> ## Usage

> ### Basic Command

```bash
# Run the tool
python phishingweb.py
```

> ### Interactive Process

1. Launch the script
2. Enter target website URL when prompted
3. Tool automatically:
   - Fetches the HTML content
   - Downloads all CSS files
   - Downloads all JavaScript files
   - Consolidates everything into single HTML
   - Saves to `__fishing_list__/` directory

> ### Command Example

```bash
python phishingweb.py

# When prompted:
# Enter: https://example.com
# Output: Page saved as __fishing_list__/Example-Page.html
```

> ## Technical Details

> ### Resource Handling

**CSS Processing:**
- Downloads all stylesheet links
- Embeds CSS content within `<style>` tags
- Removes original `<link>` tags

**JavaScript Processing:**
- Downloads all external scripts
- Embeds JS content within `<script>` tags
- Removes original `<script src>` tags

**URL Resolution:**
- Converts relative URLs to absolute paths
- Handles protocol-relative URLs
- Maintains resource integrity

> ### Performance Optimization

- **Concurrent Downloads**: Uses ThreadPoolExecutor for parallel resource fetching
- **Connection Reuse**: Implements session management for efficiency
- **Timeout Handling**: Configurable timeouts for network operations
- **Error Resilience**: Graceful error handling without process termination

> ## Output Format

> ### Generated HTML Structure
```html
<!DOCTYPE html>
<html>
<head>
    <!-- Original meta tags and title -->
    <style>
        /* All embedded CSS content */
    </style>
</head>
<body>
    <!-- Original HTML content -->
    <script>
        /* All embedded JavaScript */
    </script>
</body>
</html>
```

> ### File Naming Convention
Files are named using the website title with sanitization:
- Original: `Example Website | Login Page`
- Sanitized: `Example-Website---Login-Page.html`

> ## Error Handling

The tool includes comprehensive error handling for:
- Network connectivity issues
- Invalid URLs or domains
- Resource download failures
- File system permissions
- HTML parsing errors

> ## Security Applications

> ### Legitimate Use Cases
- **Security Awareness Training**: Create realistic phishing simulations
- **Penetration Testing**: Test organizational phishing defenses
- **Red Team Exercises**: Simulate advanced persistent threats
- **Educational Purposes**: Demonstrate phishing techniques in controlled environments
- **Security Tool Development**: Test anti-phishing solutions

> ### Ethical Considerations
⚠️ **Important**: This tool should only be used for:
- Authorized security testing
- Educational purposes
- Security research with proper consent
- Testing your own systems

> ## Performance Metrics

- **Page Fetch Time**: ~2-5 seconds (depending on resources)
- **Resource Consolidation**: ~1-3 seconds
- **Concurrent Connections**: Up to 10 simultaneous downloads
- **File Size Optimization**: Minimal overhead for embedded resources

> ## Platform Support

- Windows 10/11
- Linux distributions (Ubuntu, Debian, Kali)
- macOS 10.14+
- Cross-terminal compatibility

> ## Troubleshooting

> ### Common Issues

**Issue**: "Error retrieving CSS/JS"
**Solution**: Check internet connection and target website accessibility

**Issue**: "Invalid URL"
**Solution**: Ensure URL includes http:// or https:// prefix

**Issue**: "Permission denied"
**Solution**: Run with appropriate file system permissions

> ### Debug Mode
For troubleshooting, modify the script to enable verbose logging:
```python
# Add debug prints in resource download sections
print(f"[DEBUG] Downloading: {url}")
```

> ## License

MIT License - Free for educational and authorized security testing purposes

> ## Author

**Creator**: 2yt  
**Telegram**: [@GKSVGK](https://t.me/GKSVGK)  
**Channels**: [@iTechZIR](https://t.me/iTechZIR), [@dev_2yt_code_c](https://t.me/dev_2yt_code_c)

> ## Version History

**1.0.0** - Initial Release
- Complete website cloning functionality
- CSS and JavaScript embedding
- Multi-threaded resource downloading
- File sanitization and organization
- User-agent spoofing capabilities

> ## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

> ## Acknowledgments

- Beautiful Soup team for HTML parsing library
- Python requests library for HTTP handling
- Security community for ethical testing methodologies

> ## Disclaimer

This tool is intended for **authorized security testing and educational purposes only**. Unauthorized use against systems you do not own or have explicit permission to test is illegal and unethical. Always obtain proper authorization before conducting any security testing.

---

⭐ If you find this tool useful for legitimate security testing, please give it a star !
