# Instagram-notes-updates
## Getting Started

Follow these steps to get started with the project:

1. Clone the GitHub repository:

   ```bash
   git clone https://github.com/Yaekirua/Instagram-notes-updates.git
cd Instagram-notes-updates
pip install -r requirements.txt

## Changing Notes in `main.py`

If you want to customize the notes used in the application, follow these steps:

1. Open the `main.py` file in your code editor.
2. Locate the section where the notes are defined, typically around line 11.
3. Modify the notes according to your preferences.
4. Save the `main.py` file.

Example (main.py):

```python
# Example notes
notes = [
    "Note 1",
    "Note 2",
    "Note 3",
]
## Putting Instagram Credentials into `.env`

To access Instagram functionality, you'll need to set up your Instagram credentials in a `.env` file. Follow these steps:

1. Create a new file in the project directory named `.env` if it doesn't already exist.

2. Open the `.env` file in a text editor.

3. Add your Instagram credentials in the following format:

   ```env
   INSTAGRAM_USERNAME=your_username
   INSTAGRAM_PASSWORD=your_password
