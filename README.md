# Collinear Simulations using *TraitBasis*
Generate realistic, high-fidelity, multi-turn user interactions conditioned on user intents and user personas (traits and attributes). Simulations can be used to evaluate agents, to create training data for long horizon RL training, or to prototype product flows.

TraitBasis is a method for highly-controllable generations that does not suffer from the limitations of prompt-based approaches like the user persona fading with number of turns or the user forgetting the intent in a long context. We will be releasing our paper shortly.

Demo notebooks can be found in the `examples/` directory. Contact info@collinear.ai for an API key to generate simulations using TraitBasis.

## Features
- Generate multi-turn customer interactions directly from the example notebooks.
- Tune personas, intents, and sampling parameters through the JSON configs in `examples/**/configs/`.
- Call Together or any OpenAI-compatible endpoint by supplying your API keys.
- (Together example) Upload simulation outputs to Together and poll evaluation jobs entirely within the notebook flow.
- (Together example) Review persona summaries and scored transcripts inline to decide next changes.


## Example folders
- `examples/quick_start/`: Minimal notebook to generate TraitBasis-driven rollouts.
- `examples/rl/`: Rollouts tailored for long-horizon RL training workflows using examples similar to Tau Bench
- `examples/simulations_together_evals/`: Together model as the agent + Together Evals judging end-to-end.


## Getting Started
### Install & Configure
Install uv if you don't already have it, then prepare the environment:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python 3.12 --seed
uv pip install --upgrade pip
uv pip install jupyterlab ipykernel together collinear nest_asyncio jinja2
uv pip install -e examples/rl/tau-hard mistralai==0.4.2 httpx==0.27.2 # tau-hard (RL) dependencies
uv run python -m ipykernel install --user --name trait-basis
```

If you plan to call Together endpoints, export your API key in the active shell:

```bash
export TOGETHER_API_KEY="YOUR_TOGETHER_API_KEY"
```

### Run the Notebooks
Start Jupyter from the project root:

```bash
uv run --with jupyter jupyter lab
```

Select the `trait-basis` kernel in each notebook and run the grouped import cell before generating simulations.
