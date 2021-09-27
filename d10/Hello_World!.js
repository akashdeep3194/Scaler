module.exports = { 
    //param A : array of integers
    //return a array of integers
       solve : function(A,B){
              const arr = []
              for (var i=0;i<A.length;i++){
                  arr.push(A[i]+B)
              }
              return arr
       }
    };
    var solveObj = require('./Hello_World!.js')
    console.log(solveObj.solve([1,2,3,4],2))
