# Collinear Simulations
Generate realistic, high-fidelity, multi-turn user interactions conditioned on user intents and user personas (traits and attributes). Simulations can be used to evaluate agents, to create training data for long horizon RL training, or to prototype product flows.

## ✨ Features
- Personas by design: Compose personas from personality traits (with finegrained intensity controls from 1-5 scale) and user attributes (e.g., age, gender, occupations, location).
- Intent control: Drive conversations with an intent taxonomy (e.g., billing dispute, cancellation, upgrade, tech support), or bring your own.
- Multi-turn realism: User personas that do not fade even after >25 turns.
- Pluggable agents: Attach your endpoint, upload or write scripted policies, and support for fine-grained agent description.
- Evaluation hooks: Intent understanding, query resolution, looping behavior, knowledge gaps, customer satisfaction, tone, empathy, etc.
- RL-friendly: Push to Prime Intellect hub with single line of code.

## Installation

```# From source
git clone https://github.com/collinear-ai/simulations.git

cd simulations

pip install -e .[all]
```
## Quick start
```
# Generate 100 conversations across 8 personas and 6 intents
simulate run \
  --agent-model-url $USER_MODEL_URL \
  --agent-api-key $USER_API_KEY \
  --personas config/personas.yaml \
  --intents  config/intents.yaml \
  --n 100 \
  --out data/conversations.jsonl \
```
