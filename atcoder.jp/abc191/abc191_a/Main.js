"use strict";
// inputに入力データ全体が入る
function Main(input) {
    // 1行目がinput[0], 2行目がinput[1], …に入る
    input = input.split("\n");
    const tmp = input[0].split(" ");
  	const v = Number(tmp[0])
  	const t = Number(tmp[1])
  	const s = Number(tmp[2])
  	const d = Number(tmp[3])
  	const time = v / t
    if (d/v >= t && d/v <= s) {
      console.log('No')
    } else {
		console.log('Yes')
    }
  
}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require("fs").readFileSync("/dev/stdin", "utf8"));