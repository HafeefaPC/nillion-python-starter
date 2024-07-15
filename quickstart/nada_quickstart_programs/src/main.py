from nada_dsl import *

def nada_main():
    # Define the parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party4 = Party(name="Party4")

    # Define secret inputs
    x = SecretInteger(Input(name="X", party=party1))
    y = SecretInteger(Input(name="Y", party=party2))

    # Perform some operations
    sum_result = x + y
    product_result = x * y

    # Define the output
    return [Output(sum_result, "sum_output", party4), Output(product_result, "product_output", party4)]
