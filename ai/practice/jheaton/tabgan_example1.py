from tabgan.sampler import (
    OriginalGenerator,
    GANGenerator,
    ForestDiffusionGenerator,
    LLMGenerator,
)
import pandas as pd
import numpy as np


# random input data
train = pd.DataFrame(np.random.randint(-10, 150, size=(150, 4)), columns=list("ABCD"))
target = pd.DataFrame(np.random.randint(0, 2, size=(150, 1)), columns=list("Y"))
test = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list("ABCD"))

# generate data
print("generate data")
print("OriginalGenerator")
new_train1, new_target1 = OriginalGenerator().generate_data_pipe(
    train,
    target,
    test,
)
print("GANGenerator")
new_train2, new_target2 = GANGenerator(
    gen_params={"batch_size": 500, "epochs": 10, "patience": 5}
).generate_data_pipe(
    train,
    target,
    test,
)
# print("ForestDiffusionGenerator")
# new_train3, new_target3 = ForestDiffusionGenerator().generate_data_pipe(train, target, test, )
print("LLMGenerator")
new_train4, new_target4 = LLMGenerator(
    gen_params={"batch_size": 32, "epochs": 4, "llm": "distilgpt2", "max_length": 500}
).generate_data_pipe(
    train,
    target,
    test,
)
print("generate data complete")


# example with all params defined
print("call GANGenerator")
new_train4, new_target4 = GANGenerator(
    gen_x_times=1.1,
    cat_cols=None,
    bot_filter_quantile=0.001,
    top_filter_quantile=0.999,
    is_post_process=True,
    adversarial_model_params={
        "metrics": "AUC",
        "max_depth": 2,
        "max_bin": 100,
        "learning_rate": 0.02,
        "random_state": 42,
        "n_estimators": 100,
    },
    pregeneration_frac=2,
    only_generated_data=False,
    gen_params={
        "batch_size": 500,
        "patience": 25,
        "epochs": 500,
    },
).generate_data_pipe(
    train, target, test, deep_copy=True, only_adversarial=False, use_adversarial=True
)

print("End")
