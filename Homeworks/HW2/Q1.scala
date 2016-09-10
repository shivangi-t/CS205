/**
  * Created by shivangi on 06/09/16.
  */
object Q1 {

  def main(args: Array[String]) {
    print("Enter a number: ")
    val n = readInt()
    println("The factorial is " + factorial(n))
  }

  def factorial(n: Int): Int = n match {
    case 0 => 1
    case _ => n * factorial(n - 1) //recursive call to factorial function for previous number
  }
}
