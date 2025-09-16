# Collinear Simulations
Generate realistic, high-fidelity, multi-turn user interactions conditioned on user intents and user personas (traits and attributes). Simulations can be used to evaluate agents, to create training data for long horizon RL training, or to prototype product flows.

Demo notebooks can be found in the `examples/` directory. Contact info@collinear.ai for an API key to generate high quality synthetic data.

## ✨ Features
- Personas by design: Compose personas from personality traits and user attributes (e.g., age, gender, occupations, location).
- Intent control: Drive conversations with an intent taxonomy (e.g., billing dispute, cancellation, upgrade, tech support).
- Multi-turn realism: User personas that do not fade even after >25 turns.
- Pluggable agents: Use your own Assistant API (open or closed source) to benchmark against or create custom evals for
- Evaluation hooks: Intent understanding, query resolution, looping behavior, knowledge gaps, customer satisfaction, tone, empathy, etc.
- RL-friendly: Push to Prime Intellect hub with single line of code.

