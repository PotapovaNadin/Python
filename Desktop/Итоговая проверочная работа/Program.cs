/* Задача: 
Написать программу, которая из имеющегося массива строк 
формирует массив из строк, длина которых меньше либо равна 3 символа.
*/

Console.WriteLine("Imput size");
int size = Convert.ToInt32(Console.ReadLine());
string [] array1 = CreateArray(size);
ShowArray(array1);

string[] CreateArray (int size)
{   
    string [] array1 = new string[size];
    for(int i = 0; i < size; i++)
    {
        Console.WriteLine("введите строку ");
        array1[i] = Console.ReadLine();
    }
    return array1;
}

void ShowArray(string[] array)
{
    for(int i = 0; i < array.Length; i++)
        Console.Write(array[i] + " ");
    
    Console.WriteLine();
}
string [] array2 = new string [array1.Length];

void FindThirdLenght(string[] array1, string [] array2)
{
    for (int i = 0; i < array1.Length; i++)
    {   
        int count = 0;
        if(array1[i].Length < 4)
        {
            array2[count] = array1[i];
            Console.Write($"{array2[count]}, ");
            count++;
        }
    }
}

FindThirdLenght(array1, array2);

