function addStrings(str1, str2){
    str1a = str1.split('').reverse();
    str2a = str2.split('').reverse();
    var output = '';
    var longer = Math.max(str1.length, str2.length);
    var carry = false;
    for (var i = 0; i < longer; i++) {
      var result = 0;
      if (str1a[i] && str2a[i]) {
        result = parseInt(str1a[i]) + parseInt(str2a[i]);
  
      } else if (str1a[i] && !str2a[i]) {
        result = parseInt(str1a[i]);
  
      } else if (!str1a[i] && str2a[i]) {
        result = parseInt(str2a[i]);
      }
  
      if (carry) {
          result += 1;
          carry = false;
      }
      if(result >= 10) {
        carry = true;
        output += result.toString()[1];
      }else {
        output += result.toString();
      }
    }
    output = output.split('').reverse().join('');
  
    if(carry) {
      output = '1' + output;
    }
    return output;
  }

var fs = require('fs');
var input = parseInt(fs.readFileSync('/dev/stdin').toString().trim());

var end_1 = '1'
var end_0 = '0'
for (var i = 1; i < input; i++) {
    var new_end_0 = addStrings(end_0, end_1);
    var new_end_1 = end_0;
    end_0 = new_end_0;
    end_1 = new_end_1;
}
console.log(addStrings(end_0, end_1));