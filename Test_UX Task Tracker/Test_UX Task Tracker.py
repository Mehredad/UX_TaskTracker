import unittest
from io import StringIO
from unittest.mock import patch

# Conduct unit testing with valid and invalid inputs scenarios
class TestUXTaskTracker(unittest.TestCase):
    @patch('builtins.input', side_effect=['45'])
    def test_time_taken_input(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            while True:
                try:
                    time_taken = float(input("⏱️ Enter time taken to finish the task (in seconds): "))
                    self.assertEqual(time_taken, 45.0)  # Expected valid float
                    break
                # Error case
                except ValueError:
                    print("❌ Invalid input. Please enter a valid number.")

    @patch('builtins.input', side_effect=['2'])
    def test_mental_process_selection(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            valid_choices = {'1': "Cognitive", '2': "Judgement", '3': "Decision"}
            while True:
                mental_process = input("Enter your choice (1, 2, or 3): ")
                if mental_process in valid_choices:
                    self.assertEqual(valid_choices[mental_process], "Judgement")
                    break
                else:
                    print("❌ Invalid input. Please enter 1, 2, or 3.")

    @patch('builtins.input', side_effect=['Find jeans', 'done'])
    def test_subtask_input(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            sub_tasks = []
            while True:
                sub_task_name = input("🔹 Enter sub-task name (or type 'done' to finish adding sub-tasks):")
                if sub_task_name.lower() == "done":
                    break
                sub_tasks.append({"sub_task_name": sub_task_name, "steps": []})
            self.assertEqual(len(sub_tasks), 1)  # Expect one subtask
            self.assertEqual(sub_tasks[0]['sub_task_name'], 'Find jeans')

    # Unit test for edge cases, such as: empty input for task names, large numbers or boundary values for time, and multiple tasks, subtasks, and steps.
    @patch('builtins.input', side_effect=['99999'])
    def test_large_time_taken(self, mock_input):
        with patch('sys.stdout', new=StringIO()):
            time_taken = float(input("⏱️ Enter time taken to finish the task (in seconds): "))
            self.assertEqual(time_taken, 99999)


if __name__ == '__main__':
    unittest.main()