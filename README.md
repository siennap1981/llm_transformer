# LLM Transformation Model Demo

A vanilla Python example demonstrating an LLM-based text transformation model.

## Features

- Transform text between various formats using LLM
- Built with vanilla Python (no frameworks required)
- Supports multiple transformation types:
  - **JSON** - Convert text to JSON format
  - **Summary** - Create concise summaries
  - **Formal** - Rewrite in formal tone
  - **Casual** - Rewrite in casual/friendly tone
  - **Bullet Points** - Convert to bullet point format
  - **Email** - Convert to professional email
- Custom transformation instructions support

## Installation

```bash
# Clone the repository
git clone https://github.com/siennap1981/octo-goggles.git
cd octo-goggles
```

## Usage

### With OpenAI API

```bash
# Set your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"

# Run the demo
python3 llm_transformer.py
```

### Without API Key (Mock Mode)

The demo works without an API key using mock transformations:

```bash
python3 llm_transformer.py
```

## Example

```python
from llm_transformer import LLMTransformer

# Initialize transformer
transformer = LLMTransformer()

# Transform text
result = transformer.transform(
    "We need to schedule a meeting tomorrow at 2pm.",
    "formal"
)
print(result)
```

## Requirements

- Python 3.7+
- openai (optional, for real LLM transformations)

## License

MIT