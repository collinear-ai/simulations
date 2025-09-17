# Collinear Simulations
Generate realistic, high-fidelity, multi-turn user interactions conditioned on user intents and user personas (traits and attributes). Simulations can be used to evaluate agents, to create training data for long horizon RL training, or to prototype product flows.

Demo notebooks can be found in the `examples/` directory. Contact info@collinear.ai for an API key to generate high quality synthetic data.

## Features
- Generate multi-turn customer interactions directly from the example notebooks.
- Tune personas, intents, and sampling parameters through the JSON configs in `examples/**/configs/`.
- Call Together or any OpenAI-compatible endpoint by supplying your API keys.
- Upload simulation outputs to Together and poll evaluation jobs entirely within the notebook flow.
- Review persona summaries and scored transcripts inline to decide next changes.


## Getting Started
### Install & Configure
Install uv if you don't already have it, then prepare the environment:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python 3.12 --seed
uv pip install --upgrade pip
uv pip install jupyterlab ipykernel together collinear nest_asyncio jinja2
uv run python -m ipykernel install --user --name collinear-synthetic
```

### Run the Notebooks
Start Jupyter from the project root:

```bash
uv run --with jupyter jupyter lab
```

Select the `collinear-synthetic` kernel in each notebook and run the grouped import cell before generating simulations.
