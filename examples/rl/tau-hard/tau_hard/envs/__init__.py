# Copyright Sierra

from typing import Optional, Union
from tau_hard.envs.base import Env
from tau_hard.envs.user import UserStrategy
from typing import Dict, Any

def get_env(
    env_name: str,
    user_strategy: Union[str, UserStrategy],
    user_model: str,
    task_split: str,
    user_provider: Optional[str] = None,
    task_index: Optional[int] = None,
    trait_dict: Optional[Dict[str, Any]] = None,
) -> Env:
    if env_name == "retail":
        from tau_hard.envs.retail import MockRetailDomainEnv

        return MockRetailDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
            trait_dict=trait_dict,
        )
    elif env_name == "airline":
        from tau_hard.envs.airline import MockAirlineDomainEnv

        return MockAirlineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
            trait_dict=trait_dict,
        )
    else:
        raise ValueError(f"Unknown environment: {env_name}")
