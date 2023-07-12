
// 1

for (let i = 1; i <= 10; i++) {
    if (i % 2 !== 0) {
      console.log(i);
    }
  }

// 2

const masyvas = ['Obuolys', 'Bananas', 'Kriaušė', 'Slyva'];

for (const elementas of masyvas) {
  console.log(elementas);
}

// 3

const masyvas2 = [5, 10, 15, 20];
let suma = 0;

masyvas2.forEach((sk) => {
  suma += sk;
});

console.log(suma);
