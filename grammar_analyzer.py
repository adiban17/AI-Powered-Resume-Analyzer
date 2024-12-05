import language_tool_python

# Initialize the grammar checker
tool = language_tool_python.LanguageTool('en-US')  # or 'en-GB' for British English

# Text to check
def grammar_analysis(text):

    # Check for grammar mistakes
    matches = tool.check(text)

    # Display suggestions
    for match in matches:
        print(f"Error: {match.message}")
        print(f"Suggestion: {match.replacements}")
