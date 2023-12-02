from mycrograd_debug.drawviz_debug import (
    draw_dot,
    draw_nn,
    print_all_values,
    print_my_params,
)

debug_parameters = False
debug_values = False


def debugFunc(model, options, message="", inputs=[], targets=[]):
    if message:
        print(message)
    if "parameters" in options:
        print("parameters")
        print_my_params(model)
    if inputs:
        print("inputs")
        print(inputs)
    if "targets" in options:
        print("targets")
        print(targets)
    if debug_parameters:
        print_my_params(model)
    # if debug_values:
    #     print_all_values(activation)
