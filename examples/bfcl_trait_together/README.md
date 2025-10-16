# BFCL Trait: Function Call Evaluation using Traits for Together Models

## Leaderboard Table (`multi_turn_base`)
| Model (base score) \ Trait | Confusion | Skepticism | Impatience | Incoherence |
|:---|:---:|:---:|:---:|:---:|
| GPT 4o (0.59) | 0.19 (-0.40) | 0.21 (-0.38) | 0.35 (-0.24) | 0.29 (-0.30) |
| Kimi K2 (0.60) | 0.18 (-0.42) | 0.12 (-0.48) | 0.31 (-0.29) | 0.20 (-0.40) |
| GLM 4.5 (0.75) | 0.17 (-0.58) | 0.18 (-0.57) | 0.33 (-0.42) | 0.25 (-0.50) |

> Drop from base show in parenthesis

## File Structure
```
.
├── bfcl_trait_eval/ #bfcl code directory
├──config/ #config directory
└── bfcl_eval_together.ipynb #notebook for running
```

## Pre Requisite
1. Setup `TOGETHER_API_KEY`

```bash
export TOGETHER_API_KEY=<api_key>
```

2. Install `bfcl-eval` using uv or pip
```bash
# Option A: using `uv` (if you have `uv` on PATH)
uv install bfcl-eval

# Option B: using pip (recommended, inside a virtualenv)
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools
pip install bfcl-eval
```

## Config 
### Example config (save as config/config.json)

```json
{
    "model": "moonshotai/Kimi-K2-Instruct-0905",
    "model_type": "together",
    "is_fc_model": false,
    "test_category": [
        "multi_turn_base"
    ],
    "temperature": 0.001,
    "include_input_log": false,
    "exclude_state_log": false,
    "num_threads": 1,
    "skip_server_setup": false,
    "local_model_path": null,
    "result_dir": "result",
    "score_dir": "score",
    "allow_overwrite": false,
    "run_ids": false,
    "trait": "skeptical",
    "intensity": "medium"
}
```

- `model`: model identifier used for Together-hosted evaluation.
- `model_type`: runtime/provider type ("together").
- `is_fc_model`: set true if the model expects function-call style interactions.
- `test_category`: list of test suites to run (e.g., "multi_turn_base").
- `temperature`: sampling temperature for generation.
- `include_input_log` / `exclude_state_log`: control logging detail.
- `num_threads`: parallel worker count.
- `skip_server_setup`: skip any local server bootstrap when true.
- `local_model_path`: path to a locally cached model (null if not used).
- `result_dir` / `score_dir`: output directories for run artifacts and scores.
- `allow_overwrite`: permit overwriting existing outputs.
- `run_ids`: include run identifiers in outputs.
- `trait`: ["confusion", "impatience", "incoherence", "skeptical"]
- `intensity`: ["medium", "high"] intensity of the trait

