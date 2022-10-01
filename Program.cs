//using System;

bool IsDigitsOnly(string str)
{
    foreach (char c in str)
    {
        if (c < '0' || c > '9')
            return false;
    }

    return true;
}

Console.Write("Введите строку 1: ");
char[] str1 = Console.ReadLine().ToCharArray();
Console.Write("Введите строку 2: ");
char[] str2 = Console.ReadLine().ToCharArray();
int end = 0;
for (int i = 0; i < str1.Length && i < str2.Length; i++)
{
    Console.WriteLine($"{str1[i]} + {str2[i]} = {(char)(str1[i] + str2[i])}");
    end = i + 1;
}
while (end < str2.Length)
{
    Console.WriteLine($"  + {str2[end]} = {str2[end]}");
    end++;
}
while (end < str1.Length)
{
    Console.WriteLine($"{str1[end]} +   = {str1[end]}");
    end++;
}

/*-------------Часть 1---------------*/

Console.Write("Введите число: ");
int num;
String str = Console.ReadLine();
if (IsDigitsOnly(str))
{
    num = Convert.ToInt32(str);
    if (num < 10)
    {
        Console.WriteLine($"В числе всего одна цифра = {num}");
    }
    else
    {
        int tmp = num;
        while (tmp > 99)
        {
            tmp /= 10;
        }
        Console.WriteLine($"Вторая цифра слева = {tmp % 10}");
    }
}
else
{
    Console.WriteLine($"Введено не число");
    return;
}

/*-------------Часть 2---------------*/

Console.Write("Введите A: ");
int A;
str = Console.ReadLine();
if (IsDigitsOnly(str))
{
    A = Convert.ToInt32(str);
}
else
{
    Console.WriteLine($"Введено не число");
    return;
}
Console.Write("Введите B: ");
int B;
str = Console.ReadLine();
if (IsDigitsOnly(str))
{
    B = Convert.ToInt32(str);
}
else
{
    Console.WriteLine($"Введено не число");
    return;
}
Console.Write("Введите C: ");
int C;
str = Console.ReadLine();
if (IsDigitsOnly(str))
{
    C = Convert.ToInt32(str);
}
else
{
    Console.WriteLine($"Введено не число");
    return;
}

if (A == 0 || B == 0 || C == 0)
{
    Console.WriteLine($"На ноль делить нельзя");
}
else if (num % A == 0 && num % B == 0 && num % C == 0)
{
    Console.WriteLine("Делится без остатка");
}
else
{
    Console.WriteLine("Не делится без остатка");
}

/*-------------Часть 3---------------*/

bool were = false;
for (int i = 10; i < 100; i++)
{
    if (i * 2 % 10 == 8 && i * 3 % 10 == 4)
    {
        Console.WriteLine(i);
        were = true;
    }
}
if (!were)
{
    Console.WriteLine("Таких чисел не найдено");
}