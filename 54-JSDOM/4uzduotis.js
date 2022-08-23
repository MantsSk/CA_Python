// 1

// document.querySelector('h1').addEventListener('click', (event) => {
//     event.target.style.textAlign = "center";
//     event.target.style.fontSize = "4rem";
//     event.target.style.color = "red";
//   });

// 2-3 
// const button = document.querySelector('button');
// button.style.cssText = 'position:absolute; top:0; left:0;';

// let isInOriginalPosition = true;
// function changePosition() {
//   event.target.style.cssText = isInOriginalPosition ? 'position:absolute; bottom:0; right:0;' : 'position:absolute; top:0; left:0;';
//   isInOriginalPosition = !isInOriginalPosition;
// }

// button.addEventListener('click', changePosition);

// 3
// const button = document.querySelector('button');
// button.style.cssText = 'position:absolute; top:0; left:0';

// let corner = 0;
// const cornerStyles = ['position:absolute; top:0; right:0;', 'position:absolute; bottom:0; right:0;', 'position:absolute; bottom:0; left:0;', 'position:absolute; top:0; left:0;'];
// function changePosition(event) {
//   if (corner < cornerStyles.length) {
//     event.target.style.cssText = cornerStyles[corner];
//     corner++;
//   }
//   if (corner === cornerStyles.length) {
//     corner = 0;
//   }
// }

// button.addEventListener('click', changePosition);
