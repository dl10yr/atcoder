"use strict";
// inputに入力データ全体が入る
function Main(input) {
    // 1行目がinput[0], 2行目がinput[1], …に入る
    input = input.split("\n");
    const tmp = input[0].split(" ");
  	const n = Number(tmp[0])
  	const x = Number(tmp[1])
  	const a = input[1].split(' ').map(d => Number(d)).filter(d => d !== n && d !==x)
  	console.log(a.join(' '))
}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require("fs").readFileSync("/dev/stdin", "utf8"));