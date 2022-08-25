// 1
// function drawL(event) {
//     const size = Number(event.target.value);
//     const outputElement = document.getElementById('output');
  
//     let output = '';
//     for (i = 0; i < size - 1; i++) {
//       output += 'L<br>';
//     }
//     for (i = 0; i < size; i++) {
//       output += 'L'
//     }
//     outputElement.innerHTML = output; 
//   }
  
//   document.getElementById('size').addEventListener('input', drawL)
  

// 2
// function drawC(event) {
//     const size = Number(event.target.value);
//     const outputElement = document.getElementById('output');
  
//     if (size < 3) {
//       outputElement.innerHTML = 'C letter size must be at least 3';
//       return;
//     }
  
//     let output = '';
//     for (i = 0; i < size; i++) {
//       output += 'C'
//     }
//     output += '<br>'
//     for (i = 0; i < size - 2; i++) {
//       output += 'C<br>';
//     }
//     for (i = 0; i < size; i++) {
//       output += 'C'
//     }
//     outputElement.innerHTML = output;
//   }
  
//   document.getElementById('size').addEventListener('input', drawC)

// 3
// function addNameToList(event) {
//     const name = event.target.value.trim();
//     const outputElement = document.getElementById('output');
//     if (name) {
//       outputElement.innerText += `${name}, `;
//     }
//   }
  
//   document.getElementById('name').addEventListener('blur', addNameToList);

// 4

// function alertNearestNumber(n1, n2) {
//     if (Math.abs(100 - n1) > Math.abs(100 - n2)) {
//       alert(n2);
//     }
//     else {
//       alert(n1);
//     }
//   }
  
//   function handleFormSubmit(event) {
//     event.preventDefault();
//     const n1 = Number(document.getElementById('number1').value);
//     const n2 = Number(document.getElementById('number2').value);
//     alertNearestNumber(n1, n2);
//   }
  
//   document.querySelector('form').addEventListener('submit', handleFormSubmit);

// 5

// let randomNumber = Math.floor(Math.random() * 5) + 1;
// console.log(randomNumber);

// function guessNumber(event) {
//   event.preventDefault();
//   const guessedNumber = Number(document.getElementById('guess').value);
//   if (randomNumber === guessedNumber) {
//     alert("Atspėjai, numeris buvo " + randomNumber)
//   }
//   else {
//     alert("Neatspėjai, numeris buvo " + randomNumber)
//   }
// }

// document.querySelector('form').addEventListener('submit', guessNumber);

// 6

// let counter = 0;
// let randomNumber = Math.floor(Math.random() * 5) + 1;
// console.log(randomNumber);

// function guessNumber(event) {
//   event.preventDefault();
//   counter++;
//   const guessedNumber = Number(document.getElementById('guess').value);
//   if (randomNumber === guessedNumber) {
//     alert(`Atspėjai iš ${counter} karto`);
//   }
//   else {
//     alert("Neatspėjai");
//   }
// }

// document.querySelector('form').addEventListener('submit', guessNumber);