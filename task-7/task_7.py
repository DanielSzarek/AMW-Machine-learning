import itertools
import pandas as pd


def activation_function(data):
    return 0 if data < 0 else 1


def calculate_neuron(inputs, weigths, bias_weight, bias=1):
    neuron_sum = bias * bias_weight

    for x, w in zip(inputs, weigths):
        neuron_sum += x * w
    return neuron_sum


def and_neuron():
    bias_weight = -1.5
    weigths = [1, 1]
    outputs = []
    activation_function_outputs = []

    inputs = [i for i in itertools.product([0, 1], repeat=2)]
    for input_tuple in inputs:
        neuron_value = calculate_neuron(input_tuple, weigths, bias_weight)
        outputs.append(neuron_value)
        activation_function_outputs.append(activation_function(neuron_value))

    df = pd.DataFrame(inputs, columns={"X1", "X2"})
    df["-1.5+X1+X2"] = outputs
    df["a"] = activation_function_outputs
    return df


def or_neuron():
    bias_weight = -0.5
    weigths = [1, 1]
    outputs = []
    activation_function_outputs = []

    inputs = [i for i in itertools.product([0, 1], repeat=2)]
    for input_tuple in inputs:
        neuron_value = calculate_neuron(input_tuple, weigths, bias_weight)
        outputs.append(neuron_value)
        activation_function_outputs.append(activation_function(neuron_value))

    df = pd.DataFrame(inputs, columns={"X1", "X2"})
    df["-0.5+X1+X2"] = outputs
    df["a"] = activation_function_outputs
    return df


def not_neuron():
    bias_weight = 1
    weigths = [-2]
    outputs = []
    activation_function_outputs = []

    inputs = [i for i in itertools.product([0, 1], repeat=1)]
    for input_tuple in inputs:
        neuron_value = calculate_neuron(input_tuple, weigths, bias_weight)
        outputs.append(neuron_value)
        activation_function_outputs.append(activation_function(neuron_value))

    df = pd.DataFrame(inputs, columns={"X1"})
    df["1-2X1"] = outputs
    df["a"] = activation_function_outputs
    return df


def xnor_neuron():
    bias_weights_a1 = 0.5
    weigths_a1 = [-1, -1]
    activation_function_outputs_a1 = []

    bias_weights_a2 = -1.5
    weigths_a2 = [1, 1]
    activation_function_outputs_a2 = []

    inputs = [i for i in itertools.product([0, 1], repeat=2)]

    for input_tuple in inputs:
        neuron_value = calculate_neuron(input_tuple, weigths_a1, bias_weights_a1)
        activation_function_outputs_a1.append(activation_function(neuron_value))

        neuron_value = calculate_neuron(input_tuple, weigths_a2, bias_weights_a2)
        activation_function_outputs_a2.append(activation_function(neuron_value))

    bias_weights_a3 = -0.5
    weigths_a3 = [1, 1]
    outputs = []
    activation_function_outputs_a3 = []
    for i_1, i_2 in zip(activation_function_outputs_a1, activation_function_outputs_a2):
        output = bias_weights_a3 + i_1 * weigths_a3[0] + i_2 * weigths_a3[0]
        outputs.append(output)
        activation_function_outputs_a3.append(activation_function(output))

    df = pd.DataFrame(inputs, columns={"X1", "X2"})
    df["XNOR"] = outputs
    df["a"] = activation_function_outputs_a3
    return df


def xor_neuron():
    bias_weights_a1 = -0.5
    weigths_a1 = [1, 1]
    activation_function_outputs_a1 = []

    bias_weights_a2 = 1.5
    weigths_a2 = [-1, -1]
    activation_function_outputs_a2 = []

    inputs = [i for i in itertools.product([0, 1], repeat=2)]

    for input_tuple in inputs:
        neuron_value = calculate_neuron(input_tuple, weigths_a1, bias_weights_a1)
        activation_function_outputs_a1.append(activation_function(neuron_value))

        neuron_value = calculate_neuron(input_tuple, weigths_a2, bias_weights_a2)
        activation_function_outputs_a2.append(activation_function(neuron_value))

    bias_weights_a3 = -1.5
    weigths_a3 = [1, 1]
    outputs = []
    activation_function_outputs_a3 = []
    for i_1, i_2 in zip(activation_function_outputs_a1, activation_function_outputs_a2):
        output = bias_weights_a3 + i_1 * weigths_a3[0] + i_2 * weigths_a3[0]
        outputs.append(output)
        activation_function_outputs_a3.append(activation_function(output))

    df = pd.DataFrame(inputs, columns={"X1", "X2"})
    df["XOR"] = outputs
    df["a"] = activation_function_outputs_a3
    return df


if __name__ == "__main__":
    print("AND:")
    print(and_neuron())
    print("\nOR: ")
    print(or_neuron())
    print("\nNOT: ")
    print(not_neuron())
    print("\nXNOR: ")
    print(xnor_neuron())
    print("\nXOR: ")
    print(xor_neuron())
