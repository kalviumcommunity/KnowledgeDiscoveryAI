import unittest

class TestKnowledgeDiscoveryAI(unittest.TestCase):
    def test_sample_1(self):
        # Replace with actual model call and expected output
        model_output = "AI applications in healthcare are improving diagnostics."
        expected_output = "AI applications in healthcare"
        self.assertIn(expected_output, model_output)

    def test_sample_2(self):
        model_output = "Renewable energy is key to fighting climate change."
        expected_output = "climate change"
        self.assertIn(expected_output, model_output)

    def test_sample_3(self):
        model_output = "Deep learning enables complex pattern recognition."
        expected_output = "deep learning"
        self.assertIn("deep learning", model_output.lower())

    def test_sample_4(self):
        model_output = "Blockchain improves supply chain transparency."
        expected_output = "supply chain"
        self.assertIn(expected_output, model_output)

    def test_sample_5(self):
        model_output = "Pomodoro and GTD are effective productivity techniques."
        expected_output = "productivity techniques"
        self.assertIn(expected_output, model_output)

if __name__ == "__main__":
    unittest.main()
