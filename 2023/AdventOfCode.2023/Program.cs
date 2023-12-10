using AdventOfCode._2023.Library;

string? inputDay = string.Empty;
short day;
while (!short.TryParse(inputDay, out day))
{
    Console.Write("Enter Day: ");
    inputDay = Console.ReadLine();
}

Console.WriteLine(Part.One);

Console.WriteLine(PuzzleFactory.GetPuzzle(day, $"{day:'0'#}/example.txt", Part.One).GetAnswer());
Console.WriteLine(PuzzleFactory.GetPuzzle(day, $"{day:'0'#}/data.txt", Part.One).GetAnswer());

Console.WriteLine(Part.Two);

Console.WriteLine(PuzzleFactory.GetPuzzle(day, $"{day:'0'#}/example.txt", Part.Two).GetAnswer());
Console.WriteLine(PuzzleFactory.GetPuzzle(day, $"{day:'0'#}/data.txt", Part.Two).GetAnswer());