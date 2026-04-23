"""
Vanilla Python LLM Transformation Model Demo
This example demonstrates using an LLM to transform text from one format to another.
"""

import json
import os
from typing import Any, Optional

# Try to import openai - if not available, use mock mode
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class LLMTransformer:
    """A simple LLM-based text transformation model."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo"):
        self.model = model
        self.client = None
        
        if OPENAI_AVAILABLE:
            api_key = api_key or os.environ.get("OPENAI_API_KEY")
            if api_key:
                self.client = OpenAI(api_key=api_key)
    
    def transform(
        self, 
        input_text: str, 
        transformation_type: str,
        instructions: Optional[str] = None
    ) -> str:
        """
        Transform input text based on the specified transformation type.
        
        Args:
            input_text: The text to transform
            transformation_type: Type of transformation (e.g., 'json', 'summary', 'formal')
            instructions: Optional custom instructions for the transformation
            
        Returns:
            Transformed text
        """
        # Define transformation prompts
        transformation_prompts = {
            "json": f'Convert the following text into a JSON format:\n\n{input_text}',
            "summary": f'Provide a concise summary of the following text:\n\n{input_text}',
            "formal": f'Rewrite the following text in a formal tone:\n\n{input_text}',
            "casual": f'Rewrite the following text in a casual, friendly tone:\n\n{input_text}',
            "bullet_points": f'Convert the following text into bullet points:\n\n{input_text}',
            "email": f'Convert the following into a professional email:\n\n{input_text}',
        }
        
        # Get the prompt
        if instructions:
            prompt = f'{instructions}\n\n{input_text}'
        elif transformation_type in transformation_prompts:
            prompt = transformation_prompts[transformation_type]
        else:
            prompt = f'Transform the following text: {input_text}'
        
        # Use OpenAI if available
        if self.client:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful text transformation assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        
        # Fallback: return mock transformation
        return self._mock_transform(input_text, transformation_type)
    
    def _mock_transform(self, text: str, transformation_type: str) -> str:
        """Mock transformation for demonstration when no API key is available."""
        mock_transformations = {
            "json": json.dumps({"transformed": text, "type": transformation_type}, indent=2),
            "summary": f"[Summary of: {text[:50]}...]",
            "formal": f"Dear Sir/Madam, regarding: {text}",
            "casual": f"Hey there! So {text}",
            "bullet_points": f"• {text}",
            "email": f"Subject: Transformation Request\n\nDear Team,\n\n{text}\n\nBest regards",
        }
        return mock_transformations.get(
            transformation_type, 
            f"Transformed ({transformation_type}): {text}"
        )


def demo():
    """Demonstrate the LLM Transformer."""
    print("=" * 60)
    print("LLM Transformation Model Demo")
    print("=" * 60)
    
    # Initialize transformer
    transformer = LLMTransformer()
    
    # Sample input text
    sample_text = """
    We need to schedule a meeting to discuss the quarterly sales report. 
    John from marketing will present the latest numbers. Sarah will talk about 
    the new marketing campaign. The meeting should be next Tuesday at 2pm in 
    the main conference room. Everyone should bring their laptops for the 
    presentation.
    """
    
    # Test different transformation types
    transformations = ["summary", "bullet_points", "formal", "email", "json"]
    
    print("\n📝 Original Text:")
    print("-" * 40)
    print(sample_text.strip())
    
    for transform_type in transformations:
        print(f"\n🔄 Transformation: {transform_type.upper()}")
        print("-" * 40)
        result = transformer.transform(sample_text, transform_type)
        print(result)
        print()
    
    # Custom transformation
    print("\n🔄 Custom Transformation (Spanish)")
    print("-" * 40)
    custom_result = transformer.transform(
        sample_text, 
        "custom",
        instructions="Translate the following text to Spanish:"
    )
    print(custom_result)
    
    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    demo()