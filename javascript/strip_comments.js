function solution(input, markers) {
let output = input.split("\n");
    console.log(output);
    for (let i = 0; i < output.length; i++){
      for (let j = 0; j < output[i].length; j++){
        for (let k = 0; k < markers.length; k++){
          if (output[i][j] === markers[k]){
            output[i] = output[i].slice(0,j).trim();
          }
        }
      }
    }
    output = output.join("\n")
    return output;
  };
  
entrada = "apples, plums % and bananas\npears\noranges !applesauce";
marcadores = ["%", "!"];

console.log(solution(entrada, marcadores));