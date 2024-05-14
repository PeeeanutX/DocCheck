# DocCheck

## Overview
DocCheck is designed to streamline the process of implementing new handling devices in assembly planning within a 
multiproject environment. By leveraging AI to automate data and summary generation, DocCheck reduces manual planning
efforts and enhances decision-making efficiency.

## Features
- **Automated Data Analysis**: Automatically processes and analyzes progress reports and logs related to the assembly
of handling devices.
- **Content-Based Summaries**: Provides up-to-date summaries on the status of implementation processes.
- **Self-Learning AI**: Continuously improves its data processing and summary generation capabilities based on user
feedback and new data.

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8+

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/PeeeanutX/DocCheck.git
   cd DocCheck
   
2. Install the rquired dependencies:
   ```bash
   pip install -r requirements.txt
   
### Usage
To start using DocCheck, run the following command from the root directory of the project:
```bash
python src/main.py
```

## Development
### Structure
- **`data/`**: Contains raw and processed data used by the application.
- **`src/`**: Source code for the project including AI models and API interfaces.
- **`tests/`**: Contains tests for ensuring code quality and functionality.
- **`notebooks/`**: Jupyter notebooks for exploratory data analysis and interactive model training.

### Testing
Run the following command to execute tests:
```bash
python -m unittests discover -s tests
```