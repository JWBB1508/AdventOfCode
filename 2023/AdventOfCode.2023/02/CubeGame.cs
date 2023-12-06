using AdventOfCode._2023.Library;
using System.Text.RegularExpressions;

namespace AdventOfCode._2023._02
{
    internal class CubeGame : APuzzle
    {
        private static readonly IDictionary<string, short> Max = new Dictionary<string, short>
        {
            { "Red", 12 },
            { "Green", 13 },
            { "Blue", 14 }
        };

        public CubeGame(string dataFilename, Part part)
            : base(dataFilename, part)
        { }

        public override string GetAnswer()
        {
            switch (Part)
            {
                case Part.One:
                    return SumPossibleGames().ToString();
                case Part.Two:
                    return SumPowers().ToString();
                default:
                    throw new ArgumentOutOfRangeException(nameof(Part), Part, "Invalid Part");
            }
        }

        private int SumPossibleGames()
        {
            int sum = 0;
            foreach (var line in File.ReadLines(DataFilename))
            {
                var game = Game.FromLine(line);

                if (game.Results.All(x => x.Red <= Max["Red"] && x.Green <= Max["Green"] && x.Blue <= Max["Blue"]))
                {
                    sum += game.Id;
                }
            }

            return sum;
        }

        private int SumPowers()
        {
            int sum = 0;
            foreach (var line in File.ReadLines(DataFilename))
            {
                var game = Game.FromLine(line);

                sum += game.Results.Select(x => x.Red).Max()
                    * game.Results.Select(x => x.Green).Max()
                    * game.Results.Select(x => x.Blue).Max();
            }

            return sum;
        }

        private class Game
        {
            public int Id { get; }

            public IEnumerable<Result> Results { get; }

            private Game(int id, IEnumerable<Result> results)
            {
                Id = id;
                Results = results;
            }

            public static Game FromLine(string line)
            {
                var match = Regex.Match(line, @"^Game (\d+): (.*)$");

                if (!match.Success)
                {
                    throw new ArgumentException($"Invalid line: {line}", nameof(line));
                }

                return new Game(
                    int.Parse(match.Groups[1].Value),
                    match.Groups[2].Value.Split(';').Select(Result.FromLine));
            }

            internal class Result
            {
                public short Red { get; }

                public short Green { get; }

                public short Blue { get; }

                public Result(short red, short green, short blue)
                {
                    Red = red;
                    Green = green;
                    Blue = blue;
                }

                public static Result FromLine(string line)
                {
                    return new Result(GetValue(line, "red"), GetValue(line, "green"), GetValue(line, "blue"));
                }

                private static short GetValue(string line, string colour)
                {
                    var match = Regex.Match(line, @$"(\d+) {colour}");
                    if (match.Success)
                    {
                        return short.Parse(match.Groups[1].Value);
                    }
                    else
                    {
                        return 0;
                    }
                }
            }
        }
    }
}