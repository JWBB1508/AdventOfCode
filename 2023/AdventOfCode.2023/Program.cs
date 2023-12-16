using AdventOfCode._2023.Library;

while (true)
{
    string? inputDay = string.Empty;
    short day;
    while (!short.TryParse(inputDay, out day))
    {
        Console.Write("Enter Day (q to exit): ");
        inputDay = Console.ReadLine();

        if (inputDay == "q")
        {
            Environment.Exit(0);
        }
    }

    Console.WriteLine(Part.One);

    Console.WriteLine(PuzzleFactory.GetPuzzle(day, $"{day:'0'#}/example.txt", Part.One).GetAnswer());
    Console.WriteLine(PuzzleFactory.GetPuzzle(day, $"{day:'0'#}/data.txt", Part.One).GetAnswer());

    Console.WriteLine(Part.Two);

    Console.WriteLine(PuzzleFactory.GetPuzzle(day, $"{day:'0'#}/example.txt", Part.Two).GetAnswer());
    Console.WriteLine(PuzzleFactory.GetPuzzle(day, $"{day:'0'#}/data.txt", Part.Two).GetAnswer());
}