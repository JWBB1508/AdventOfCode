using AdventOfCode._2023._02;
using AdventOfCode._2023.Library;

const string Day = "02";

Console.WriteLine(Part.One);

Console.WriteLine(new CubeGame($"{Day}/example.txt", Part.One).GetAnswer());
Console.WriteLine(new CubeGame($"{Day}/data.txt", Part.One).GetAnswer());

Console.WriteLine(Part.Two);

Console.WriteLine(new CubeGame($"{Day}/example.txt", Part.Two).GetAnswer());
Console.WriteLine(new CubeGame($"{Day}/data.txt", Part.Two).GetAnswer());