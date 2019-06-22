var str ='{"name":"小强","age":16,"msg":["a","b"],"regex": "^http://.*"}';
var json = JSON.parse(str);
console.log("name:" + json.name);
console.log("msgLen:" + json.msg.length);

// 结果
// name:小强
// msgLen:2