from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='llavanext-v1.5-0.5b',
        path='/root/autodl-tmp/models/llavanext-v1.5-0.5b',
        max_out_len=32768,
        batch_size=4,
        run_cfg=dict(num_gpus=2),
    )
]
