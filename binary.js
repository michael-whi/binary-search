var array = [1,2,3,4,5,6]
function binary_search(array, item){
     let low = 0
     let high = array.length-1

     while(low <= high){
         console.log("========")
         let mid = Math.floor((low+high)/2)
         console.log(low, mid, high)
         let guess = array[mid]
         if(guess === item){
             return item
         }
         if(guess > item){
             high = mid
         }else{
             low = mid
         }
    }
 return null
}

binary_search(array, 4)