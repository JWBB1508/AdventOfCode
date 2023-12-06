using AdventOfCode._2023._03;
using AdventOfCode._2023.Library;

const string Day = "03";

Console.WriteLine(Part.One);

Console.WriteLine(new EngineSchematic($"{Day}/example.txt", Part.One).GetAnswer());
Console.WriteLine(new EngineSchematic($"{Day}/data.txt", Part.One).GetAnswer());

Console.WriteLine(Part.Two);

Console.WriteLine(new EngineSchematic($"{Day}/example.txt", Part.Two).GetAnswer());
Console.WriteLine(new EngineSchematic($"{Day}/data.txt", Part.Two).GetAnswer());