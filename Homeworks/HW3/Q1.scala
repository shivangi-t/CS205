/**
  * Created by shivangi on 26/10/16.
  */
case class Queue(list: List[Any]) {

  override def equals(obj: Any): Boolean = obj match{
    case _ @ Queue(list2: List[Any]) => list == list2
    case _ => false
  }

  def Enqueue(item: Any): Queue = {
    print(item+" added")
    new Queue(list:+item)
  }

  def Dequeue: Queue = {
    print (list.head)
    new Queue(list.tail)

  }

}
