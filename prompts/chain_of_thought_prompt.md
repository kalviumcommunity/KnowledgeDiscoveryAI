# Chain of Thought Prompting Example

## What is Chain of Thought Prompting?
Chain of thought prompting is a technique where the AI is encouraged to reason step-by-step, making its intermediate reasoning explicit before arriving at a final answer. This helps improve performance on complex reasoning tasks.

## Example Prompt

**Prompt:**
"Read the following article and answer the question. Show your reasoning step by step."

**Input:**
Article: "A company increased its revenue by 20% in the first year and then by 10% in the second year. If the initial revenue was $100,000, what is the revenue after two years?"

**Expected Output:**
- Step 1: Initial revenue is $100,000.
- Step 2: After a 20% increase, revenue = $100,000 × 1.2 = $120,000.
- Step 3: After a 10% increase, revenue = $120,000 × 1.1 = $132,000.
- Final Answer: $132,000.

---
This file demonstrates how chain of thought prompting is used in the KnowledgeDiscoveryAI project.
