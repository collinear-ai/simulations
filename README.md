# Collinear TraitMix Simulations

&nbsp; &nbsp;[![arXiv](https://img.shields.io/badge/arxiv-2510.04491-b31b1b)](https://arxiv.org/abs/2510.04491) &nbsp; &nbsp; [![Blog:TraitBasis](https://img.shields.io/badge/Blog-TraitBasis-orange)](https://blog.collinear.ai/p/trait-basis) &nbsp; &nbsp; [![Benchmark:TauTrait](https://img.shields.io/badge/Benchmark-TauTrait-blue)](https://github.com/collinear-ai/tau-trait)

<img width="1216" height="704" alt="traitmix" src="https://github.com/user-attachments/assets/4dce85b0-bef4-42dc-b00e-5586d7a04014" height="10" />

Collinear TraitMix is a product for sandbox AI agent testing with simulations. With TraitMix, you can generate realistic, high-fidelity, multi-turn user interactions conditioned on user intents and user personas (traits and attributes). TraitMix can be used to evaluate agents, to create training data for long horizon RL training, or to prototype product flows. 

TraitMix is powered by our cutting-edge research on steering personas called TraitBasis. TraitBasis is a method for highly-controllable generations that does not suffer from the limitations of prompt-based approaches like the user persona fading with number of turns or the user forgetting the intent in a long context. 

Demo notebooks can be found in the `examples/` directory. Contact info@collinear.ai for an API key to generate simulations using TraitBasis.

## Features
- Generate multi-turn customer interactions directly from the example notebooks.
- Tune personas, intents, and sampling parameters through the JSON configs in `examples/**/configs/`.
- Call Together or any OpenAI-compatible endpoint by supplying your API keys.
- (Together example) Upload simulation outputs to Together and poll evaluation jobs entirely within the notebook flow.
- (Together example) Review persona summaries and scored transcripts inline to decide next changes.


## Example folders
- `examples/quick_start/`: Minimal notebook to generate TraitMix rollouts.
- `examples/rl/`: Rollouts tailored for long-horizon RL training workflows using examples similar to Tau Bench
- `examples/simulations_together_evals/`: End-to-end testing for nay other hosted on Together using Together Evals.


## Getting Started
### Install & Configure
Install uv if you don't already have it, then prepare the environment:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source .venv/bin/activate
uv venv --python 3.12 --seed
uv pip install --upgrade pip
uv pip install jupyterlab ipykernel together collinear nest_asyncio jinja2 --no-cache
uv pip install "openai>=1.13.3" "mistralai>=0.4.0" "anthropic>=0.26.1" "google-generativeai>=0.5.4" "tenacity>=8.3.0" "termcolor>=2.4.0" "numpy>=1.26.4" "litellm==1.41.0"
uv pip install tau-trait

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
