// Note: an env capable of running cpp is required to execute this.

/*
Pseudocode
-----------
f(array)
    n := array size
    define three ints i_0, i_1, i_2
    
    // initialize the 3 variables just like
    // we did for our dp array
   
    i_1 := array[n-1]
    i_2 := 0

    // this is just to handle the case where the loop
    // doesn't even run for a single iteration -- when
    // the array has a single element.
    
    i_0 := i_1

    // run the loop, updating the variables similar
    // to the array implementation.
    for(i = n-2 -> 0)
        i_0 := max(array[i] + i_2, i_1)
        i_2 := i_1
        i_1 := i_0

    return i_0
*/

#include <iostream.h>
#include <std/c++.h>

using namespace as std;

int main()
{
    vector <int> array = {5, 10, 100, 10, 5}
    cout << f(array) << endl;
  
    return 0;
}

int f(vector <int> &array)
{
    n = array.size();
    
    int i_0, i_1, i_2;

    // these variables handle our base cases
    i_1 = array[n-1];
    i_2 = 0;
    
    // this line handles the case where the input array
    // has a single element
    i_0 = i_1;
  
    // iteratively update all three variables
    // based on our recurrence relation.
    for(i = n-2; i >= 0; i--)
    {
        i_0 = max(array[i] + i_2, i_1);
        i_2 = i_1;
        i_1 = i_0;
    }

    // the final answer is in i_0
    return i_0;
}