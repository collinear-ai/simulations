## High‑Fidelity Agent Rollouts with TraitBasis, Together Models, and Together Evals

Create realistic, multi‑turn rollouts of AI agents using a Together model as the agent and evaluate them with Together Evals. This example pairs configurable user personas/intents via TraitBasis (our TraitMix method) with an agent model, then uploads the resulting transcripts for automated judging.

### What’s in this folder
- `simulations_together_evals.ipynb`: End‑to‑end notebook to generate rollouts and run evaluations.
- `configs/simulation_config.json`: Master config for models, sampling, concurrency, and Together Evals.
- `configs/traitmix_config_*.json`: Domain‑specific TraitBasis persona traits, intents, and tasks.
- `configs/judge_system_prompt.jinja`: Judge system prompt template used by Together Evals.

Note: Config files now use the `traitmix_config_*` naming. These files define TraitBasis personas (traits and characteristics) and task templates.

### Prerequisites
- Python 3.10+ recommended
- A Together API key
  - Set in your shell before running the notebook:

```bash
export TOGETHER_API_KEY="YOUR_TOGETHER_API_KEY"
```

### Install and launch Jupyter
This repo uses uv in the top‑level `simulations/README.md`. If you prefer pip, that works too.

Using uv (recommended):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python 3.12 --seed
uv pip install --upgrade pip
uv pip install jupyterlab ipykernel together collinear nest_asyncio jinja2
uv run python -m ipykernel install --user --name collinear-synthetic
uv run --with jupyter jupyter lab
```

Using pip:
```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install jupyterlab ipykernel together collinear nest_asyncio jinja2
python -m ipykernel install --user --name collinear-synthetic
jupyter lab
```

Open `simulations_together_evals.ipynb` and select the `collinear-synthetic` kernel.

### Configure
Edit `configs/simulation_config.json` to control:
- `client`: Agent model, base URL, and API key source
  - `assistant_model_url`: Typically `https://api.together.xyz/v1`
  - `assistant_model_name`: e.g. `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo`
- `simulate`: Number of samples, turns, temperatures, max tokens, and concurrency
- `assess`: Judge model settings (when judging directly via API)
- `together`: Output paths, judge system prompt path, evaluation type and thresholds
- `traitmix_config_file`: Which `traitmix_config_*.json` to use (airline, retail, etc.)

Pick a domain by setting `traitmix_config_file` to one of the provided files in `configs/`.

### Workflow at a glance
1) Generate high‑fidelity rollouts
   - The notebook builds conversations by combining a domain task from `traitmix_config_*.json` with a TraitBasis persona and your chosen Together agent model.
   - It produces a JSONL dataset of conversations and agent responses.

2) Judge with Together Evals
   - The notebook uploads the dataset to Together and starts an evaluation job with the judge system prompt in `configs/judge_system_prompt.jinja`.
   - You can choose scoring and pass/fail thresholds in `simulation_config.json`.
   - Results are polled and summarized in‑notebook, including per‑item scores, pass status, and rationale.

### Tips for high fidelity
- Use larger, instruction‑tuned Together models for the agent when realism matters.
- Tune `num_exchanges` to capture longer task flows.
- Use TraitBasis `mix_traits` to combine complementary persona traits for broader behavioral coverage.
- Adjust temperatures for both TraitBasis prompting and the agent to balance diversity vs. determinism.

### Outputs
- JSONL dataset of simulated conversations and agent responses
- JSONL evaluation results with score/pass/rationale
- Inline summaries to help you iterate on prompts, personas, and thresholds

### Troubleshooting
- Authentication errors: confirm `TOGETHER_API_KEY` is exported in the active shell.
- Rate limits/timeouts: lower `max_concurrency`, increase `timeout`, or add `rate_limit_retries` in `simulation_config.json`.
- Empty results: verify `traitmix_config_file` points to an existing `configs/traitmix_config_*.json` and the judge prompt path is valid.

### Learn more
- Together models and API: `https://docs.together.ai/`
- Collinear simulations overview: see `simulations/README.md` one level up.
