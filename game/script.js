function getComputerChoice() {
    const choices = ['rock', 'paper', 'scissors'];
    const randomIndex = Math.floor(Math.random() * 3);
    return choices[randomIndex];
}

function determineWinner(playerChoice, computerChoice) {
    if (playerChoice === computerChoice) {
        return "It's a tie!";
    }
    
    if (
        (playerChoice === 'rock' && computerChoice === 'scissors') ||
        (playerChoice === 'scissors' && computerChoice === 'paper') ||
        (playerChoice === 'paper' && computerChoice === 'rock')
    ) {
        return 'You win!';
    } else {
        return 'You lose!';
    }
}

document.querySelectorAll('#buttons button').forEach(button => {
    button.addEventListener('click', () => {
        const playerChoice = button.id;
        const computerChoice = getComputerChoice();
        playGame(playerChoice, computerChoice);
    });
});

function playGame(playerChoice, computerChoice) {
    document.getElementById('playerChoice').src = `${playerChoice}.png`;
    document.getElementById('computerChoice').src = `${computerChoice}.png`;
    const result = determineWinner(playerChoice, computerChoice);
    document.getElementById('result').textContent = `Computer chose ${computerChoice}. ${result}`;
}
