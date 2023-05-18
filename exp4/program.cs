// The namespace declaration provides a way to logically organize your classes
using Classes;
namespace Classes;

public class House
{
  // House properties
    public string Address { get; }
    public int Size { get;}

  // House methods
    public void SellHouse(decimal amount, DateTime date)
    {
    }
}
public House(string address, int squareFeet)
{
    this.Address = address;
    this.Size = squareFeet;
}


// Let's create a 1500 square foot house on Candy Cane Lane
var house = new House("123 Candy Cane Lane", 1500);