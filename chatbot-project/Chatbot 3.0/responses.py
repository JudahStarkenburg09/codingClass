responses = [
    {
        "in": [r"^(?: )*(hi|hello|whats( )*up|salutations|sup|hilo|greetings)(?: )*(?:\w*)?(?: )*$"],
        "out": ["Hi!", "Hello!", "Salutations!"],
    },
    {
        "in": [r"^(?: )*(?:\w*)?(?: )*(how( )*are( )*you|hows( )*it( )*going|what( )*is( )*up|howdy|hey)(?: )*(?:\w*)?(?: )*$"],
        "out": ["I'm doing well, thank you!", "I'm good, how about you?", "All good!"],
    },
    {
        "in": [r"^(?: )*(bye|goodbye|see( )*you|farewell|adios|take( )*care)(?: )*(?:\w*)?(?: )*$"],
        "out": ["Goodbye!", "See you later!", "Farewell!"],
    },
    {
        "in": [r"^(?: )*what(?:s| is) your name\??(?: )*(?:\w*)?(?: )*$"],
        "out": ["I'm a computer program, so you can call me Linus!"],
    },
    {
        "in": [r"^(?: )*(?:\w(?: )*)?(good|ok|decent|fantastic|great|wonderful|excellent|superb|amazing|splendid|oustanding|marvelous|fabulous|exceptional|tremendous)(?: )*(?:\w(?: )*){0,2}$"],
        "out": ["Nice.", "That's good."],
    },
    {
        "in": [r"^(?: )*(?:\w(?: )*)?(bad|awful|trash|garbage)(?: )*(?:\w(?: )*){0,2}$"],
        "out": ["I'm sorry to hear that!", "Oh no!", "I hope it gets better!"],
    }
]
