function isPalindrome(string) {
    const reversedString = string.split('').reverse().join('');
    return string === reversedString;
  }
  
  function filterPalindromes(strings) {
    const palindromes = [];
  
    for (const string of strings) {
      if (isPalindrome(string)) {
        palindromes.push(string);
      }
    }
  
    return palindromes;
  }
  
  const words = ['level', 'radar', 'hello', 'madam', 'world'];
  const palindromes = filterPalindromes(words);
  
  console.log(palindromes);
