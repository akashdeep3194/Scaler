module.exports = { 
    //param A : array of integers
    //return a array of integers
       solve : function(A,B){
              const arr = []
              const ele
              for (ele in A){
                  arr.push(ele+B)
              }
              console.log(arr)
              return arr
       }
   };
   