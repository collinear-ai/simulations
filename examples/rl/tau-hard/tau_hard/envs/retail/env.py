# Copyright Sierra

from tau_hard.envs.base import Env
from tau_hard.envs.retail.data import load_data
from tau_hard.envs.retail.rules import RULES
from tau_hard.envs.retail.tools import ALL_TOOLS
from tau_hard.envs.retail.wiki import WIKI
from typing import Optional, Union
from tau_hard.envs.user import UserStrategy
from typing import Dict, Any


class MockRetailDomainEnv(Env):
    def __init__(
        self,
        user_strategy: Union[str, UserStrategy] = UserStrategy.LLM,
        user_model: str = "gpt-4o",
        user_provider: Optional[str] = None,
        task_split: str = "test",
        task_index: Optional[int] = None,
        trait_dict: Optional[Dict[str, Any]] = None,
    ):
        match task_split:
            case "test":
                from tau_hard.envs.retail.tasks_test import TASKS_TEST as tasks
            case "train":
                from tau_hard.envs.retail.tasks_train import TASKS_TRAIN as tasks
            case "dev":
                from tau_hard.envs.retail.tasks_dev import TASKS_DEV as tasks
            case _:
                raise ValueError(f"Unknown task split: {task_split}")
        super().__init__(
            data_load_func=load_data,
            tools=ALL_TOOLS,
            tasks=tasks,
            wiki=WIKI,
            rules=RULES,
            user_strategy=user_strategy,
            user_model=user_model,
            user_provider=user_provider,
            task_index=task_index,
            trait_dict=trait_dict,
        )
        self.terminate_tools = ["transfer_to_human_agents"]
