import tensorflow as tf
import tensorflow_datasets as tfds

# Sample conversation pairs
conversations = [
    ("Hi", "Hello!"),
    ("How are you?", "I'm a chatbot, I don't have feelings, but I'm here to help!"),
    ("Tell me a joke", "Why did the computer go to therapy? Because it had too many bugs!"),
    # ... add more conversation pairs ...
]

# Prepare data
questions = [conv[0] for conv in conversations]
answers = [conv[1] for conv in conversations]

# Tokenize data
tokenizer = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(questions + answers, target_vocab_size=2**13)
START_TOKEN, END_TOKEN = [tokenizer.vocab_size], [tokenizer.vocab_size + 1]
VOCAB_SIZE = tokenizer.vocab_size + 2

# Convert text to sequences of tokens
questions = [START_TOKEN + tokenizer.encode(question) + END_TOKEN for question in questions]
answers = [START_TOKEN + tokenizer.encode(answer) + END_TOKEN for answer in answers]

# Create TensorFlow Dataset
MAX_LENGTH = 40
def filter_max_length(x, y, max_length=MAX_LENGTH):
    return tf.logical_and(tf.size(x) <= max_length, tf.size(y) <= max_length)

data = tf.data.Dataset.from_tensor_slices(({
    'inputs': questions,
    'dec_inputs': answers[:, :-1]
}, {
    'outputs': answers[:, 1:]
}))

# Filter out sequences that are too long
data = data.filter(filter_max_length)

# Pad sequences to a fixed length
BATCH_SIZE = 64
data = data.padded_batch(BATCH_SIZE, padded_shapes=([None], [None]))


# Build and compile the model
def transformer(vocab_size, num_layers, units, d_model, num_heads, dropout, name="transformer"):
    inputs = tf.keras.layers.Input(shape=(None,), name="inputs")
    dec_inputs = tf.keras.layers.Input(shape=(None,), name="dec_inputs")

    # Embedding layers
    input_embed = tf.keras.layers.Embedding(vocab_size, d_model)(inputs)
    dec_embed = tf.keras.layers.Embedding(vocab_size, d_model)(dec_inputs)

    # Encoder
    encoder_outputs = input_embed
    for _ in range(num_layers):
        encoder_outputs = tf.keras.layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=d_model, dropout=dropout
        )(encoder_outputs, encoder_outputs)
        encoder_outputs = tf.keras.layers.Dropout(dropout)(encoder_outputs)
        encoder_outputs = tf.keras.layers.LayerNormalization(epsilon=1e-6)(encoder_outputs)

    # Decoder
    decoder_outputs = dec_embed
    for _ in range(num_layers):
        decoder_outputs = tf.keras.layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=d_model, dropout=dropout
        )(decoder_outputs, decoder_outputs)
        decoder_outputs = tf.keras.layers.Dropout(dropout)(decoder_outputs)
        decoder_outputs = tf.keras.layers.LayerNormalization(epsilon=1e-6)(decoder_outputs)

        decoder_outputs = tf.keras.layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=d_model, dropout=dropout
        )(decoder_outputs, encoder_outputs)
        decoder_outputs = tf.keras.layers.Dropout(dropout)(decoder_outputs)
        decoder_outputs = tf.keras.layers.LayerNormalization(epsilon=1e-6)(decoder_outputs)

    outputs = tf.keras.layers.Dense(vocab_size, activation="softmax")(decoder_outputs)

    model = tf.keras.models.Model(inputs=[inputs, dec_inputs], outputs=outputs, name=name)
    return model

model = transformer(
    vocab_size=VOCAB_SIZE,
    num_layers=4,
    units=128,
    d_model=256,
    num_heads=4,
    dropout=0.3
)

model.compile(optimizer=tf.keras.optimizers.Adam(0.0001, beta_1=0.9, beta_2=0.98, epsilon=1e-9),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True, reduction='none'),
              metrics=[tf.keras.metrics.SparseCategoricalAccuracy('accuracy')])

# Train the model
EPOCHS = 50
model.fit(data, epochs=EPOCHS)