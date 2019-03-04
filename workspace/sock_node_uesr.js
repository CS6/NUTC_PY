/*
sock 客戶端程式
等待0.1秒送出請求
*/
var net = require('net');
var client = net.connect({ path: '/tmp/movit.sock' },
    function () { //'connect' listener
        console.log('connected to server!');
        client.write('world!\r\n');
    });


function delay(ms) {
    return new Promise(solve => setTimeout(solve, ms));
} 


var msg = "YAYAYA";
var mun = 0 ;
async function main()  {
    for (var times = 0; times < 100; times++) {
        client.write(msg+mun);
        console.log(msg+mun);
        await delay(1000);
        mun=mun + 1;
    }
}

main();



// while (i < 100) {
    // setInterval(() => {
    //     client.write(msg + i);
    //     console.log(msg + i)
    //     i = i + 1
    // }, 1000);
//     setInterval(function () {
//         console.log("Hello"); 
//        }, 3000);

// }



//    client.write('world2!\r\n');
//var fs = require('fs');

    // var dd
    // dd = JSON.stringify(data);
    // fs.writeFile('test.txt', dd, function (err) {
    //     if (err)
    //         console.log(err)
    //     else
    //         console.log('Write operation complete.');
    // });
    //var p1_data = data.toString();


//fs.writeFile('test.txt', data, function (err) {
//    if (err)
//        console.log(err);
//    else
//        console.log('Write operation complete.');
//});

