# OptimalMastermind

OptimalMastermind is a Python project that implements the classic Mastermind game, featuring an optimal guessing strategy based on entropy calculations. The repository is organized into several key components as described below.

## Project Structure

- **Core Logic**
  - `mastermind.py` & `mastermind_classes.py`: Contain the main game logic, data structures, and optimal entropy-based guessing strategy.

- **Auxiliary Scripts**
  - Scripts for generating lookup tables and other utilities.
  - `play_mastermind.py`: Command-line interface (CLI) for playing Mastermind.

- **Web Interface**
  - `server.py`: Flask server for running the web version of Mastermind.
  - `static/`: Contains static assets (CSS, JS, images) for the web interface.
  - `templates/`: HTML templates for rendering the Flask web pages.

## Features

- Play Mastermind via CLI or a web interface.
- Uses entropy to compute the most informative guess at each step.
- Easily extensible and organized for both experimentation and interactive play.

## Getting Started

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Play via CLI**
   ```bash
   python play_mastermind.py
   ```

3. **Run the Web App**
   ```bash
   python server.py
   ```
   Then navigate to `http://localhost:5000` in your browser.

## License

MIT License. See [LICENSE](LICENSE) for details.
