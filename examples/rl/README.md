# Tau-Hard docs  

In the simulations_RL notebook, we run Tau-Hard (Collinear's version of Tau Bench for Agent robustness testing), leveraging the Collinear TraitBasis technology to improve the realism of the user turns. 

```
import argparse
from tau_hard.types import RunConfig
from tau_hard.run import run
from litellm import provider_list
from tau_hard.envs.user import UserStrategy

from tau_hard.types import RunConfig
from tau_hard.run import run

config = RunConfig(
    model_provider="openai",
    user_model_provider="steer",
    model=CLIENT_ASSISTANT_MODEL_NAME,
    user_model="", # steer api abstracts the model
    num_trials=1,
    env="retail",
    agent_strategy="tool-calling",
    temperature=0.7,
    task_split="test",
    start_index=0,
    end_index=-1,
    task_ids=[4],
    log_dir="results",
    max_concurrency=1,
    seed=10,
    shuffle=0,
    user_strategy="llm",
    few_shot_displays_path=None,
    trait_dict={"impatience": 1, "confusion": 0, "skeptical": 0, "incoherence": 0},
)
```

You can also just set the configurations in `tau_hard_config.json`. The definitions of the settings are below.

## Tau-Hard Config Settings
### General
- **`--num-trials`** *(int, default: 1)*  
  Number of independent trials to run.

- **`--seed`** *(int, default: 10)*  
  Random seed for reproducibility.

- **`--shuffle`** *(int, default: 0)*  
  Whether to shuffle task order (0 = no, 1 = yes).

- **`--log-dir`** *(str, default: `results`)*  
  Directory where logs and results are stored.

### Environment & Tasks
- **`--env`** *(str, choices: `retail`, `airline`, default: `retail`)*  
  Domain environment in which to run simulations.

- **`--task-split`** *(str, choices: `train`, `test`, `dev`, default: `test`)*  
  Dataset split of tasks to run (applies only to the retail domain currently).

- **`--start-index`** *(int, default: 0)*  
  Index of the first task to run.

- **`--end-index`** *(int, default: -1)*  
  Index of the last task to run. Use `-1` to run all remaining tasks.

- **`--task-ids`** *(list of int, optional)*  
  Explicit list of task IDs to run (overrides index ranges).

### Agent Configuration
- **`--model`** *(str, required)*  
  The model to use for the **agent**.

- **`--model-provider`** *(str, choices from `provider_list`)*  
  Provider for the agent’s model.

- **`--agent-strategy`** *(str, choices: `tool-calling`, `act`, `react`, `few-shot`, default: `tool-calling`)*  
  Strategy used by the agent to interact with the environment.  
  - `tool-calling`: Invoke external tools.  
  - `act`: Pure action selection.  
  - `react`: Reason + act alternation.  
  - `few-shot`: Use few-shot exemplars.

- **`--temperature`** *(float, default: 0.0)*  
  Sampling temperature for the action model (higher = more randomness).

- **`--few-shot-displays-path`** *(str, optional)*  
  Path to a JSONL file containing few-shot demonstration examples.

### User Simulator Configuration
- **`--user-model`** *(str, default: `gpt-4o`)*  
  Model to use for the **user simulator**.

- **`--user-model-provider`** *(str, optional)*  
  Provider for the user simulator’s model.

- **`--user-strategy`** *(str, choices from `UserStrategy`, default: `llm`)*  
  Strategy for the simulated user (e.g., LLM-based).

### Execution Controls
- **`--max-concurrency`** *(int, default: 1)*  
  Number of tasks to run in parallel.
