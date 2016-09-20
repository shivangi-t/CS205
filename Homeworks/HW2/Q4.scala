/**
  * Created by shivangi on 17/09/16.
  */
object Q4 {

  def main(args: Array[String]): Unit= {
    val list: List[Int] = List(8, 2, 4, 1)
    println(InsertionSort(list))
  }

  def InsertionSort(list: List[Int]): List[Int] = list match {
    case Nil => Nil
    case x::rest => sortInsert(InsertionSort(rest), x)
  }

  def sortInsert(list: List[Int], num: Int):List[Int]= {
    list match {
      case Nil => val newlist: List[Int] = List(num)
        newlist
      // returns single element list
      case x :: rest => if (num < x) {
        val newlist: List[Int] = num :: x :: rest
        newlist
        // if number is less than the first element, places the number at the beginning of the list
      }
      else {
        val newlist: List[Int] = x :: sortInsert(rest, num)
        newlist
        // else, ignores the first element and applies function on rest of the list

      }
    }

  }
  }

