function checkGuess() {
    var guess = parseInt(document.getElementById("guess").value);
    var message = document.getElementById("message");

    // Call the Pygbag-converted function to check the guess
    var result = check_guess(guess);

    // Display the result
    message.textContent = result;
}
