function calculateSalary() {
    const speed1 = Number(document.getElementById('speed1').value) || 0;
    const speed2 = Number(document.getElementById('speed2').value) || 0;
    const speed3 = Number(document.getElementById('speed3').value) || 0;
    const speed4 = Number(document.getElementById('speed4').value) || 0;

    const speedCount = speed1 + speed2 * 2 + speed3 * 3 + speed4 * 4;

    let wagePerSpeed;
    if (speedCount <= 20) wagePerSpeed = 6.75;
    else if (speedCount <= 25) wagePerSpeed = 7;
    else if (speedCount <= 30) wagePerSpeed = 7.25;
    else if (speedCount <= 35) wagePerSpeed = 7.5;
    else if (speedCount <= 40) wagePerSpeed = 7.75;
    else if (speedCount <= 45) wagePerSpeed = 8;
    else if (speedCount <= 50) wagePerSpeed = 8.25;
    else if (speedCount <= 55) wagePerSpeed = 8.5;
    else if (speedCount <= 60) wagePerSpeed = 8.75;
    else if (speedCount <= 65) wagePerSpeed = 9;
    else if (speedCount <= 70) wagePerSpeed = 9.25;
    else if (speedCount <= 75) wagePerSpeed = 9.5;
    else wagePerSpeed = 9.75;

    // Calculate new wage using individual multipliers
    const newWage = (
        speed1 * wagePerSpeed +
        speed2 * wagePerSpeed * 2 +
        speed3 * wagePerSpeed * 2.66 +
        speed4 * wagePerSpeed * 3.33
    );

    // Display the result
    document.getElementById('result').innerHTML = 
        `Your wage per speed is Gel ${wagePerSpeed.toFixed(2)}<br>
        Your salary is Gel ${newWage.toFixed(2)}`;
}
