# py-data_seattle

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Clone the Repository

```bash
git clone https://github.com/eginez/py_data_seatttle_2025.git
cd py-data_seattle_2025
```

### Installation

1. Create a virtual environment (recommended):

```bash
python -m venv venv
```

2. Activate the virtual environment:

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Notebooks

Start Jupyter Lab:

```bash
jupyter lab
```

This will open Jupyter Lab in your browser. Navigate to the `src/` directory to access the notebooks:

- `1_graphs_and_algos.ipynb` - Graph algorithms
- `2_quantum_layout.ipynb` - Quantum layout optimization

### Project Structure

```
.
├── README.md
├── requirements.txt
└── src/
    ├── 1_graphs_and_algos.ipynb
    ├── 2_quantum_layout.ipynb
    ├── data/
    └── utils.py
```

## Dependencies

This project uses Qiskit and related quantum computing libraries, along with standard data science tools like NumPy, Pandas, Matplotlib, and Seaborn. See `requirements.txt` for the complete list.

## Deactivating the Virtual Environment

When you're done, deactivate the virtual environment:

```bash
deactivate
```
