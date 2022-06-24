import os
from typing import Any, Dict

from modelscope.utils.config import Config
from modelscope.utils.constant import Tasks
from ...base import Model, Tensor
from ...builder import MODELS
from .model.generator import Generator
from .model.model_base import ModelBase

__all__ = ['DialogStateTrackingModel']


@MODELS.register_module(Tasks.dialog_state_tracking, module_name=r'space-dst')
class DialogStateTrackingModel(Model):

    def __init__(self, model_dir: str, *args, **kwargs):
        """initialize the test generation model from the `model_dir` path.

        Args:
            model_dir (str): the model path.
            model_cls (Optional[Any], optional): model loader, if None, use the
                default loader to load model weights, by default None.
        """

        super().__init__(model_dir, *args, **kwargs)
        self.model_dir = model_dir
        self.config = kwargs.pop(
            'config',
            Config.from_file(
                os.path.join(self.model_dir, 'configuration.json')))
        self.text_field = kwargs.pop(
            'text_field',
            IntentBPETextField(self.model_dir, config=self.config))

        self.generator = Generator.create(self.config, reader=self.text_field)
        self.model = ModelBase.create(
            model_dir=model_dir,
            config=self.config,
            reader=self.text_field,
            generator=self.generator)

        def to_tensor(array):
            """
            numpy array -> tensor
            """
            import torch
            array = torch.tensor(array)
            return array.cuda() if self.config.use_gpu else array

        self.trainer = IntentTrainer(
            model=self.model,
            to_tensor=to_tensor,
            config=self.config,
            reader=self.text_field)
        self.trainer.load()

    def forward(self, input: Dict[str, Tensor]) -> Dict[str, Tensor]:
        """return the result by the model

        Args:
            input (Dict[str, Any]): the preprocessed data

        Returns:
            Dict[str, np.ndarray]: results
                Example:
                    {
                        'predictions': array([1]), # lable 0-negative 1-positive
                        'probabilities': array([[0.11491239, 0.8850876 ]], dtype=float32),
                        'logits': array([[-0.53860897,  1.5029076 ]], dtype=float32) # true value
                    }
        """
        import numpy as np
        pred = self.trainer.forward(input)
        pred = np.squeeze(pred[0], 0)

        return {'pred': pred}
