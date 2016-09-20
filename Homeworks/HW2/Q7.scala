/**
  * Created by shivangi on 20/09/16.
  */
object Q7 {

  def main(args: Array[String]){
    print("Enter a number: ")
    val x = readInt()
    print("Enter a power: ")
    val n = readInt()
    println(fastPower(x, n))

  }

  def fastPower(x: Int, n: Int) : BigInt = {
    if (x == 0) {0}
    else if (x == 1 || n == 0) {1}
    else if (n%2 == 1) {x * fastPower(x, n-1)} //divide into x * even power of x and apply function
    else {fastPower(x, n/2) * fastPower(x, n/2)} //divide into x(n/2) * x(n/2) recursively
  }



}
