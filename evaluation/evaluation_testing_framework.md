# Evaluation Dataset and Testing Framework

## Evaluation Dataset (5 Samples)

### Sample 1
- **Input:** Article about AI in healthcare
- **Expected Output:** Summary and insights about AI applications in healthcare

### Sample 2
- **Input:** Podcast transcript on renewable energy
- **Expected Output:** Key points and connections to climate change notes

### Sample 3
- **Input:** Book excerpt on deep learning
- **Expected Output:** Main concepts and cross-references to existing ML notes

### Sample 4
- **Input:** Web article on blockchain in supply chain
- **Expected Output:** Summary and creative prompts for other industries

### Sample 5
- **Input:** User notes on productivity techniques
- **Expected Output:** Synthesized list of techniques and suggestions for improvement

---

## Judge Prompt
"Compare the model's output with the expected result. Rate the output for accuracy, relevance, and creativity on a scale of 1-5. Provide feedback for improvement."

---

## Testing Framework (Python Example)

```python
import unittest

class TestKnowledgeDiscoveryAI(unittest.TestCase):
    def test_sample_1(self):
        # Replace with actual model call and expected output
        model_output = "..."
        expected_output = "..."
        self.assertIn("AI applications in healthcare", model_output)

    # Add similar tests for other samples

if __name__ == "__main__":
    unittest.main()
```

---
This file demonstrates the evaluation pipeline, judge prompt, and a basic testing framework for the KnowledgeDiscoveryAI project.
