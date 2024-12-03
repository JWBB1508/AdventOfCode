namespace AdventOfCode._2024.Library
{
    internal static class PuzzleFactory
    {
        public static APuzzle GetPuzzle(short day, string dataFilename, Part part)
        {
            return day switch
            {
                1 => new _01.ListDistanceFinder(dataFilename, part),
                2 => new _02.ReactorReportAnalyser(dataFilename, part),
                _ => throw new ArgumentOutOfRangeException(nameof(day), day, $"Day {day} not supported by PuzzleFactory"),
            };
        }
    }
}