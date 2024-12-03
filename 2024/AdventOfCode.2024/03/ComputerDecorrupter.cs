using AdventOfCode._2024.Library;
using System.Text.RegularExpressions;

namespace AdventOfCode._2024._03
{
    internal class ComputerDecorrupter : APuzzle
    {
        private readonly Regex _mulRegex;
        private readonly Regex _doRegex;

        public ComputerDecorrupter(string dataFilename, Part part) : base(dataFilename, part)
        {
            // Got stuck on this for ages before adding RegexOptions.Singleline - nasty newlines in the puzzle input!
            _mulRegex = new Regex(@"mul\((\d{1,3}),(\d{1,3})\)", RegexOptions.Singleline);
            _doRegex = new Regex(@"(^|do\(\)).*?(don't\(\)|$)", RegexOptions.Singleline);
        }

        public override string GetAnswer()
        {
            return Part switch
            {
                Part.One => _mulRegex.Matches(File.ReadAllText(DataFilename))
                .Sum(x => short.Parse(x.Groups[1].Value) * short.Parse(x.Groups[2].Value))
                .ToString(),
                Part.Two => _doRegex.Matches(File.ReadAllText(DataFilename))
                .SelectMany(x => _mulRegex.Matches(x.Value))
                .Sum(x => int.Parse(x.Groups[1].Value) * int.Parse(x.Groups[2].Value))
                .ToString(),
                _ => throw new ArgumentOutOfRangeException(nameof(Part), Part, "Unsupported Part"),
            };
        }
    }
}