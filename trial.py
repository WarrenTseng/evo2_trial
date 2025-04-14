# Source: https://github.com/ArcInstitute/evo2

import torch
from evo2 import Evo2  # Import the Evo2 model from the evo2 package

# Load the pre-trained Evo2 model (7B variant)
evo2_model = Evo2('evo2_7b')

# Define the input DNA sequence
sequence = 'ACGT'

# Tokenize the sequence and convert it to a tensor suitable for the model
input_ids = torch.tensor(
    evo2_model.tokenizer.tokenize(sequence),  # Convert DNA string to token IDs
    dtype=torch.int,                          # Set data type as integer
).unsqueeze(0).to('cuda:0')                   # Add batch dimension and move to GPU

# Specify the name of the layer from which you want to extract embeddings
layer_name = 'blocks.28.mlp.l3'

# Run the model on the input sequence and request embeddings from the specified layer
outputs, embeddings = evo2_model(
    input_ids,
    return_embeddings=True,          # Ensure embeddings are returned
    layer_names=[layer_name],        # Specify which layer's embeddings to extract
)

# Print the shape of the embeddings extracted from the chosen layer
print('Embeddings shape: ', embeddings[layer_name].shape)
