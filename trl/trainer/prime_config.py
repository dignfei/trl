# Copyright 2025 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass, field
from typing import Optional

from transformers import TrainingArguments


@dataclass
class PrimeConfig(TrainingArguments):
    r"""
    Configuration class for the [`PrimeConfig`].

    Only the parameters specific to PRIME training are listed here. For details on other parameters, refer to the
    [`~transformers.TrainingArguments`] documentation.

    Using [`~transformers.HfArgumentParser`] we can turn this class into
    [argparse](https://docs.python.org/3/library/argparse#module-argparse) arguments that can be specified on the
    command line.

    Parameters:
        > Parameters that control the model and reference model

        model_init_kwargs (`dict[str, Any]` or `None`, *optional*, defaults to `None`):
            Keyword arguments for [`~transformers.AutoModelForCausalLM.from_pretrained`], used when the `model`
            argument of the [`PrimeTrainer`] is provided as a string.

        > Parameters that control the data preprocessing

        max_prompt_length (`int` or `None`, *optional*, defaults to `512`):
            Maximum length of the prompt. If the prompt is longer than this value, it will be truncated left.
        num_generations (`int` or `None`, *optional*, defaults to `8`):
            Number of generations per prompt to sample.
        temperature (`float`, *optional*, defaults to `0.9`):
            Temperature for sampling. The higher the temperature, the more random the completions.
        max_completion_length (`int` or `None`, *optional*, defaults to `None`):
            Maximum length of the generated completion.
        use_vllm (`bool`, *optional*, defaults to `False`):
            Whether to use vLLM for generating completions. Requires vLLM to be installed (`pip install vllm`).

        > Parameters that control the training

        learning_rate (`float`, *optional*, defaults to `1e-6`):
            Initial learning rate for [`AdamW`] optimizer. The default value replaces that of
            [`~transformers.TrainingArguments`].
        beta (`float`, *optional*, defaults to `0.04`):
            KL coefficient.
    """

    # Parameters that control the model and reference model
    model_init_kwargs: Optional[dict] = field(
        default=None,
        metadata={
            "help": "Keyword arguments for `transformers.AutoModelForCausalLM.from_pretrained`, used when the `model` "
            "argument of the `PrimeTrainer` is provided as a string."
        },
    )

    # Parameters that control the data preprocessing
    max_prompt_length: Optional[int] = field(
        default=512,
        metadata={
            "help": "Maximum length of the prompt. If the prompt is longer than this value, it will be truncated left."
        },
    )
    num_generations: Optional[int] = field(
        default=8,
        metadata={"help": "Number of generations to sample."},
    )
    temperature: Optional[float] = field(
        default=0.9,
        metadata={"help": "Temperature for sampling. The higher the temperature, the more random the completions."},
    )
    max_completion_length: Optional[int] = field(
        default=256,
        metadata={"help": "Maximum length of the generated completion."},
    )
    use_vllm: Optional[bool] = field(
        default=False,
        metadata={
            "help": "Whether to use vLLM for generating completions. Requires vLLM to be installed "
            "(`pip install vllm`)."
        },
    )

    # Parameters that control the training
    learning_rate: float = field(
        default=1e-6,
        metadata={
            "help": "Initial learning rate for `AdamW` optimizer. The default value replaces that of "
            "`transformers.TrainingArguments`."
        },
    )
    beta: float = field(
        default=0.04,
        metadata={"help": "KL coefficient."},
    )
    correct_ratio_min: float = field(
        default=0.2,
        metadata={"help": "Minimum ratio of correct responses required to keep a prompt batch."},
    )
    correct_ratio_max: float = field(
        default=0.8,
        metadata={"help": "Maximum ratio of correct responses allowed to keep a prompt batch."},
    )
    num_ppo_epochs: int = field(
        default=4,
        metadata={"help": "Number of PPO epochs to run per batch (M in the PRIME paper)."},
    )
    gamma: float = field(
        default=1.0,
        metadata={"help": "Discount factor for future rewards in advantage estimation."},
    )
    epsilon: float = field(
        default=0.2,
        metadata={"help": "PPO clip range for policy updates."},
    )
